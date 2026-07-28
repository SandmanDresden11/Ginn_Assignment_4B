---
name: bd-market-memo
description: Draft a BD (business development) meeting memo that connects a specific sales/partnership meeting's notes to independently gathered web-search market evidence. Use only when the task supplies both meeting notes and web-search research evidence for the same meeting (or explicitly asks for a "BD meeting memo" connecting the two). Produces one schema-conformant Markdown memo per meeting with fact/inference/recommendation separated, TBD-marked follow-ups, cited market claims, and human-review flags for pricing, security, legal/regulatory, and competitive claims. Never sends messages, edits CRM records, makes commitments, or gives legal advice.
---

# BD Market Memo

## When this skill applies

Trigger this skill only when **both** of the following are true for the current task:

1. There are meeting notes for a specific prospect/partner meeting (attendees, discussion, open items), **and**
2. There is web-search-derived market/competitive research evidence gathered for that same meeting (source title, publisher, date, URL, and a relevance judgment).

Also trigger if the user explicitly asks for "a BD meeting memo," "a memo connecting meeting notes to research," or equivalent, even if the two inputs haven't been pasted in yet — in that case, ask for (or locate) the missing input before drafting.

**Do not trigger** for: general meeting summarization with no research angle, market research summaries with no meeting to anchor them, CRM data entry, or any request to draft outbound messages, proposals, or contracts.

## What this skill produces

Exactly one Markdown memo per meeting, following the schema in [references/output-schema.md](references/output-schema.md). Nothing else is written to CRM, email, or calendar systems — this skill drafts an internal analysis document for a human BD professional to review and act on.

## Non-negotiable judgment rules

### Rule A — Complete follow-up

A follow-up entry is "complete" only when it has all five of:

- **Action** — what will be done
- **Owner** — who is responsible
- **Timeline** — when it is due
- **Rationale** — why this follow-up matters, grounded in the meeting discussion
- **Confidence** — how firm the commitment is (e.g., firm commitment vs. tentative/no commitment made)

**Never invent a missing owner or date.** If the meeting notes don't name an owner or don't give a date, write `TBD` in that field literally, and add the follow-up to a **Human Review Required** list for explicit assignment. A follow-up with a `TBD` field is still reported — it is just marked incomplete, never silently completed with a guess.

### Rule B — Search-result relevance gate (score-3 only)

Only include a web-search result in the memo if it has relevance score 3, as defined in [references/relevance-rubric.md](references/relevance-rubric.md): the source directly **changes, confirms, or reprioritizes** a specific next step from that specific meeting. Generic, redundant, off-topic, or merely-related evidence (score ≤2) is excluded from the memo body — note in an audit/appendix line that lower-scoring evidence was considered and excluded, but do not use it to support a claim.

If the supplied research evidence doesn't identify relevance scores at all, do not assume score 3 — treat as insufficient evidence per the fail-clean behavior below, and ask for scored evidence.

## Sourcing requirements for every market claim

Every claim about the market, a competitor, pricing, or a vendor capability must carry, inline or in a footnote: **title, publisher, date (or "undated — verify before use" if the source has no date), and URL.** A claim that cannot be traced to a source with all four fields must be labeled an inference or dropped, not stated as fact.

## Fact / inference / recommendation separation

Structure memo content so a reader can tell at a glance which category each statement belongs to:

- **Fact** — directly stated in the meeting notes or directly supported by a cited score-3 source.
- **Inference** — a reasonable interpretation or connection the memo author is drawing between a meeting issue and a source (label it as such; don't blend it into "Fact").
- **Recommendation** — a suggested next step for the human BD owner to consider. Recommendations are proposals, not commitments — see Prohibited Actions.

Never merge these three into one undifferentiated paragraph. Use the section structure in the output schema to keep them visually and structurally distinct.

## Mandatory human review flags

Flag the following categories for **explicit human review** before anything in the memo is acted on or shared externally — see [references/human-review-policy.md](references/human-review-policy.md) for the full policy and examples:

- **Pricing** — any dollar figure, discount, tier, or commercial term
- **Security** — any claim about access control, data handling, encryption, audit logging, or platform security posture
- **Legal/regulatory** — any claim touching compliance, consent, data protection law, or regulatory exposure
- **Major competitive claims** — any claim comparing this vendor to a named competitor's capability, pricing, or positioning

A source can carry more than one flag (e.g., "Security; Legal/regulatory"). Flag at the claim level, not just the source level, if a single source contains both flagged and unflagged content.

## Prohibited actions

This skill drafts an internal memo only. It must never, under any circumstances:

- Send emails, chat messages, or any other outbound communication
- Create, update, or delete CRM records
- Make or imply a commitment, promise, discount, or deadline on behalf of the company
- Provide legal advice or a definitive legal/compliance conclusion (legal/regulatory content is flagged for counsel, not resolved)

If a draft would require any of the above to be "complete," stop short and flag it for the human owner instead of completing it.

## Fail-clean behavior

Before drafting, verify:

1. The meeting notes file exists, is non-empty, and contains at least a date, participants, and discussion content.
2. The research evidence file exists, is non-empty, and contains at least one candidate source with title/publisher/date/URL and a relevance judgment.
3. At least one source clears the score-3 relevance bar (Rule B).

If any check fails, do not fabricate content to compensate. Instead, produce a short status report (not a full memo) that names:
- which input was missing, empty, malformed, or insufficient
- what exactly is missing (e.g., "no source cleared the relevance-3 bar; 2 candidate sources were score-2 or below")
- what a human would need to supply or fix before a memo can be drafted

Use the "Status: Insufficient Input" variant described in [references/output-schema.md](references/output-schema.md) for this case, rather than returning an error message with no structure.

## Reference files

- [references/output-schema.md](references/output-schema.md) — the required memo section structure (both success and insufficient-input variants)
- [references/relevance-rubric.md](references/relevance-rubric.md) — how to score search-result relevance (score 3 vs. lower) and worked examples
- [references/human-review-policy.md](references/human-review-policy.md) — full definitions and examples for each human-review flag category
