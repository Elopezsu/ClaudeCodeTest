/**
 * Skool → Loom Transcript Extractor
 *
 * Cómo usar:
 *   1. npm install && npm run install-browsers
 *   2. node extract.js
 *   3. Inicia sesión en Skool en la ventana que abre
 *   4. Presiona Enter — el resto es automático
 */

const { chromium } = require('playwright');
const fs   = require('fs');
const path = require('path');
const readline = require('readline');

const CLASSROOM_URL = 'https://www.skool.com/link-system-8225/classroom';
const GROUP_SLUG    = 'link-system-8225';
const OUTPUT_DIR    = path.join(__dirname, 'transcripts');
const DELAY_MS      = 1200;

function waitForEnter(prompt) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  return new Promise(resolve => rl.question(prompt, () => { rl.close(); resolve(); }));
}
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }
function sanitize(s) {
  return s.replace(/[^a-z0-9áéíóúüñ\s\-]/gi, '').trim().replace(/\s+/g, '_').substring(0, 55);
}

// ─── Extraer lista de cursos desde __NEXT_DATA__ ──────────────────────────────
async function extractCourses(page) {
  return page.evaluate(() => {
    try {
      const data    = JSON.parse(document.getElementById('__NEXT_DATA__').textContent);
      const courses = data?.props?.pageProps?.renderData?.allCourses
                   || data?.props?.pageProps?.allCourses || [];
      return courses.map(c => ({
        id:         c.id,
        slug:       c.name,
        title:      c.metadata?.title || c.name,
        numModules: c.metadata?.numModules || 0,
      }));
    } catch { return []; }
  });
}

