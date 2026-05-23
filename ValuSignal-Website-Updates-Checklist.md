# ValuSignal 2026 — Website Updates Checklist
**For:** Dev / Website Manager
**Prepared by:** Eunice Lopez, Operations
**Date:** May 23, 2026
**Context:** Pre-June 15 early bird window. Items marked Critical need to be done before any new campaign traffic is sent to the site. Medium items improve conversion rate and should be done by June 1.

---

## CONFIRMED DONE ✅

These were verified via screenshots on May 23, 2026 — no action needed:

- ✅ Agent Pricing Lab removed from navigation, registration page, and ticket blocks
- ✅ Registration page is live with active Stripe checkout ("Go to Checkout" button)
- ✅ Early bird deadline correctly shows June 15 on the registration page
- ✅ Refund guarantee visible on registration page: "If the conference doesn't deliver, we'll refund your ticket."

---

## CRITICAL — Do This Week (Before New Campaigns Launch May 28)

### 1. Add early bird urgency to the homepage
**Where:** Near the primary "Register for 2026" CTA button on the homepage hero or directly below it
**What to add:** One line — *"Early bird pricing: $197 through June 15 — $297 after."*
**Why:** The homepage currently has a countdown timer to the event (September 18–19) but no price urgency. A lead who visits the homepage and does not click through to /register never sees that the window closes June 15.

---

### 2. Remove APL price IDs from Make.com Blueprint B (Checkout – Create Session)
**Where:** Make.com → Scenarios → "Checkout – Create Session (Production)" → Switcher module
**What to remove:** Two entries in the Switcher:
  - Ticket name "Agent Pricing Lab EB" → price ID `price_1TI5E5GV9wmT3CuaRFNkdFO9`
  - Ticket name "Agent Pricing Lab" → price ID `price_1T4J9CGV9wmT3CuadEZA3gJj`
**Why:** APL was eliminated April 21. These price IDs are orphaned — if a stale link or old email triggers an APL checkout attempt, it could create a confusing or failed transaction.

---

## MEDIUM — Do by June 1 (Improves Conversion Rate)

### 3. Add social proof to the homepage hero section
**Where:** In or directly below the hero headline ("Where Valuation Does Business.") — before the first scroll
**What to add:** 2–3 credibility lines. Suggested copy:
*"Speakers include Malinda Griffin (President, National Association of Appraisers), Michelle Czekalski Bradley (Past Chair, Appraisal Standards Board), and Joshua Walitt — among 70+ confirmed valuation professionals."*
**Why:** The speaker carousel is lower on the page. Appraisers evaluating whether to spend $197 need a credibility signal before they scroll, not after.

---

### 4. Move refund guarantee to homepage near pricing CTA
**Where:** Directly below or near the "Register for 2026" button on the homepage (same placement as on the /register page)
**What to add:** Existing text from the registration page: *"If the conference doesn't deliver, we'll refund your ticket."*
**Why:** This copy removes the biggest purchase objection. Right now it only appears after the buyer has already decided to click Register — it should appear at the decision point, not after.

---

### 5. Update "Subscribe for updates" copy on the Schedule page
**Where:** The schedule section module with the subscribe field
**What to change:** Replace "Subscribe for updates" / "The schedule is being built" framing with:
*"Full schedule releasing [specific date]. Subscribe to be notified when it drops."*
**Why:** "Being built" signals to a potential buyer that the product is incomplete. "Releasing on [date]" signals it's intentional and coming. Same form, different buyer perception.

---

## SUGGESTED — After June 15

These do not block conversion before June 15 but improve the site for the post-deadline window.

### 6. Add a post-deadline pricing update
After June 15, update the registration page early bird banner from "Early bird price — increases June 15" to reflect the new $297 price clearly. Avoid leaving dead "early bird" language on a page where early bird no longer exists.

### 7. Verify all lead magnet URLs are live
Before they are promoted in email campaigns and social posts, confirm these all load correctly:
  - `valusignal.com/website-lesson` (25-min video for Campaign 2)
  - `map.valusignal.com` (UAD 3.6 Readiness Map)
  - `workflow-capacity-calculator.lovable.app` (Workflow Capacity Calculator)
  - UAD 3.6 Survival Guide download link (from Form 03 confirmation)

### 8. Audit the /schedule page for APL session references
The schedule page may still show a session titled "Pricing for Agents: A Repeatable System (Workshop)" from the original APL track. Confirm whether this session has been kept, moved to another track, or removed. If it is kept under a different track, it should be labeled accordingly — not appear as an orphaned session without a track.

---

## Summary

| # | Item | Priority | Target Date |
|---|---|---|---|
| 1 | Add early bird urgency line to homepage | 🔴 Critical | May 26 |
| 2 | Remove APL price IDs from Make.com Blueprint B | 🔴 Critical | May 27 |
| 3 | Add social proof to hero section | 🟡 Medium | June 1 |
| 4 | Move refund guarantee to homepage | 🟡 Medium | June 1 |
| 5 | Update schedule page "subscribe" copy | 🟡 Medium | June 1 |
| 6 | Post-deadline pricing update | 🟢 Suggested | June 16 |
| 7 | Verify all lead magnet URLs | 🟢 Suggested | May 30 |
| 8 | Audit /schedule for APL session | 🟢 Suggested | June 1 |

---

*Reference document: `ValuSignal-Conversion-Audit-May2026.md` — full audit context.*
