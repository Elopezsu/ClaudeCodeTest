const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, PageBreak } = require('docx');
const fs = require('fs');

function p(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 120 },
    ...opts,
    children: [new TextRun({ text, font: "Arial", size: 22, ...opts.run })]
  });
}

function emptyLine() {
  return new Paragraph({ children: [new TextRun({ text: "" })] });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 200 },
    children: [new TextRun({ text, bold: true, font: "Arial", size: 32 })]
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 300, after: 160 },
    children: [new TextRun({ text, bold: true, font: "Arial", size: 26 })]
  });
}

function label(text) {
  return new Paragraph({
    spacing: { after: 80 },
    children: [new TextRun({ text, bold: true, font: "Arial", size: 22 })]
  });
}

function divider() {
  return new Paragraph({
    spacing: { before: 200, after: 200 },
    children: [new TextRun({ text: "───────────────────────────────────────", font: "Arial", size: 20, color: "AAAAAA" })]
  });
}

function emailBlock(subject, lines) {
  const children = [];
  children.push(label("Subject: " + subject));
  children.push(emptyLine());
  for (const line of lines) {
    children.push(p(line));
  }
  return children;
}

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal",
        run: { size: 32, bold: true, color: "1a1a1a", font: "Arial" },
        paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal",
        run: { size: 26, bold: true, color: "444444", font: "Arial" },
        paragraph: { spacing: { before: 300, after: 160 }, outlineLevel: 1 } }
    ]
  },
  sections: [{
    properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children: [

      // TITLE
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 400 },
        children: [new TextRun({ text: "ValuSignal 2026 — Cold Email Sequence", bold: true, font: "Arial", size: 40 })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 600 },
        children: [new TextRun({ text: "18 emails · 3 variations each · Signed as Hansel / ValuSignal 2026", font: "Arial", size: 20, color: "777777" })]
      }),

      // ── EMAIL 1 ──
      h1("EMAIL 1 — Cold Outreach"),
      p("Rules: plain text only, no links, reply CTA, peer-to-peer tone.", { run: { italics: true, color: "666666" } }),
      emptyLine(),

      h2("Variation A"),
      ...emailBlock("Lock In 33% Off ValuSignal 2026 Before Prices Rise", [
        "ValuSignal 2026",
        "Built different.",
        "",
        "No vendor pitches. No panels where everyone agrees with each other.",
        "Just working appraisers sharing what's actually moving the needle right now.",
        "",
        "Reply to this email and I'll send you the full details.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation B"),
      ...emailBlock("Lock In 33% Off Your Appraiser Pass Before Early Bird Ends", [
        "ValuSignal 2026",
        "Your kind of conference.",
        "",
        "80+ hours of sessions built by appraisers, for appraisers.",
        "AI tools, new revenue lines, Expert Witness work — no fluff, no sales decks.",
        "",
        "Interested? Just reply.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation C"),
      ...emailBlock("Save 33% on ValuSignal 2026 — Early Bird Pricing Won't Last", [
        "ValuSignal 2026",
        "The conversation the industry needs.",
        "",
        "AI workshops, Expert Witness sessions, practice expansion — built around what appraisers are actually dealing with right now.",
        "",
        "Reply and I'll send you everything.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 1 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 1 — Early Bird Urgency"),
      p("Angle: $197 only until June 1, price goes up from there. Introduce 'Appraiser Track' by name.", { run: { italics: true, color: "666666" } }),
      emptyLine(),

      h2("Variation A"),
      ...emailBlock("Lock In $197 on ValuSignal 2026 Before Prices Rise", [
        "ValuSignal 2026",
        "Beat the deadline.",
        "",
        "When it's gone, it's gone. Lock in your early bird rate now.",
        "The Appraiser Track gets you every session, the Claude Code workshop, and 3 months of replays.",
        "",
        "$197 now. $247 on June 1. $297 on August 1.",
        "",
        "Register here: www.valusignal.com",
        "",
        "Expires June 1.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation B"),
      ...emailBlock("Save $100 on ValuSignal 2026 — Early Bird Closes June 1", [
        "ValuSignal 2026",
        "The clock is running.",
        "",
        "One of your last chances to lock in the early bird rate on the Appraiser Track.",
        "Full access — 80+ hours of sessions, Claude Code workshop, 3 months of replay.",
        "",
        "Early bird: $197. Jumps to $247 on June 1.",
        "",
        "Register here: www.valusignal.com",
        "",
        "Expires June 1.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation C"),
      ...emailBlock("$197 Locks Your Seat at ValuSignal 2026 — June 1 It Goes Up", [
        "ValuSignal 2026",
        "Don't wait on this one.",
        "",
        "Early bird closes June 1. After that the Appraiser Track is $247, then $297.",
        "Every session, the AI workshop, 3 months of replay — locked in at $197 while it lasts.",
        "",
        "www.valusignal.com",
        "",
        "Expires June 1.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 2 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 2 — AI Workshop"),
      p("Angle: First appraisal conference with a hands-on AI workshop, Claude Code + OpenAI, built for appraisers.", { run: { italics: true, color: "666666" } }),
      emptyLine(),

      h2("Variation A"),
      ...emailBlock("First Hands-On AI Workshop at an Appraisal Conference", [
        "ValuSignal 2026",
        "This one's new.",
        "",
        "No other appraisal conference has done this.",
        "A hands-on Claude Code and OpenAI workshop built specifically for how appraisers work. No tech background needed.",
        "",
        "See the full agenda: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation B"),
      ...emailBlock("Learn Claude Code at ValuSignal 2026 — Built for Appraisers", [
        "ValuSignal 2026",
        "AI, for appraisers.",
        "",
        "The industry's first hands-on AI workshop.",
        "Claude Code, OpenAI tools, real workflows — walk away ready to use them the next day.",
        "",
        "Details here: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation C"),
      ...emailBlock("The AI Workshop Appraisers Have Been Waiting For", [
        "ValuSignal 2026",
        "Finally.",
        "",
        "We built the AI workshop the industry has been missing.",
        "Claude Code, OpenAI — practical, hands-on, zero tech background required.",
        "",
        "Check it out: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 3 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 3 — Volume of Value"),
      p("Angle: 80+ hours, 50+ speakers, 3-month replay access, one registration covers it all.", { run: { italics: true, color: "666666" } }),
      emptyLine(),

      h2("Variation A"),
      ...emailBlock("80+ Hours of Appraisal Content for One Registration", [
        "ValuSignal 2026",
        "One pass. Everything.",
        "",
        "80+ hours of sessions. 50+ speakers. 3 months of on-demand replays.",
        "You don't have to attend live — pick the sessions that matter and come back to the rest.",
        "",
        "Register here: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation B"),
      ...emailBlock("50 Speakers. 80 Hours. 3 Months of Replay. ValuSignal 2026.", [
        "ValuSignal 2026",
        "The full picture.",
        "",
        "50+ appraisers on one stage. 80+ hours of content. Everything on-demand for 3 months.",
        "No filler. No one paid to be on stage.",
        "",
        "See who's speaking: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation C"),
      ...emailBlock("More Content Than Any Appraisal Conference — One Registration", [
        "ValuSignal 2026",
        "Here's what you're getting.",
        "",
        "80+ hours. 50+ vetted speakers. 3 months of replay access after the event.",
        "For what most in-person conferences charge for a single day.",
        "",
        "www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 4 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 4 — New Revenue Lines"),
      p("Angle: Expert Witness positioning + practice expansion, ways to grow beyond the AMC model.", { run: { italics: true, color: "666666" } }),
      emptyLine(),

      h2("Variation A"),
      ...emailBlock("Two Ways Appraisers Are Growing Beyond the AMC Model", [
        "ValuSignal 2026",
        "New revenue, same license.",
        "",
        "Expert Witness work and practice expansion — two full sessions at ValuSignal 2026.",
        "Real appraisers sharing how they made the shift.",
        "",
        "See the sessions: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation B"),
      ...emailBlock("Get Off the AMC Treadmill — Expert Witness Sessions at ValuSignal 2026", [
        "ValuSignal 2026",
        "Time to diversify.",
        "",
        "The volume isn't sustainable and the fees aren't moving.",
        "ValuSignal 2026 has full sessions on Expert Witness positioning, litigation support, and adjacent practice areas that leverage your license.",
        "",
        "Worth a look: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation C"),
      ...emailBlock("Curious About Expert Witness Work? ValuSignal 2026 Has a Full Session on It.", [
        "ValuSignal 2026",
        "Beyond the appraisal order.",
        "",
        "How to get started, what attorneys look for, how to price it — all covered.",
        "Real appraisers who made the shift sharing what actually worked.",
        "",
        "www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 5 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 5 — Final Close"),
      p("Angle: Last email, reinforce Appraiser Track value, June 1 deadline, graceful exit.", { run: { italics: true, color: "666666" } }),
      emptyLine(),

      h2("Variation A"),
      ...emailBlock("Last Chance to Lock In $197 on ValuSignal 2026 Before Prices Rise", [
        "ValuSignal 2026",
        "Final call.",
        "",
        "This is the last email I'll send on this.",
        "The Appraiser Track is $197 until June 1 — every session, the Claude Code workshop, 3 months of replays.",
        "",
        "After June 1 it's $247. It won't come back down.",
        "",
        "www.valusignal.com",
        "",
        "Expires June 1.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation B"),
      ...emailBlock("Closing the Loop — ValuSignal 2026 Early Bird Ends June 1", [
        "ValuSignal 2026",
        "One last thing.",
        "",
        "The Appraiser Track covers everything — AI workshop, Expert Witness sessions, 80+ hours, 3-month replay.",
        "$197 until June 1. $247 after. If you have a question before registering, just reply.",
        "",
        "www.valusignal.com",
        "",
        "Expires June 1.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation C"),
      ...emailBlock("Before I Leave You Alone — ValuSignal 2026 Early Bird Closes June 1", [
        "ValuSignal 2026",
        "Last one, I promise.",
        "",
        "Every session, the Claude Code workshop, Expert Witness content, 3 months of replays — $197 until June 1, then $247.",
        "If something's holding you back, reply and tell me what it is.",
        "",
        "www.valusignal.com",
        "",
        "Expires June 1.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("ValuSignal-2026-Cold-Email-Sequence.docx", buffer);
  console.log("Done: ValuSignal-2026-Cold-Email-Sequence.docx");
});
