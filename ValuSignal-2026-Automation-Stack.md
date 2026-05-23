# ValuSignal 2026 — Automation Stack Ingestion
*Last updated: 2026-05-23*

---

## 1. MAKE.COM BLUEPRINTS (3 production scenarios)

### Blueprint A: Stripe + Instantly
**Purpose:** When a Stripe payment fires, mark that lead as "Registered" in the Instantly campaign tracking sheet.

**Flow:**
1. `stripe:watchEvents` → webhook #2351281 (listens for charge events)
2. `google-sheets:filterRows` → searches "Instantly Campaign Performance Tracking" (Sheet ID: `1AskVEt1gtsPqjAYsQ299MlYZirEoydyYE42NZa-4pME`) for row where column B = `receipt_email`
3. `google-sheets:updateRow` → sets column E ("Registration / Meeting Status") = `"Registered"`

**Key insight:** This is the bridge between Stripe purchases and Instantly outreach tracking — keeps the campaign sheet in sync so already-converted leads don't keep receiving cold outreach.

---

### Blueprint B: Checkout – Create Session (Production)
**Purpose:** Accepts a webhook from the Webflow registration form and creates a Stripe Checkout session, returning the URL.

**Webhook:** `create_checkout_session` (hook #2050066) — receives: `email`, `firstName`, `lastName`, `phone`, `company`, `position`, `ticket.name`, `ticket.quantity`, `product_type`, `referral`, `rewardful_referral`

**Price ID Map (set via Switcher on `ticket.name`):**
| Ticket Name | Price ID | Type |
|---|---|---|
| Appraiser Track EB | price_1TI5DTGV9wmT3Cuaaj1FqyKs | ticket |
| Career Launchpad EB | price_1TI53fGV9wmT3CuagpfUMwoJ | ticket |
| Agent Pricing Lab EB | price_1TI5E5GV9wmT3CuaRFNkdFO9 | ticket ⚠️ APL eliminated |
| Appraiser Track | price_1T4J84GV9wmT3CuaWlv5sEzM | ticket |
| Career Launchpad | price_1T4J8aGV9wmT3CuaQNFJO9sO | ticket |
| Agent Pricing Lab | price_1T4J9CGV9wmT3CuadEZA3gJj | ticket ⚠️ APL eliminated |
| Featured Sponsorship | price_1TBGqBGV9wmT3CuauuYZBKEJ | sponsorship |
| Title Sponsorship | price_1TBGqUGV9wmT3CuavRnyWv5j | sponsorship |
| Core Sponsorship | price_1TBGpsGV9wmT3CuaRDsvGl6H | sponsorship |

**Branch logic:**
- Branch A (no `rewardful_referral`): POST to `https://api.stripe.com/v1/checkout/sessions` → respond `{url, rewardful_referral: "n/a"}`
- Branch B (has `rewardful_referral`): Same but sets `client_reference_id` = referral token → respond `{url, rewardful_referral}`

**URLs:**
- Success: `https://www.valusignal.com/thank-you?email={{email}}&type={{product_type}}`
- Cancel: `https://www.valusignal.com/register`

**⚠️ Action needed:** APL price IDs still in blueprint — need to be removed since APL was eliminated Apr 21.

---

### Blueprint C: Stripe – Payment Success – Handler (Production)
**Purpose:** Full post-purchase workflow. Fires on every successful Stripe checkout. Creates deal in Pipedrive, creates person if new, sends confirmation email, triggers DocuSign for sponsors.

**Webhook:** `Stripe + Make New` (hook #2050101)

**Variables extracted from Stripe session:**
- `order_email`, `order_first_name`, `order_last_name`, `order_full_name`
- `order_phone`, `order_company`, `order_position`
- `order_ticket_type`, `order_ticket_price_id`, `order_quantity`
- `order_amount_total` (in cents → divided by 100 for Pipedrive deal value)
- `order_currency`, `order_stripe_session_id`, `order_payment_intent`, `order_timestamp`, `price_id`

**Switcher:** classifies `price_id` → `"ticket"` or `"sponsorship"`

**Router — TICKET PATH:**
- Person exists in Pipedrive → `createDeal` (title: `{ticket_type} - {full_name}`, value: amount) → send confirmation email: *"🎟️ Your ValuSignal ticket is confirmed!"*
- New person → `CreatePerson` → `createDeal` → send confirmation email

**Router — SPONSORSHIP PATH:**
- Person exists → `createDeal` → nested router by tier:
  - Core → DocuSign template + confirmation email
  - Featured → DocuSign template + confirmation email
  - Title → DocuSign template + confirmation email
- New person → `CreatePerson` → `createDeal` → same DocuSign+email routing

**Auth:** ValuSignal Stripe Secret Key - Production (keychain #132552), Pipedrive connection #7991174

---

## 2. WEB FORMS (Pipedrive) — 8 Active

| Form | Views | Submitted | Conv% | Owner |
|---|---|---|---|---|
| (01) General Contact / Inquiry | 81 | 16 | **19.8%** | Eunice |
| (02) Rebuild Your Appraiser Website | 236 | 8 | 3.4% | Eunice |
| (03) Get the UAD 3.6 Survival Guide | 104 | 14 | **13.5%** | Eunice |
| (04) Stay Updated / Get Schedule | 2,368 | 53 | 2.2% | Rohit |
| (05) Sponsor Inquiry | 222 | 7 | 3.2% | Eunice |
| (06) Tech - More Platforms | 204 | 6 | 2.9% | Eunice |
| (07) Replace your $400-a-year appraiser | 26 | 3 | **11.5%** | Rohit |
| Session Updates | 411 | 5 | 1.2% | Rohit |

**Archived:** (01) Landing Page Leads, (07) Registration Opening Soon

**Total ~1,000 contacts in Pipedrive** across all form submissions + outreach.

---

## 3. EMAIL SEQUENCES (Pipedrive Automated Campaigns)

### Sequence A — General Contact / Inquiry
*Triggers from: Form 01, Session Updates*

| Step | Subject | Content |
|---|---|---|
| 1 | We Have Received Your Message | Ack + early bird banner (ends June 1) + 3 sessions (Roy Meyer, Patricia Staebler, Lisa Gulden) + pricing $197/$47 |
| 2 | Here Is Where ValuSignal Is Most Useful | Audience fit: valuation fields, evolving workflows, practical applications |
| 3 | Just Following Up on Your Message | New sessions: Tony Pistilli (Computer Vision), Tobias Peter (Housing Market) |
| 4 | The Program Is Coming Into Focus | 3 confirmed sessions (Joshua Walitt, Tobias Peter, Michele Golden) + Buy CTA |
| 5 | New Sessions and Speakers Have Just Been Added | Program update + early bird |
| 6 | What Kind of Event Is This, Really? | 3 focus areas (Practical Application, What's Changing, Business Direction) + Roy Meyer featured |

### Sequence B — Sponsor Inquiry
*Triggers from: Form 05*

| Step | Subject | Content |
|---|---|---|
| 1 | Thank You for Your Interest in Sponsoring ValuSignal | Ack + why sponsor + Book a Call with Eunice CTA |
| 2 | Most Sponsorships Look Similar on Paper | 4 differentiators: Direct Access, Context, Measurable Interaction, Ongoing Presence |
| 3 | Most Product Demos Follow a Familiar Pattern | 3 structured areas: Real Workflow Context, UAD 3.6 Readiness, Decision-Relevant Clarity |
| 4 | The Most Effective Demos Are Not the Most Polished | 4-step framework for demos |
| 5 | Is This the Right Audience for Us? | Audience: Appraisers, Review/QC, Valuation Leaders, Analysts |
| 6 | Does This Make Sense for Us? | Fit criteria + not-a-fit criteria |
| 7 | We Are Finalizing the Tech Demo Lineup | Urgency + Confirm Your Spot / Book a Call |
| 8 | "Is This the Right Audience for Us?" (follow-up variant) | Audience defined by intent not just role |

### Sequence C — UAD 3.6 Survival Guide
*Triggers from: Form 03*

| Step | Subject | Content |
|---|---|---|
| 1 | UAD 3.6 Is Not About Learning Something New | 3 shifting areas: Data Consistency, Adjustment Support, Report Structure + Download Guide CTA |
| 2 | The Presentation Problem Most Appraisers Don't See Coming | 3 review issues: Adjustment Support, Commentary Alignment, Extra Interpretation |
| 3 | What Should Change in Your Workflow? | Data Alignment + Clear Support + Learn More at ValuSignal |
| 4 | This Event Isn't Designed for Everyone | Audience fit / not-a-fit (CE credit seekers) |

### Sequence D — Tech Demo / Vendor Track
*Triggers from: Form 06 (Tech - More Platforms)*

| Step | Subject | Content |
|---|---|---|
| 1 | Most Product Demos Follow a Familiar Pattern | 3 evaluation areas |
| 2 | Who Will Actually Be in These Sessions? | 4 audience groups; actively deciding what to adopt |
| 3 | The Most Effective Demos Are Not the Most Polished | 4-step structure |
| 4 | We Are Finalizing the Tech Demo Lineup | Urgency + CTA |
| 5 | Most Sponsorships Look Similar on Paper | Engagement model |

---

## 4. LEAD MAGNETS

- **UAD 3.6 Survival Guide** — downloadable resource (Form 03 entry point)
- **Workflow Capacity Calculator** — https://workflow-capacity-calculator.lovable.app (Lovable-built tool)
- **UAD 3.6 Readiness Map** — interactive map at map.valusignal.com (referenced in all sequence footers)

---

## 5. CONTACTS & CONVERSION CONTEXT

- **~1,000 contacts in Pipedrive** — ingested from web forms + cold outreach campaigns
- **Instantly Campaign Tracking Sheet** (Google Sheets `1AskVEt1gtsPqjAYsQ299MlYZirEoydyYE42NZa-4pME`) tracks: Date, Lead, Outreach Status, Outreach Update Date, Registration/Meeting Status, Meeting Date, Campaign, Variant#
- **Early Bird deadline: June 1, 2026** — all sequences reference this urgency trigger
- **Event dates: September 18–19, 2026** — virtual

---

## 6. MEETING NOTES (6 months, Nov 2025 – May 2026)

Files located in: `~/Downloads/All meetings/`

**Subfolders:**
- `drive-download-20260523T155020Z-3-001/` — Team Meetings (Jan–May 2026), ValuSignal syncs, Website Launch, Rewardful meeting
- `drive-download-20260523T155025Z-3-001/` — Cold Email Campaign meetings (Apr 13 + May 18)
- `drive-download-20260523T155044Z-3-001/` — Eunice+Hansel, Eunice+Oleg, Patrick testing, Jeremy flow testing
- `drive-download-20260523T155051Z-3-001/` — Hansel+Bill (Apr 27), Hansel+Eunice (Apr 21), Louis catch-up
- `drive-download-20260523T155103Z-3-001/` — Agendas (Dec 2025 – May 2026, weekly)

**Key meetings to note:**
- `Team Meeting - 2026_05_19` — most recent (4 days ago)
- `Cold Email Campaign Weekly Meeting - 2026_05_18` — Instantly campaign status
- `Hansel + Bill (ValuSignal 2026) - 2026_04_27` — likely post-pivot strategy
- `Hansel + Eunice - 2026_04_21` — day of APL pivot decision

---

## 7. SCHEDULE FILE

Latest agenda: `~/Downloads/valusignal_schedule_2026-05-23.xlsx`

---

## 8. GAPS / ACTION ITEMS IDENTIFIED

1. **Blueprint B (Checkout):** APL price IDs still hardcoded — remove `Agent Pricing Lab EB` and `Agent Pricing Lab` entries since APL was eliminated Apr 21
2. **Form (04) Stay Updated** — highest volume (2,368 views, 53 submitted) but no dedicated nurture sequence mapped — opportunity to add one targeting the 2,315 views-but-didn't-submit
3. **Form (07) Replace $400/year appraiser** — 11.5% conversion but only 26 views — needs traffic
4. **Session Updates form** — 1.2% conversion, 411 views — weakest performer, may need form redesign
5. **1,000 Pipedrive contacts** — need segmentation strategy for conversion plan (see next steps)
