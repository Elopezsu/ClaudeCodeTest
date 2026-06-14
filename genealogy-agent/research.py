#!/usr/bin/env python3
"""
Agente de Investigación Genealógica Autónoma — Familia López Suárez
Inspirado en karpathy/autoresearch: da al agente una métrica, herramientas, y lo sueltas.

Fuentes: Geni.com, WikiTree, FindAGrave, MyHeritage, DuckDuckGo
(FamilySearch bloqueado por Incapsula — requiere API corporativa)
"""

import asyncio
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

import anthropic
from playwright.async_api import async_playwright, BrowserContext

BASE_DIR = Path(__file__).parent
TREE_FILE = BASE_DIR / "tree.json"
LOG_FILE = BASE_DIR / "log.md"
PROGRAM_FILE = BASE_DIR / "program.md"


# ── Árbol ─────────────────────────────────────────────────────────────────────

def load_tree() -> dict:
    with open(TREE_FILE, encoding="utf-8") as f:
        return json.load(f)


def save_tree(tree: dict):
    with open(TREE_FILE, "w", encoding="utf-8") as f:
        json.dump(tree, f, ensure_ascii=False, indent=2)


def get_gaps(tree: dict) -> list[tuple[str, dict]]:
    gaps = []
    for pid, person in tree["people"].items():
        if not person.get("parents") and not person.get("searched"):
            gaps.append((pid, person))
    gaps.sort(key=lambda x: x[1].get("search_priority", 1), reverse=True)
    return gaps


def print_metric(tree: dict):
    confirmed = sum(1 for p in tree["people"].values() if p.get("parents"))
    total = len(tree["people"])
    gaps = len(get_gaps(tree))
    print(f"  Métrica: {confirmed}/{total} con padres | Gaps pendientes: {gaps}")


# ── Log ───────────────────────────────────────────────────────────────────────

def log_finding(person_name: str, finding: str, source: str, confidence: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = (
        f"\n---\n## {timestamp} — {person_name}\n"
        f"**Confianza:** {confidence}  \n**Fuente:** {source}  \n**Hallazgo:** {finding}\n"
    )
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


def init_log():
    if not LOG_FILE.exists():
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("# Log de Investigación Genealógica\n\nIniciado: " + datetime.now().strftime("%Y-%m-%d %H:%M") + "\n")


# ── Fetch helper ──────────────────────────────────────────────────────────────

async def fetch(ctx: BrowserContext, url: str, wait_ms: int = 4000) -> str:
    """Abre pestaña nueva, navega, extrae texto, cierra."""
    page = await ctx.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await page.wait_for_timeout(wait_ms)
        return (await page.text_content("body") or "")[:6000]
    except Exception as e:
        return f"Error: {e}"
    finally:
        try:
            await page.close()
        except Exception:
            pass


# ── Búsquedas ─────────────────────────────────────────────────────────────────

async def search_geni(ctx: BrowserContext, person: dict) -> str:
    """Geni.com — árbol mundial colaborativo (accesible sin login)."""
    name = person["name"].replace(" ", "+")
    url = f"https://www.geni.com/search?search_type=people&names={name}"
    return await fetch(ctx, url, wait_ms=5000)


async def search_wikitree(ctx: BrowserContext, person: dict) -> str:
    """WikiTree — árbol genealógico colaborativo gratuito."""
    parts = person["name"].split()
    given = parts[0]
    surname = parts[-1] if len(parts) > 1 else ""
    url = f"https://www.wikitree.com/index.php?title=Special:SearchPerson&FirstName={given}&LastName={surname}&BirthDecade=&BirthCountry=Colombia"
    return await fetch(ctx, url, wait_ms=4000)


async def search_findagrave(ctx: BrowserContext, person: dict) -> str:
    """FindAGrave — registros de tumbas y defunciones."""
    name = person["name"].replace(" ", "+")
    url = f"https://www.findagrave.com/memorial/search?q={name}&locationId=country_37"
    return await fetch(ctx, url, wait_ms=4000)


async def search_myheritage(ctx: BrowserContext, person: dict) -> str:
    """MyHeritage — búsqueda pública de registros."""
    parts = person["name"].split()
    given = parts[0]
    surname = " ".join(parts[1:]) if len(parts) > 1 else ""
    url = f"https://www.myheritage.com/research/record-search?action=queryRecords&formId=master&formMode=1&displayMode=compact&numResults=20&qfn={given}&qln={surname}&qby=&qbdy=&qbd={person.get('birth_year_min',1880)},{person.get('birth_year_max',1920)}&qbo=Colombia"
    return await fetch(ctx, url, wait_ms=5000)


async def search_duckduckgo(ctx: BrowserContext, person: dict) -> str:
    """DuckDuckGo HTML — búsqueda genealógica sin CAPTCHA."""
    name = person["name"]
    place = person.get("birth_place", "Colombia")
    birth_from = person.get("birth_year_min", 1880)
    birth_to = person.get("birth_year_max", 1920)
    query = f'"{name}" genealogía {place} nacimiento {birth_from} {birth_to} Colombia'
    url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
    return await fetch(ctx, url, wait_ms=3000)


async def search_duckduckgo_apellido(ctx: BrowserContext, person: dict) -> str:
    """DuckDuckGo — búsqueda por apellido + región."""
    parts = person["name"].split()
    surname = parts[-1] if parts else ""
    place = person.get("birth_place", "Colombia")
    query = f'apellido "{surname}" genealogía {place} Colombia historia familia'
    url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
    return await fetch(ctx, url, wait_ms=3000)


async def search_prasca_especial(ctx: BrowserContext) -> str:
    """Búsqueda específica apellido Prasca (origen italiano Colombia)."""
    query = 'Prasca Colombia Barranquilla genealogía italiano inmigrante "siglo XIX" familia'
    url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}"
    return await fetch(ctx, url, wait_ms=3000)


