# ValuSignal 2026 — Promo Email Sequences (June 2026)

**Created:** 2026-06-17  
**Context:** Two sequences built from the June 16 team meeting with Hansel.  
Sent from **Deanne / Eunice personal inboxes** (NOT Instantly). Instantly runs as Hansel — these run as his team.

---

## Placeholders to fill before sending

| Placeholder | What to add |
|---|---|
| `EARLYBIRD` | Promo code — confirmed |
| Pricing story | Standard $297 → early bird was $197 → code gives extra $10 off = **$187 final** |
| `[DEANNE LAST NAME]` | Deanne's full last name for signature |
| Sender name / reply-to | Set up Deanne + Eunice inboxes in your sending tool |

---

## SEQUENCE 1 — Warm Leads (~200 from Campaigns 1 & 2)

**Who they are:** Replied to or engaged with Hansel's Instantly cold emails. They know ValuSignal exists. They just haven't registered.  
**Goal:** Close with a personal promo code as a VIP gesture from Hansel's team.  
**Thread behavior:** Email 2 sends blank subject — lands in same thread as Email 1.

---

### Email 1 — Day 0

**Subject:** `Hansel asked us to reach out, {{first_name}}`

{{first_name}},

I'm Deanne — part of Hansel Dobbs's team at ValuSignal. He flagged your name as someone who'd been in touch and wanted to make sure you got a personal note before September.

Early bird closed June 15, but Hansel wanted you to have code **EARLYBIRD** at checkout — it brings the ticket to $187. That code is only valid through June 20.

September 18–19. Fully virtual. 70+ sessions including UAD 3.6 readiness, AI workshops, and speakers like Kelly Davids (President, The Appraisal Foundation) and Tony Pistilli (Restb.ai). No flights, no hotels.

If anything comes up before you register, reply here and I'll make sure Hansel sees it.

Deanne [DEANNE LAST NAME]  
On behalf of Hansel Dobbs, MNAA, CDEI | ValuSignal 2026

---

### Email 2 — Day 5 (blank subject — threads under Email 1)

*[Leave subject line blank in your sending tool so it threads as a reply]*

{{first_name}},

Early bird closed June 15 — **EARLYBIRD** at valusignal.com/register is the three-day extension Hansel held for people who'd been in the conversation. It expires June 20 and brings the ticket to $187.

Reply here if anything comes up.

Reply here if you have any questions.

Deanne [DEANNE LAST NAME]  
On behalf of Hansel Dobbs, MNAA, CDEI | ValuSignal 2026

---

---

## SEQUENCE 2 — Cold Pipedrive Leads (~870 contacts)

**Who they are:** In Pipedrive but have had zero contact with ValuSignal yet. Warm-up sequence — no hard sell.  
**Goal:** Introduce ValuSignal as a concept, establish the virtual-only value prop, earn enough trust that Email 2 lands with credibility. Registration CTA comes in Email 2, softly.  
**Thread behavior:** Email 2 sends blank subject — lands in same thread as Email 1.  
**No promo code in this sequence** — these contacts need introduction first.

---

### Email 1 — Day 0

**Subject:** `{{first_name}}, not sure if you've heard of this`

{{first_name}},

There's a conference built specifically for residential appraisers this September — ValuSignal 2026, September 18–19.

What makes it different: it's 100% virtual. No flights, no hotels, no days lost away from your desk. The cost to attend is less than a single hotel night at a typical appraisal conference — and you keep the content for three months on-demand after the event.

70+ sessions covering UAD 3.6 readiness, AI workflows, revenue diversification, and where the profession is headed.

Worth knowing about?

Deanne [DEANNE LAST NAME]  
On behalf of Hansel Dobbs, MNAA, CDEI | ValuSignal 2026

---

### Email 2 — Day 5 (blank subject — threads under Email 1)

*[Leave subject line blank in your sending tool so it threads as a reply]*

{{first_name}},

Wanted to add one thing to my last note.

The speaker lineup includes Kelly Davids (President, The Appraisal Foundation), Lisa Desmarais (VP of Appraisal Issues, 30+ years), Malinda Griffin (President, National Association of Appraisers), and Tony Pistilli (Restb.ai, 30+ years in real estate valuation).

This is the kind of conversation that happens at the national level — UAD 3.6, AI in practice, collateral modernization, where the GSEs are heading — but delivered virtually so you don't have to book a flight to be in the room.

If it sounds relevant, the full lineup and registration are at valusignal.com/register.

Deanne [DEANNE LAST NAME]  
On behalf of Hansel Dobbs, MNAA, CDEI | ValuSignal 2026

---

---

## Notes for deployment

**Sequence 1 (warm leads)**
- Pull the ~200 list from Instantly — filter for anyone who replied to Campaign 1 or 2 and has not yet registered
- Create the promo code in your registration/Stripe setup before sending
- Set "reply-to" to Hansel's email so any replies route back to him
- Send from Deanne + Eunice inboxes (personal Gmail / Outlook — not Instantly, not a mass-send tool)
- Email 2 goes out only if no reply to Email 1 within 5 days

**Sequence 2 (cold Pipedrive)**
- Pull the ~870 from Pipedrive — exclude anyone already in the Instantly warm list
- Can run from Deanne/Eunice inboxes or a low-volume tool (avoid Instantly for these since Instantly already runs as Hansel — two senders from the same brand helps avoid domain fatigue)
- Email 2 goes out only if no reply to Email 1 within 5 days
- If anyone replies to either email, move them manually to the warm sequence with a personal response before sending the promo code
