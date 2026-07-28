# Output Schema

Every meeting produces exactly one Markdown file. There are two possible shapes: the normal **Memo** (sufficient input) and the **Insufficient Input** status report (fail-clean case). Never mix the two — pick one shape and use it completely.

## Filename convention

`<NN>_<meeting-slug>_memo.md`, where `NN` is the two-digit meeting prefix shared with the source notes and research-evidence files (e.g., `01_Northstar_Advisory_Discovery_memo.md`).

---

## Shape 1: Memo (sufficient input)

```markdown
# BD Meeting Memo — <Meeting Title>

**Meeting date:** <date from notes, or "not stated in notes">
**Memo generated:** <ISO date/time of generation>
**Meeting file:** <source filename>
**Research evidence file:** <source filename>
**Status:** Complete

## 1. Meeting Summary (Fact)

2-5 sentences, drawn only from the meeting notes: who attended, what was discussed, what was and was not agreed. No claims from research sources belong in this section.

## 2. Key Issues Raised

A bullet list of the specific questions, concerns, or requirements raised in the meeting that research was gathered to address. Attribute each to the person who raised it when the notes name one (e.g., "Dana's migration-risk concern").

## 3. Market & Competitive Evidence (Fact, cited)

One entry per score-3 source that survived the relevance gate (Rule B). Each entry:

```markdown
### <Source title>
- **Publisher:** <publisher>
- **Date:** <date, or "undated — verify before use">
- **URL:** <url>
- **Connects to:** <the specific meeting issue from Section 2 this source addresses>
- **Finding (Fact):** <what the source states, restated neutrally>
- **Human review flag:** <None | Pricing | Security | Legal/regulatory | Major competitive claim | combination>
```

If a flag other than "None" is present, also add a line: `> ⚠ Human review required before this claim is shared externally or acted on.`

## 4. Inferences

Bullet list of reasonable interpretations connecting a Section 2 issue to a Section 3 source, explicitly labeled as inference rather than fact (e.g., "This *suggests* HubSpot's outcome-based pricing could address Dana's sequencing concern, though it does not confirm the board will accept an AI trial before full data cleanup."). Do not state these as settled facts.

## 5. Recommended Follow-Ups

A table. Every row must satisfy Rule A — Action, Owner, Timeline, Rationale, Confidence are all required fields (using `TBD` where the notes don't specify):

| Action | Owner | Timeline | Rationale | Confidence |
|---|---|---|---|---|
| <what will be done> | <name or TBD> | <date or TBD> | <why, tied to meeting/evidence> | <Firm commitment / Tentative / No commitment made> |

Any row containing `TBD` in Owner or Timeline must also appear in Section 6.

## 6. Human Review Required

A checklist of everything that needs explicit human sign-off before action, merging:
- Every follow-up row from Section 5 with a `TBD` owner or timeline (needs assignment)
- Every source/claim flagged Pricing, Security, Legal/regulatory, or Major competitive claim in Section 3 (needs verification/counsel/approval before external use)

```markdown
- [ ] Assign owner for: "<action>" (currently TBD)
- [ ] Confirm timeline for: "<action>" (currently TBD)
- [ ] Verify pricing claim before quoting externally: "<claim, source>"
- [ ] Legal/regulatory claim requires counsel review: "<claim, source>"
```

## 7. Excluded Evidence (Audit Note)

One line per candidate source that did NOT clear the score-3 bar, so a reviewer can see what was considered and rejected, not just what was used:

```markdown
- "<source title>" (score <N>) — excluded: <one-line reason>
```

## 8. Scope Note

Always include this closing block verbatim (edit only the bracketed meeting reference):

```markdown
---
This memo is an internal analysis aid for [meeting reference]. It does not constitute a commitment, contract, legal advice, or CRM update. No message was sent and no CRM record was changed as part of producing this memo. All Human Review Required items must be resolved by an authorized human before any claim in this memo is shared externally or acted upon.
```

---

## Shape 2: Insufficient Input (fail-clean)

Used whenever meeting notes or research evidence are missing, empty, malformed, or don't contain at least one score-3 source.

```markdown
# BD Meeting Memo — Status Report

**Meeting file:** <filename or "not found">
**Research evidence file:** <filename or "not found">
**Memo generated:** <ISO date/time>
**Status:** Insufficient Input — memo not drafted

## What was checked

- [ ] Meeting notes file present and non-empty
- [ ] Meeting notes contain date, participants, and discussion content
- [ ] Research evidence file present and non-empty
- [ ] Research evidence contains title/publisher/date/URL and a relevance judgment per source
- [ ] At least one source meets the relevance-3 bar

(Mark each with ✅ or ❌ based on what was actually found.)

## What is missing

Plain-language description of exactly what's missing or insufficient, e.g.:
"3 candidate sources were supplied; all scored 2 or below on relevance. No source directly changes, confirms, or reprioritizes a next step from this meeting, so Rule B blocks memo drafting."

## What a human needs to supply or fix

A short, actionable list, e.g.:
- Re-run research with a more targeted query: `<suggested query>`
- Confirm the correct research-evidence file was provided for this meeting number
- Add participant names/date to the meeting notes if missing

No memo body, follow-up table, or evidence section is produced in this shape — do not partially fill Shape 1's sections with guessed content.
