const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, PageBreak } = require('docx');
const fs = require('fs');

function p(text, opts = {}) {
  return new Paragraph({
    spacing: { after: 140 },
    children: [new TextRun({ text, font: "Arial", size: 22, ...opts.run })]
  });
}

function empty() {
  return new Paragraph({ spacing: { after: 80 }, children: [new TextRun({ text: "" })] });
}

function h1(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 200 },
    children: [new TextRun({ text, bold: true, font: "Arial", size: 34 })]
  });
}

function h2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 280, after: 140 },
    children: [new TextRun({ text, bold: true, font: "Arial", size: 26 })]
  });
}

function subject(text) {
  return new Paragraph({
    spacing: { after: 100 },
    children: [
      new TextRun({ text: "Subject: ", bold: true, font: "Arial", size: 22 }),
      new TextRun({ text, font: "Arial", size: 22 })
    ]
  });
}

function divider() {
  return new Paragraph({
    spacing: { before: 180, after: 180 },
    children: [new TextRun({ text: "────────────────────────────────────", font: "Arial", size: 18, color: "CCCCCC" })]
  });
}

function email(subjectText, lines) {
  const out = [];
  out.push(subject(subjectText));
  out.push(empty());
  for (const line of lines) {
    out.push(line === "" ? empty() : p(line));
  }
  return out;
}

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal",
        run: { size: 34, bold: true, color: "111111", font: "Arial" },
        paragraph: { spacing: { before: 400, after: 200 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal",
        run: { size: 26, bold: true, color: "444444", font: "Arial" },
        paragraph: { spacing: { before: 280, after: 140 }, outlineLevel: 1 } }
    ]
  },
  sections: [{
    properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children: [

      // TITLE
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { before: 0, after: 200 },
        children: [new TextRun({ text: "ValuSignal 2026", bold: true, font: "Arial", size: 44 })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 160 },
        children: [new TextRun({ text: "Cold Email Sequence — Final", bold: true, font: "Arial", size: 30 })]
      }),
      new Paragraph({
        alignment: AlignmentType.CENTER,
        spacing: { after: 600 },
        children: [new TextRun({ text: "6 emails · 3 variations each · Signed as Hansel / ValuSignal 2026", font: "Arial", size: 20, color: "888888" })]
      }),

      // ── EMAIL 1 ──
      h1("EMAIL 1 — Cold Outreach"),

      h2("Variation A"),
      ...email("Lock In 33% Off ValuSignal 2026 Before Prices Rise", [
        "No vendor pitches. No panels where everyone agrees with each other.",
        "Just working appraisers sharing what's actually moving the needle right now.",
        "",
        "Early bird is $197, reply and I'll send you everything before prices go up.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation B"),
      ...email("Lock In 33% Off Your Appraiser Pass Before Early Bird Ends", [
        "80+ hours of sessions built by appraisers, for appraisers.",
        "AI tools, new revenue lines, Expert Witness work, no fluff, no sales decks.",
        "",
        "Early bird is $197, ends June 1. Interested? Just reply.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation C"),
      ...email("Save 33% on ValuSignal 2026 — Early Bird Pricing Won't Last", [
        "AI workshops, Expert Witness sessions, practice expansion, built around what appraisers are actually dealing with right now.",
        "",
        "Early bird is $197, ends June 1. Reply and I'll send you the details.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 1 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 1 — Early Bird Urgency"),

      h2("Variation A"),
      ...email("Lock In $197 on ValuSignal 2026 Before Prices Rise", [
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
      ...email("Save $100 on ValuSignal 2026 — Early Bird Closes June 1", [
        "ValuSignal 2026",
        "June 1 is the cutoff.",
        "",
        "Lock in the Appraiser Track at $197 before it jumps to $247.",
        "Full access, 80+ hours of sessions, Claude Code workshop, 3 months of replay.",
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
      ...email("$197 Locks Your Seat at ValuSignal 2026 — June 1 It Goes Up", [
        "ValuSignal 2026",
        "June 1 it changes.",
        "",
        "Early bird closes June 1. After that the Appraiser Track is $247, then $297.",
        "Every session, the AI workshop, 3 months of replay, locked in at $197 while it lasts.",
        "",
        "Register here: www.valusignal.com",
        "",
        "Expires June 1.",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 2 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 2 — AI Workshop"),

      h2("Variation A"),
      ...email("First Hands-On AI Workshop at an Appraisal Conference", [
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
      ...email("Learn Claude Code at ValuSignal 2026 — Built for Appraisers", [
        "ValuSignal 2026",
        "AI, for appraisers.",
        "",
        "The industry's first hands-on AI workshop.",
        "Claude Code, OpenAI tools, real workflows, walk away ready to use them the next day.",
        "",
        "See the workshop: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation C"),
      ...email("The AI Workshop Appraisers Have Been Waiting For", [
        "ValuSignal 2026",
        "Finally.",
        "",
        "The first hands-on AI workshop built for appraisers.",
        "Claude Code, OpenAI, practical, zero tech background required. Walk away using it the next day.",
        "",
        "See the workshop: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 3 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 3 — Volume of Value"),

      h2("Variation A"),
      ...email("80+ Hours of Appraisal Content for One Registration", [
        "ValuSignal 2026",
        "One pass. Everything.",
        "",
        "80+ hours of sessions. 50+ speakers. 3 months of on-demand replays.",
        "You don't have to attend live, pick the sessions that matter and come back to the rest.",
        "",
        "Register here: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation B"),
      ...email("50 Speakers. 80 Hours. 3 Months of Replay. ValuSignal 2026.", [
        "ValuSignal 2026",
        "Here's the full scope.",
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
      ...email("80+ Hours of Content. One Registration. ValuSignal 2026.", [
        "ValuSignal 2026",
        "Here's what you're getting.",
        "",
        "80+ hours. 50+ vetted speakers. 3 months of replay access after the event.",
        "For what most in-person conferences charge for a single day.",
        "",
        "Register here: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 4 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 4 — New Revenue Lines"),

      h2("Variation A"),
      ...email("Two Ways Appraisers Are Growing Beyond the AMC Model", [
        "ValuSignal 2026",
        "New revenue, same license.",
        "",
        "Expert Witness work and practice expansion, two full sessions at ValuSignal 2026.",
        "Real appraisers sharing how they made the shift.",
        "",
        "See the sessions: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation B"),
      ...email("Get Off the AMC Treadmill — Expert Witness Sessions at ValuSignal 2026", [
        "ValuSignal 2026",
        "The fees aren't moving.",
        "",
        "The volume isn't sustainable and the AMC model isn't going to fix itself.",
        "ValuSignal 2026 has full sessions on Expert Witness work, litigation support, and practice areas that use your license differently.",
        "",
        "See the sessions: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),
      divider(),

      h2("Variation C"),
      ...email("Curious About Expert Witness Work? ValuSignal 2026 Has a Full Session on It.", [
        "ValuSignal 2026",
        "Beyond the appraisal order.",
        "",
        "How to get started, what attorneys look for, how to price it, all covered.",
        "Real appraisers who made the shift sharing what actually worked.",
        "",
        "See the session: www.valusignal.com",
        "",
        "Hansel",
        "ValuSignal 2026"
      ]),

      // ── FOLLOW-UP 5 ──
      new Paragraph({ children: [new PageBreak()] }),
      h1("FOLLOW-UP 5 — Final Close"),

      h2("Variation A"),
      ...email("Last Chance to Lock In $197 on ValuSignal 2026 Before Prices Rise", [
        "ValuSignal 2026",
        "Final call.",
        "",
        "This is the last email I'll send on this.",
        "The Appraiser Track is $197 until June 1, every session, the Claude Code workshop, 3 months of replays.",
        "",
        "After June 1 it's $247. It won't come back down.",
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
      ...email("Last Call — ValuSignal 2026 Early Bird Ends June 1", [
        "ValuSignal 2026",
        "One last thing.",
        "",
        "The Appraiser Track is $197 until June 1, then $247. Every session, the Claude Code workshop, Expert Witness content, 3 months of replay.",
        "It won't come back down.",
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
      ...email("Before I Leave You Alone — ValuSignal 2026 Early Bird Closes June 1", [
        "ValuSignal 2026",
        "Last one, I promise.",
        "",
        "Every session, the Claude Code workshop, Expert Witness content, 3 months of replays, $197 until June 1, then $247.",
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
  fs.writeFileSync("ValuSignal-2026-Final-Emails.docx", buffer);
  console.log("Done: ValuSignal-2026-Final-Emails.docx");
});
