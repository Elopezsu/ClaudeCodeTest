# ValuSignal 2026 — LinkedIn Sponsor Sales Kit: Skill Execution Roadmap
**Date:** 2026-06-02  
**Objective:** Complete LinkedIn sales kit for sponsor outreach  
**Output language:** English  
**Pipeline:** 3-step express

---

## [1. EXECUTIVE STRATEGY]

The principle here is **80/20 Prompt Chaining** with an inverted build: the final deliverable is a complete LinkedIn sales kit in Eunice's voice — so the chain runs backwards from voice alignment → objection handling → message copy. Since all inputs already exist in memory (outreach plan, tier decks, agreements), the pipeline enters at Step 1 with zero data collection overhead. Three steps, each feeding directly into the next, with one HITL checkpoint before the final voice pass.

---

## [2. THE SKILL PIPELINE]

### Paso 1: LinkedIn Message Generation

- 🟢 **Skill:** `/sub-linkedin-writer`
- 📥 **Input:** Paste the full outreach plan (`ValuSignal2026-Sponsor-LinkedIn-Outreach-Plan.md`) + this instruction: *"Generate LinkedIn copy in English for ValuSignal 2026 sponsor outreach. Create: (1) connection request message per tier (Core/Featured/Title), (2) follow-up message per tier, (3) soft bump message. Target personas: founders for Tier B, VP Marketing/Director for Tier A, Corporate Relations for Tier C. Tone: peer-to-peer, not salesy. Max 300 chars for connection requests."*
- 📤 **Output:** 9 messages total (3 tiers × 3 message types), ready to copy-paste
- 🔄 **Handoff:** Copy all 9 messages → feed into Paso 2 alongside the tier packages

---

### Paso 2: Objection Prediction & Response Framework

- 🟢 **Skill:** `/sub-objection-predictor`
- 📥 **Input:** The 9 messages from Paso 1 + tier pricing (Core $1K / Featured $2.5K / Title $10K) + this instruction: *"For each sponsor tier, predict the 3 most likely objections a decision-maker will raise on LinkedIn and provide a 1-2 sentence response for each. Context: ValuSignal 2026 is the first virtual conference for U.S. appraisal professionals, ~2,000–3,000 attendees, Zoom Events platform. Output in English."*
- 📤 **Output:** 9 objection-response pairs (3 per tier) formatted for quick reference during live conversations
- 🔄 **Handoff:** Combine with Paso 1 output into a single document → feed into Paso 3

---

### Paso 3: Voice Alignment — Eunice's Tone

- 🟢 **Skill:** `/mi-tono`
- 📥 **Input:** The full combined document from Pasos 1+2 + this instruction: *"Rewrite all messages and objection responses in my authentic LinkedIn voice — direct, warm, peer-to-peer, never corporate. Output in English. Keep connection requests under 300 chars. Do not change the strategic logic, only the voice and phrasing."*
- 📤 **Output:** Final LinkedIn Sales Kit — all messages + objection handling in Eunice's voice, ready to use
- 🔄 **Handoff:** Save to repo as `ValuSignal2026-Sponsor-LinkedIn-SalesKit.md`

---

## [3. HITL CHECKPOINTS]

**🟡 HITL 1 — After Paso 1**
- What to review: (1) Do the connection request messages feel like a peer reaching out, not a sales rep? (2) Is the tier differentiation clear without naming the price upfront? (3) Does the Tier A version feel executive-appropriate?
- Estimated time: 5 minutes
- If something's off: Adjust the tone instruction and re-run Paso 1 before proceeding to Paso 2

**🟡 HITL 2 — After Paso 3 (final approval)**
- What to review: (1) Does every message sound like you — not like a template? (2) Are the objection responses things you'd actually say in a real conversation? (3) Is anything too long for a LinkedIn message window?
- Estimated time: 10 minutes
- If something's off: Flag the specific messages to `/mi-tono` with: *"Rewrite [message X] — it still sounds too formal / too generic / too long"*

---

## [4. QUICK START COMMAND]

Copy and paste this to start immediately:

```
Run /sub-linkedin-writer with this context:

I need LinkedIn outreach copy in English for ValuSignal 2026 sponsor sales. 

CONTEXT: ValuSignal 2026 is the first virtual conference for U.S. appraisal and valuation professionals. ~2,000–3,000 attendees. Zoom Events with Expo Hall. Three sponsor tiers: Core $1,000 (20 slots), Featured $2,500 (10 slots), Title $10,000 (1 slot exclusive). Sales contact: Eunice Lopez, Events Manager.

TARGET PERSONAS:
- Tier B (tech startups): Founders / CEOs — companies like restb.ai, Aivre, True Footage, ProxyPics, Jaro
- Tier A (enterprise AMCs): VP Marketing / Director of Partnerships — companies like Class Valuation, Clear Capital, Rocket Mortgage, ServiceLink
- Tier C (education/insurance): Director of Corporate Relations — companies like McKissock, OREP, CE Shop

DELIVERABLE: For each tier, write:
1. Connection request message (max 300 chars) — peer tone, no pitch
2. Follow-up message (sent 2-3 days after connect) — introduce ValuSignal, soft ask for deck interest
3. Soft bump (day 6-7 if no reply) — one line, no pressure

Output in English. Peer-to-peer tone throughout. Never mention price in the first two messages.
```

---

## [VERSIONING LOG]

`v1.0 — 2026-06-02 — Skill Execution Roadmap generated for: Complete LinkedIn Sales Kit for ValuSignal 2026 sponsors. Skills in pipeline: /sub-linkedin-writer → /sub-objection-predictor → /mi-tono. Entry point: Step 1 (all inputs already in memory).`