// ─── Navegar a un curso e interceptar la API de módulos ───────────────────────
async function loadCourseAndGetLessons(page, course) {
  const courseUrl = `https://www.skool.com/${GROUP_SLUG}/classroom/${course.slug}`;
  let apiModules  = null;

  // Escuchar respuestas de la API de Skool que contengan módulos
  const handler = async (response) => {
    const url = response.url();
    if (
      (url.includes('/api/') || url.includes('skool.com')) &&
      (url.includes('module') || url.includes('course') || url.includes('lesson'))
    ) {
      try {
        const ct = response.headers()['content-type'] || '';
        if (!ct.includes('json')) return;
        const json = await response.json();
        // Buscar array de módulos en la respuesta
        const candidate = json?.modules || json?.courseModules || json?.data?.modules
                       || json?.data?.courseModules || json?.data;
        if (Array.isArray(candidate) && candidate.length > 0 && candidate[0].id) {
          if (!apiModules || candidate.length > apiModules.length) {
            apiModules = candidate;
          }
        }
      } catch {}
    }
  };
  page.on('response', handler);

  await page.goto(courseUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await sleep(4000); // Dar tiempo a React + llamadas API

  page.off('response', handler);

  // Intentar también desde el DOM renderizado por React
  const domLessons = await page.evaluate(() => {
    const results = [];
    const seen    = new Set();

    // Links con ?md= (query param de módulo en Skool)
    document.querySelectorAll('a[href*="?md="], a[href*="&md="]').forEach(a => {
      if (!seen.has(a.href)) {
        seen.add(a.href);
        results.push({
          href:  a.href,
          title: a.textContent.trim().replace(/\s+/g, ' ').substring(0, 80),
        });
      }
    });

    // Si no hay links, buscar cualquier elemento que parezca lección
    if (results.length === 0) {
      document.querySelectorAll('[class*="Module"], [class*="Lesson"], [class*="module"], [class*="lesson"]').forEach(el => {
        const a = el.querySelector('a') || (el.tagName === 'A' ? el : null);
        if (a && a.href && !seen.has(a.href)) {
          seen.add(a.href);
          results.push({ href: a.href, title: a.textContent.trim().substring(0, 80) });
        }
      });
    }

    return results;
  });

  // Convertir módulos de API a formato común
  if (apiModules && apiModules.length > 0) {
    return apiModules.map(m => ({
      id:       m.id,
      slug:     m.name || m.slug,
      title:    m.metadata?.title || m.title || m.name || m.id,
      videoUrl: m.metadata?.video?.video_url || m.videoUrl || '',
      href:     null,
    }));
  }

  // Fallback: links del DOM
  if (domLessons.length > 0) {
    return domLessons.map(l => ({ id: null, slug: null, title: l.title, videoUrl: '', href: l.href }));
  }

  return [];
}

// ─── Extraer Loom ID de la página de lección ──────────────────────────────────
async function extractLoomId(page) {
  return page.evaluate(() => {
    for (const iframe of document.querySelectorAll('iframe')) {
      const src = iframe.src || iframe.getAttribute('data-src') || '';
      if (src.includes('loom.com')) {
        const m = src.match(/loom\.com\/embed\/([a-f0-9]{32})/i);
        if (m) return m[1];
      }
    }
    const el = document.querySelector('[data-loom-id]');
    if (el) return el.getAttribute('data-loom-id');
    const m = document.documentElement.innerHTML.match(
      /loom\.com\/(?:embed|share)\/([a-f0-9]{32})/i
    );
    return m ? m[1] : null;
  });
}

// ─── Extraer transcript de Loom ───────────────────────────────────────────────
async function getLoomTranscript(context, loomId) {
  const page = await context.newPage();
  let transcript = null;

  try {
    page.on('response', async (response) => {
      const url = response.url();
      if ((url.includes('transcript') || url.includes('caption') || url.endsWith('.vtt')) && !transcript) {
        try {
          const body = await response.text();
          if (body && body.length > 80) transcript = body;
        } catch {}
      }
    });

    await page.goto(`https://www.loom.com/share/${loomId}`, {
      waitUntil: 'domcontentloaded', timeout: 30000,
    });
    await sleep(3000);

    // __NEXT_DATA__
    if (!transcript) {
      transcript = await page.evaluate(() => {
        try {
          const data  = JSON.parse(document.getElementById('__NEXT_DATA__').textContent);
          const video = data?.props?.pageProps?.ssr_video
                     || data?.props?.pageProps?.video
                     || data?.props?.pageProps?.videoData;
          if (!video) return null;
          if (video.transcript) {
            return Array.isArray(video.transcript)
              ? video.transcript.map(t => t.text || t.content || '').join(' ')
              : String(video.transcript);
          }
          if (video.captions) {
            return Array.isArray(video.captions)
              ? video.captions.map(c => c.text || c.caption || '').join(' ')
              : String(video.captions);
          }
          return null;
        } catch { return null; }
      });
    }

    // DOM visible
    if (!transcript) {
      transcript = await page.evaluate(() => {
        for (const sel of ['[data-testid="transcript-container"]', '[class*="Transcript"]', '[class*="transcript"]']) {
          const el = document.querySelector(sel);
          if (el?.textContent?.trim().length > 50) return el.textContent.trim();
        }
        return null;
      });
    }

    // JSON embebido
    if (!transcript) {
      transcript = await page.evaluate(() => {
        const m = document.documentElement.innerHTML.match(/"transcript"\s*:\s*"([^"]{100,})"/);
        return m ? m[1].replace(/\\n/g, '\n').replace(/\\"/g, '"') : null;
      });
    }

  } catch (err) {
    console.error(`    Loom error ${loomId}: ${err.message}`);
  } finally {
    await page.close();
  }

  return transcript;
}

// ─── MAIN ─────────────────────────────────────────────────────────────────────
async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const browser = await chromium.launch({ headless: false, slowMo: 60 });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page    = await context.newPage();

  // Login
  await page.goto('https://www.skool.com/login');
  await waitForEnter('\n→ Inicia sesión en Skool, luego presiona Enter aquí: ');

  // Cargar classroom
  console.log('\nCargando classroom...');
  await page.goto(CLASSROOM_URL, { waitUntil: 'domcontentloaded' });
  await sleep(3000);

  const courses = await extractCourses(page);
  if (courses.length === 0) {
    fs.writeFileSync(path.join(OUTPUT_DIR, '_classroom_debug.html'), await page.content());
    console.log('⚠ No se encontraron cursos. Ver _classroom_debug.html');
    await browser.close();
    return;
  }

  const total = courses.reduce((s, c) => s + c.numModules, 0);
  console.log(`\n✓ ${courses.length} cursos, ~${total} lecciones:`);
  courses.forEach((c, i) => console.log(`  ${i + 1}. ${c.title} (${c.numModules})`));

  await waitForEnter('\n→ Presiona Enter para iniciar: ');

  const summary      = [];
  const noLoom       = [];
  const noTranscript = [];
  let idx = 0;

  for (const course of courses) {
    const courseDir = path.join(OUTPUT_DIR, sanitize(course.title));
    if (!fs.existsSync(courseDir)) fs.mkdirSync(courseDir, { recursive: true });

    console.log(`\n━━ ${course.title} ━━━━━━━━━━━━━━━━━━━━━━━━━`);

    const lessons = await loadCourseAndGetLessons(page, course);

    if (lessons.length === 0) {
      console.log('  ⚠ Sin lecciones — guardando debug');
      fs.writeFileSync(path.join(courseDir, '_debug.html'), await page.content());
      continue;
    }

    console.log(`  ${lessons.length} lecciones`);

    for (const lesson of lessons) {
      idx++;
      process.stdout.write(`  [${String(idx).padStart(3)}] ${lesson.title.substring(0, 55).padEnd(56)}`);

      let loomId = null;

      // 1. Loom en el video_url del módulo
      if (lesson.videoUrl?.includes('loom.com')) {
        const m = lesson.videoUrl.match(/loom\.com\/(?:embed|share)\/([a-f0-9]{32})/i);
        if (m) loomId = m[1];
      }

      // 2. Navegar a la lección y buscar el embed
      if (!loomId) {
        const lessonUrl = lesson.href
          || `https://www.skool.com/${GROUP_SLUG}/classroom/${course.slug}?md=${lesson.slug || lesson.id}`;
        try {
          await page.goto(lessonUrl, { waitUntil: 'domcontentloaded', timeout: 25000 });
          await sleep(2000);
          loomId = await extractLoomId(page);
        } catch (err) {
          process.stdout.write(`✗ nav error\n`);
          noLoom.push({ course: course.title, lesson: lesson.title });
          continue;
        }
      }

      const fname = `${String(idx).padStart(3)}_${sanitize(lesson.title)}.txt`;
      const fpath = path.join(courseDir, fname);

      if (!loomId) {
        process.stdout.write(`⚠ sin Loom\n`);
        noLoom.push({ course: course.title, lesson: lesson.title });
        fs.writeFileSync(fpath, `# ${lesson.title}\nCurso: ${course.title}\n\n⚠️ Sin video Loom\n`);
        continue;
      }

      process.stdout.write(`Loom:${loomId.substring(0,8)}… `);
      const transcript = await getLoomTranscript(context, loomId);

      if (!transcript || transcript.trim().length < 30) {
        process.stdout.write(`✗ sin transcript\n`);
        noTranscript.push({ course: course.title, lesson: lesson.title, loomId });
        fs.writeFileSync(fpath, `# ${lesson.title}\nLoom: https://www.loom.com/share/${loomId}\n\n⚠️ Transcript no disponible\n`);
        continue;
      }

      fs.writeFileSync(fpath, [
        `# ${lesson.title}`,
        `Curso: ${course.title}`,
        `Loom: https://www.loom.com/share/${loomId}`,
        '', '─────────────────────────────────────', '',
        transcript.trim(),
      ].join('\n'), 'utf8');

      summary.push({ course: course.title, lesson: lesson.title, file: fname });
      process.stdout.write(`✓\n`);

      await sleep(DELAY_MS);
    }
  }

  // Resumen
  fs.writeFileSync(path.join(OUTPUT_DIR, '_RESUMEN.txt'), [
    `Extracción: ${new Date().toLocaleString()}`,
    `✅ Extraídos: ${summary.length}`,
    `❌ Sin transcript: ${noTranscript.length}`,
    `⚠️  Sin Loom: ${noLoom.length}`, '',
    '## Extraídos', ...summary.map(s => `- [${s.course}] ${s.lesson}`), '',
    '## Sin transcript', ...noTranscript.map(s => `- [${s.course}] ${s.lesson} → https://www.loom.com/share/${s.loomId}`), '',
    '## Sin Loom', ...noLoom.map(s => `- [${s.course}] ${s.lesson}`),
  ].join('\n'), 'utf8');

  console.log(`\n${'═'.repeat(50)}`);
  console.log(`✅  Extraídos:      ${summary.length}`);
  console.log(`❌  Sin transcript: ${noTranscript.length}`);
  console.log(`⚠️   Sin Loom:      ${noLoom.length}`);
  console.log(`📁  ${OUTPUT_DIR}`);
  console.log('═'.repeat(50));

  await browser.close();
}

main().catch(err => { console.error('Error fatal:', err); process.exit(1); });
