# ValuSignal 2026 — Hero Section Design Brief
**For:** Developer / Designer
**Prepared by:** Eunice Lopez, Operations
**Date:** May 27, 2026
**Page:** valusignal.com (Homepage Hero)

---

## Context

The homepage hero currently has three lines of plain small text stacked below the CTA buttons with no visual treatment:

```
Virtual • Non-CE • September 18th & 19th
Early bird pricing: $197 through June 15 — $297 after.
If the conference doesn't deliver, we'll refund your ticket.
```

These three pieces of information are **conversion-critical** and need proper design treatment. The goal is to make the early bird deadline and refund guarantee visible and compelling — not buried as footnotes.

---

## Site Design Reference

| Property | Value |
|----------|-------|
| Background | Dark teal/green |
| Primary CTA button | Coral `#E8634A` |
| Text | White |
| Style | Clean, minimal, professional |

---

## Option 1 — Urgency Badge Above the CTA Button

Place a styled coral pill badge **above** the Register button. The refund guarantee stays below the buttons as a small trust line with a checkmark icon.

```
┌─────────────────────────────────────────────────────────────────┐
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  VALUSIGNAL CONFERENCE 2026                                      │
│                                                                  │
│  Where Valuation                                                 │
│  Does Business.                                                  │
│                                                                  │
│  Real-world workflows. AI adoption playbooks.                   │
│  New revenue strategies. UAD 3.6 navigation.                    │
│                                                                  │
│  ╔══════════════════════════════════════╗                        │
│  ║  🔥 Early bird ends June 15 · $197  ║  ← coral pill badge    │
│  ╚══════════════════════════════════════╝                        │
│                                                                  │
│  [ Register for 2026 ]   [ Explore Tracks ↓ ]                   │
│                                                                  │
│  Virtual · Non-CE · September 18–19                             │
│  ✓ If the conference doesn't deliver, we'll refund your ticket. │
└─────────────────────────────────────────────────────────────────┘
```

**Implementation notes:**
- Badge background: coral `#E8634A`, white text, rounded pill (`border-radius: 999px`), padding `6px 16px`
- Badge copy: `🔥 Early bird ends June 15 · $197`
- Refund line: white text, 80% opacity, small font size (`0.85rem`), `✓` icon before the text
- Add `margin-bottom: 12px` between badge and buttons
- Add `margin-top: 12px` between buttons and trust line

---

## Option 2 — Pricing Callout Card Between Subheadline and Buttons

Insert a two-column card between the subheadline and the CTA buttons. Left column shows the price with a strikethrough. Right column shows the refund guarantee.

```
┌─────────────────────────────────────────────────────────────────┐
│  VALUSIGNAL CONFERENCE 2026                                      │
│                                                                  │
│  Where Valuation                                                 │
│  Does Business.                                                  │
│                                                                  │
│  Real-world workflows. AI adoption playbooks.                   │
│  New revenue strategies. UAD 3.6 navigation.                    │
│                                                                  │
│  ┌──────────────────────┬─────────────────────────────┐         │
│  │  $197  Early Bird    │  🛡 Refund guaranteed        │         │
│  │  ~~$297~~ after      │  If it doesn't deliver,     │         │
│  │  June 15             │  we'll refund your ticket.  │         │
│  └──────────────────────┴─────────────────────────────┘         │
│                                                                  │
│  [ Register for 2026 ]   [ Explore Tracks ↓ ]                   │
│                                                                  │
│  Virtual · Non-CE · September 18–19                             │
└─────────────────────────────────────────────────────────────────┘
```

**Implementation notes:**
- Card background: `rgba(255,255,255,0.07)` (subtle light overlay on teal), `border-radius: 8px`, padding `16px 24px`
- Left column: `$197` in coral `#E8634A`, large bold. `~~$297~~` in white, 50% opacity, `text-decoration: line-through`. "after June 15" in white, small.
- Right column: 🛡 icon in soft green, refund text in white, `0.9rem`
- Add a `1px solid rgba(255,255,255,0.15)` divider between columns

---

## Option 3 — Sticky Urgency Bar at Top of Page (Site-Wide)

Add a thin sticky announcement bar **above the navigation** that appears on every page. This catches visitors who land on Speakers, Schedule, or any other page — not just the homepage.

```
┌─────────────────────────────────────────────────────────────────┐
│ 🔥  Early bird pricing ends June 15 — Register now for $197     │
│     ────────────────── saves you $100 ──────────────────        │
├─────────────────────────────────────────────────────────────────┤
│  [Logo]  Tracks  Schedule  Speakers  Tech  Sponsors  [Register] │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Where Valuation                                                 │
│  Does Business.                                                  │
│                                                                  │
│  Real-world workflows. AI adoption playbooks.                   │
│  New revenue strategies. UAD 3.6 navigation.                    │
│                                                                  │
│  [ Register for 2026 ]   [ Explore Tracks ↓ ]                   │
│                                                                  │
│  ✓ If the conference doesn't deliver, we'll refund your ticket. │
└─────────────────────────────────────────────────────────────────┘
```

**Implementation notes:**
- Bar background: coral `#E8634A`, white text, centered, `height: 40px`, `position: sticky; top: 0; z-index: 100`
- Copy: `🔥 Early bird pricing ends June 15 — Register now for $197 · Saves $100`
- Optional: wire a live countdown (`19 days left`) if feasible before June 15
- Bar should be dismissible (✕ close button on the right) but default to visible
- Remove the bar after June 15 — do not leave dead urgency copy on the site

---

## Recommended Combination

Use **Option 3 + Option 1** together:

1. **Sticky bar (Option 3)** — site-wide urgency, visible on every page
2. **Badge above button (Option 1)** — hero-specific push at the exact decision point
3. **Refund trust line** — below the buttons with a ✓ icon, properly spaced

This gives three visible touchpoints without cluttering the hero. The dark teal background makes coral badges and white trust lines pop cleanly.

---

## Copy Reference (Final)

| Element | Copy |
|---------|------|
| Urgency badge | `🔥 Early bird ends June 15 · $197` |
| Sticky bar | `🔥 Early bird pricing ends June 15 — Register now for $197 · Saves $100` |
| Price callout | `$197 Early Bird` / `~~$297~~ after June 15` |
| Refund guarantee | `✓ If the conference doesn't deliver, we'll refund your ticket.` |
| Refund badge | `🛡 Refund guaranteed` |

---

*Related file: `ValuSignal-Website-Updates-Checklist.md` — full list of pending site fixes*
