# ValuSignal 2026 — Pipedrive Nurture Automation (Setup, Test & Go-Live)

**Status (2026-06-29):** Automation **rebuilt & structurally correct**, toggle still **OFF**, first-name merge field **fixed**. Remaining before launch: unsubscribe token swap, test, enroll. See **Open items** at the bottom.

**Goal:** Drip the 10-email inbound nurture, every 5 days, to **~943 People** (`people-25004685-8.csv` — all already **Subscribed** and carrying the **VS-NURTURE-2026** label), excluding "Website Speaker."

---

## Why the original automation failed
It was built on the **Lead** object (trigger "Lead added" + condition "Lead labels"). The audience is **People** with **Person labels** (Cold/Hot/Warm lead, Conference Partner). Different object → the trigger never fired and the labels never matched → **0 enrollments**. Fix = rebuild on the **Person** object.

## The correct automation ("Pipedrive leads") — as built
| Step | Type | Config |
|---|---|---|
| 1 | **Trigger** | **Person updated** (watching the Labels field) |
| 2 | Instant condition | **Labels is `VS-NURTURE-2026`** |
| 3 | Instant condition | **Marketing status is Subscribed** (gates out non-subscribed) |
| 4 | Action | Send campaign → E1 (Welcome) → To: Person |
| 5 | Delay | 5 days |
| 6–22 | Action/Delay | Send E2 → delay 5d → … → E10 (Close) |

Mapping: campaigns are titled "NEW – email 1 … 10" = nurture **E1 … E10**.

## Merge fields — IMPORTANT
Pipedrive Campaigns uses **Mailchimp-style `*|FIELD|*` tags, NOT `{{ }}`.** `{{first_name}}` is **not recognized**.
- ✅ **Fixed 2026-06-29:** all 10 nurture emails + both templates now use **`*|FIRST_NAME|*`** (committed/pushed).
- ⏳ **Pending:** `{{unsubscribe}}` (24 instances) still in the broken `{{ }}` format → swap to **`*|UNSUBSCRIBE|*`** (or delete inline and let Pipedrive auto-append its unsubscribe footer). **Required before sending.**

---

## How to ENROLL contacts who already have the label (the key gotcha)
Turning the automation ON does **NOT** back-enroll people who already match — automations only fire on trigger events that happen **while ON, going forward**. The 943 got their label while it was OFF, so those events are gone.

**To enroll the existing 943:**
1. **Turn the automation ON first.**
2. Filter the 943 (Label = VS-NURTURE-2026).
3. **Bulk-remove** the VS-NURTURE-2026 label → then **bulk-add** it back.
   - The re-add is a fresh "Labels updated" event with the automation live → all 943 enroll at E1.
   - *Alternative:* bulk-add a throwaway label (e.g. `ENROLL-NOW`) to fire the update without stripping the real label; remove it after.
4. **Order matters:** ON first, then re-label. Re-labeling while OFF loses the events again.

For *future* leads, just add the VS-NURTURE-2026 label (with automation ON) and they enroll automatically.

---

## How to TEST (before blasting 943)
Best combo — tests every piece in under an hour with zero risk to the live automation:
1. **Clone** the automation (⋯ → Clone). Work on the copy.
2. On the copy, change every **"Delay 5 days" → "Delay 5 minutes."**
3. Make 2–3 test People using **Gmail `+alias`** (`you+test1@gmail.com`, `+test2`…) — they all land in your inbox but Pipedrive treats them as distinct. Make one **Subscribed** and one **not**, to confirm step 3 filters the unsubscribed one out.
4. Turn the **copy** ON → add the label to the test people → watch **all 10 emails arrive in ~45 min**.
5. Check the automation's **run history/log** — each step shows succeeded or failed/skipped.
6. Delete the copy. Then enroll the real 943 on the original (delays back at 5 days).

Independent of the automation, you can also use **Campaigns → Send test / Preview** on each E1–E10 to verify HTML rendering, `*|FIRST_NAME|*` population, links, and Mailmeteor spam score.

---

## ⏰ Timing watch-out — flash-sale email (E2)
E2 uses code **EARLYBIRD, expires July 4**, and lands ~5 days after enrollment.
- Enroll **June 29–30** → E2 ~July 4 (OK).
- Enroll **later** → E2 is stale → **remove E2** (or swap for a non-dated value email) before enrolling.

---

## ✅ Open items / go-live checklist
- [ ] Swap `{{unsubscribe}}` → `*|UNSUBSCRIBE|*` (or remove + use Pipedrive auto-footer) across all HTML.
- [ ] Re-paste the updated HTML (with `*|FIRST_NAME|*`) into campaigns E1–E10; run each through **Mailmeteor**.
- [ ] Confirm all 10 campaigns exist, are valid/sendable, and the chain ends cleanly at E10.
- [ ] Test via the clone + 5-min-delay + `+alias` method; check the run log.
- [ ] Check the Pipedrive plan's **daily Campaigns send limit** (943 at once is a big blast).
- [ ] Decide E2 timing vs July 4.
- [ ] **Turn automation ON**, then **remove + re-add** the label on the 943 to enroll them.

### Why this works where the old one didn't
Right **object** (Person, not Lead) · right **trigger** (Person updated via a label change) · one **enrollment label** as the "folder" · **Subscribed** gate so campaigns actually deliver.