async def run_all_searches(ctx: BrowserContext, person: dict) -> dict:
    print(f"    → Geni.com...")
    r_geni = await search_geni(ctx, person)

    print(f"    → WikiTree...")
    r_wiki = await search_wikitree(ctx, person)

    print(f"    → FindAGrave...")
    r_grave = await search_findagrave(ctx, person)

    print(f"    → MyHeritage...")
    r_mh = await search_myheritage(ctx, person)

    print(f"    → DuckDuckGo (nombre completo)...")
    r_ddg1 = await search_duckduckgo(ctx, person)

    print(f"    → DuckDuckGo (apellido + región)...")
    r_ddg2 = await search_duckduckgo_apellido(ctx, person)

    results = {
        "geni": r_geni,
        "wikitree": r_wiki,
        "findagrave": r_grave,
        "myheritage": r_mh,
        "duckduckgo_nombre": r_ddg1,
        "duckduckgo_apellido": r_ddg2,
    }

    if "Prasca" in person["name"]:
        print(f"    → Prasca italiano (especial)...")
        results["prasca_especial"] = await search_prasca_especial(ctx)

    return results


# ── Evaluación con Claude ──────────────────────────────────────────────────────

def evaluate_with_claude(client: anthropic.Anthropic, person: dict, results: dict, program: str) -> dict:
    results_text = "\n\n".join(
        f"=== {src.upper()} ===\n{text}" for src, text in results.items()
    )

    prompt = f"""Eres investigador genealógico experto en Colombia (Antioquia, Bolívar, Costa Caribe, Bajo Cauca).

CONTEXTO DEL PROYECTO:
{program}

PERSONA BUSCADA:
- Nombre: {person['name']}
- Relación: {person.get('relationship', '?')}
- Lugar probable: {person.get('birth_place', 'Colombia')}
- Años estimados: {person.get('birth_year_min', '?')}–{person.get('birth_year_max', '?')}
- Contexto: {person.get('context', '')}

RESULTADOS DE BÚSQUEDA:
{results_text[:9000]}

Analiza si algún resultado corresponde a esta persona. Busca:
1. Nombre de sus padres (para extender el árbol)
2. Fechas y lugares exactos
3. Hermanos o familiares que confirmen identidad
4. Fuente documental citada

Niveles de confianza:
- "alta": nombre+apellido+lugar+año+fuente documental
- "media": nombre+apellido+lugar sin fuente documental directa
- "baja": coincidencia parcial o dudosa

Responde SOLO con JSON válido:
{{
  "found": true/false,
  "confidence": "alta/media/baja",
  "finding": "descripción del hallazgo o null",
  "parents": {{
    "father": {{"name": "Nombre Completo", "birth_year_approx": 1870, "birth_place": "lugar"}} ,
    "mother": {{"name": "Nombre Completo", "birth_year_approx": 1875, "birth_place": "lugar"}}
  }},
  "extra_data": {{"birth_date": "...", "birth_place": "...", "marriage_date": "..."}},
  "source": "nombre fuente + URL si aplica",
  "notes": "pistas concretas para seguir investigando"
}}"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1200,
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.content[0].text.strip()
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    return {"found": False, "confidence": "baja", "finding": None,
            "parents": {}, "extra_data": {}, "source": "", "notes": text}


# ── Actualizar árbol ───────────────────────────────────────────────────────────

def update_tree(tree: dict, person_id: str, person: dict, ev: dict) -> dict:
    parents = ev.get("parents", {})
    father = parents.get("father") or {}
    mother = parents.get("mother") or {}

    def next_gen(pid):
        m = re.match(r'G(\d+)', pid)
        return f"G{int(m.group(1))+1}" if m else "G4"

    father_id = mother_id = None

    if father.get("name"):
        father_id = f"{next_gen(person_id)}_father_of_{person_id}"
        if father_id not in tree["people"]:
            by = father.get("birth_year_approx") or 1880
            tree["people"][father_id] = {
                "name": father["name"],
                "birth_year_approx": by,
                "birth_place": father.get("birth_place", "Colombia"),
                "birth_year_min": by - 10,
                "birth_year_max": by + 10,
                "relationship": f"Padre de {person['name']}",
                "parents": None,
                "sources": [ev.get("source", "")],
                "confidence": ev["confidence"],
                "searched": False,
                "search_priority": 1,
            }

    if mother.get("name"):
        mother_id = f"{next_gen(person_id)}_mother_of_{person_id}"
        if mother_id not in tree["people"]:
            by = mother.get("birth_year_approx") or 1880
            tree["people"][mother_id] = {
                "name": mother["name"],
                "birth_year_approx": by,
                "birth_place": mother.get("birth_place", "Colombia"),
                "birth_year_min": by - 10,
                "birth_year_max": by + 10,
                "relationship": f"Madre de {person['name']}",
                "parents": None,
                "sources": [ev.get("source", "")],
                "confidence": ev["confidence"],
                "searched": False,
                "search_priority": 1,
            }

    tree["people"][person_id]["parents"] = {
        "father_id": father_id, "father_name": father.get("name"),
        "mother_id": mother_id, "mother_name": mother.get("name"),
    }

    extra = ev.get("extra_data", {})
    if extra.get("birth_date"):
        tree["people"][person_id]["birth_date"] = extra["birth_date"]
    if extra.get("birth_place"):
        tree["people"][person_id]["birth_place_confirmed"] = extra["birth_place"]

    sources = tree["people"][person_id].get("sources", [])
    sources.append(ev.get("source", ""))
    tree["people"][person_id]["sources"] = sources
    return tree


# ── Loop principal ─────────────────────────────────────────────────────────────

async def research_loop():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ Falta ANTHROPIC_API_KEY. Ejecuta: export ANTHROPIC_API_KEY='sk-ant-...'")
        sys.exit(1)

    ai = anthropic.Anthropic(api_key=api_key)
    program = PROGRAM_FILE.read_text(encoding="utf-8")
    init_log()

    print("\n🧬 Agente Genealógico López Suárez")
    print("   Fuentes: Geni | WikiTree | FindAGrave | MyHeritage | DuckDuckGo")
    print("=" * 60)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        ctx = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            locale="es-CO",
            viewport={"width": 1280, "height": 800},
        )

        iteration = 0
        while True:
            tree = load_tree()
            gaps = get_gaps(tree)
            print(f"\n[Iteración {iteration}]")
            print_metric(tree)

            if not gaps:
                print("\n✅ No quedan gaps. Investigación completa.")
                break

            person_id, person = gaps[0]
            print(f"\n🔍 {person['name']}")
            print(f"   {person.get('relationship','?')} | {person.get('birth_place','?')} | {person.get('birth_year_min','?')}–{person.get('birth_year_max','?')}")

            results = await run_all_searches(ctx, person)

            print(f"    → Evaluando con Claude...")
            ev = evaluate_with_claude(ai, person, results, program)

            found = ev.get("found", False)
            conf = ev.get("confidence", "baja")
            print(f"  {'✅ ENCONTRADO' if found else '❌ No encontrado'} (confianza: {conf})")

            if found and conf in ("alta", "media"):
                p_data = ev.get("parents", {})
                print(f"  Padre: {(p_data.get('father') or {}).get('name', '?')}")
                print(f"  Madre: {(p_data.get('mother') or {}).get('name', '?')}")
                print(f"  Fuente: {ev.get('source', '?')}")
                tree = update_tree(tree, person_id, person, ev)
                save_tree(tree)
                log_finding(person["name"], ev.get("finding", ""), ev.get("source", ""), conf)
                print(f"  💾 Árbol actualizado.")
            else:
                tree["people"][person_id]["searched"] = True
                tree["people"][person_id]["search_notes"] = ev.get("notes", "")[:500]
                save_tree(tree)
                print(f"  ⚠️  Marcado como buscado.")

            if ev.get("notes"):
                print(f"  Pistas: {ev['notes'][:250]}")

            iteration += 1
            await asyncio.sleep(2)

        await browser.close()
        print(f"\n🏁 Finalizado. Log: {LOG_FILE} | Árbol: {TREE_FILE}")


if __name__ == "__main__":
    asyncio.run(research_loop())
