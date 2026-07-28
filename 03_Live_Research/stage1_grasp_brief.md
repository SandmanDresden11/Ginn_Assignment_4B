# Stage 1 GRASP Brief — Live Research & Evidence Scoring

**Stage:** Query-plan approval → live web search → source scoring → audit (this document covers the live-research + audit portion of Stage 1, run after the meeting-signal inventory and query plan were already approved).

## Goal

Turn the approved query plan into a scored, decision-relevant evidence base — one file per meeting, each source tied to a specific fact or question from that meeting's notes, scored 0–3 for relevance, and flagged for human review where it touches pricing, security, legal/regulatory, or a major competitive claim. The goal is *not* to write the business-development memos yet; it's to produce a defensible, source-backed research layer that a later stage (or Claude Code) can draft from without re-doing the search work.

## Resources

Two distinct kinds of input, with different reliability profiles:

- **The eight meeting-notes files** (`01_Northstar_Advisory_Discovery.docx` through `08_Finley_Growth_Capital_Portfolio.docx`) — static, fixed, invented-for-the-exercise documents. Everything about the prospects, budgets, and quotes comes only from these; nothing here changes between runs.
- **Live web search** — this is the load-bearing dependency for this stage, and it's fundamentally different from the meeting notes: it is not a fed or pre-loaded document set. Every claim in the evidence files came from a real-time search run on 2026-07-28, against whatever the web currently returns. That means the evidence base has a shelf life — HubSpot's own pricing pages, partner-program terms, and AI-agent pricing all had recent or imminent change dates baked into what came back today. A re-run next month would likely surface different numbers, not just updated ones.

## Autonomy limits

Being specific about where judgment was mine versus where I was steered:

**Decided independently (Claude's judgment):**
- Which of the returned search results counted as a genuine "candidate source" versus noise, and which of those were redundant with each other (documented in `rejected_results.md`).
- The relevance score (0–3) assigned to each source, and the specific wording connecting a source back to a named person's question or concern in the meeting notes.
- How to categorize each source's human-review flag (pricing / security / legal-regulatory / major competitive claim / none) — including catching and correcting one mis-flag during the audit.
- Which sources were "directional but unverified" versus solid enough to count toward the two-source minimum per meeting.

**Set or steered by the user:**
- The initial keyword choices for every query — these came from the query plan you approved before any searching started (e.g., "Salesforce Agentforce prospecting and account-research capabilities 2026," not a keyword I generated fresh at search time).
- The folder structure, file-naming convention, and the specific fields required in each evidence entry.
- The explicit instruction to stop before drafting final memos, and the requirement that certain claim categories (pricing, security, legal/regulatory, competitive) get flagged rather than asserted.

The honest tension here: I chose *which* results were relevant once the search ran, but you chose *what to search for*. A different, equally reasonable set of keywords could have surfaced a different evidence base — the query plan is doing more steering than it might look like from the results alone.

## Sign-off point

This stage's output is not self-approving. Two things gate progress to Stage 2:

- Every meeting must show at least two score-3 sources, or an explicit "insufficient decision-relevant evidence" note with a suggested query refinement — this is checked mechanically, not left to judgment.
- Every source flagged pricing / security / legal-regulatory / major-competitive-claim needs a human to actually look at it before its claim appears in memo language — the flag is a routing instruction to a person, not a completed review.

Handoff to Claude Code (or to memo drafting) should wait for a human to read `stage1_signoff.md` and accept or reject the open items listed there.

## Proof

Three artifacts let a reviewer verify this stage without re-running any searches:

- **`stage1_manifest.csv`** — a flat, 29-row ledger of every candidate source across all 8 meetings, with its score, flag, and the specific meeting issue it answers. This is the machine-checkable evidence.
- **`stage1_signoff.md`** — the audit narrative: what was checked, what passed, what was found and corrected (a mis-flagged category, an overstated date), and what's still open.
- **`rejected_results.md`** — the negative space: what was found and deliberately excluded, and why, so the absence of a source isn't mistaken for an oversight.
