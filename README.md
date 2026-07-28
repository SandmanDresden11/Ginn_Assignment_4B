# BD Meeting Memo — Skill + Batch Pipeline

This project turns two upstream inputs — a **BD meeting's notes** and **independently gathered, scored web-search research evidence** for that same meeting — into one schema-conformant Markdown memo per meeting, plus a JSON audit record. It is a classroom exercise: **HubSpot is the only real organization referenced anywhere in the sample data**; every prospect (Northstar, Meridian, Harborline, SummitWorks, BrightPath, BluePeak, NABC, Finley Growth Capital), person, and commercial detail is invented.

This is "Stage 2" of a two-stage pipeline. Stage 1 (already complete, see `03_Live_Research/stage1_signoff.md`) gathered and audited web-search evidence per meeting, scored each candidate source's relevance, and flagged sensitive categories. This project consumes that Stage 1 output — it does not re-run web research.

## Project structure

```
.claude/skills/bd-market-memo/
  SKILL.md                          # trigger conditions, judgment rules, prohibited actions
  references/output-schema.md       # required memo section structure (2 shapes)
  references/relevance-rubric.md    # how the score-3 relevance gate is applied
  references/human-review-policy.md # pricing/security/legal/competitive flag definitions
scripts/
  batch_process.py                  # pairs notes + research, drafts memos, writes audit JSON
  validate_outputs.py                # checks schema compliance, produces a CSV summary
tests/
  test_plan.md                      # runnable dry-run test plan (no API key needed)
  fixtures/edge_case_vague_notes.md  # meeting notes with no owners/dates/commitments
  fixtures/weak_search_evidence.md   # research evidence where nothing scores 3
01_Meeting_Notes/*.docx              # the 8 sample meetings (input)
03_Live_Research/*_research_evidence.md, stage1_manifest.csv, stage1_signoff.md  # Stage 1 output (input)
```

## Setup

Requires Python 3.11+.

```bash
pip install -r requirements.txt
```

Live mode additionally requires the `ANTHROPIC_API_KEY` environment variable to be set. **Never** paste your key into a file this repo tracks, and the scripts never print it — only "is/isn't set" is logged.

## Usage

### Dry run (no API calls, no API key required)

```bash
python scripts/batch_process.py \
  --notes-dir 01_Meeting_Notes \
  --research-dir 03_Live_Research \
  --out-dir out \
  --dry-run
```

Writes, per meeting: `out/<NN>_<slug>_memo.md` (in dry-run mode, this is the **complete assembled prompt packet** the API would receive — not generated prose) and `out/<NN>_<slug>_audit.json` (deterministic stats: source counts, relevance-gate results, human-review flags, elapsed time — computed without any model call).

### Live mode

```bash
export ANTHROPIC_API_KEY=sk-...      # set in your shell, never in a tracked file
python scripts/batch_process.py \
  --notes-dir 01_Meeting_Notes \
  --research-dir 03_Live_Research \
  --out-dir out \
  --model claude-sonnet-5
```

Same output layout, but `<NN>_<slug>_memo.md` now contains the actual drafted memo per `references/output-schema.md`.

**Do not run live mode until you've reviewed dry-run output** — that's the point of the dry-run flag.

### Validate outputs

```bash
python scripts/validate_outputs.py --out-dir out
```

Checks required memo sections, that every recommended action has an owner+timeline or an explicit `TBD`, and that every claim the audit data marks eligible has a URL and relevance score 3. Writes `out/validation_summary.csv`.

## Judgment rules this skill enforces

- **Rule A — complete follow-up:** action + owner + timeline + rationale + confidence. Missing owner/date is marked `TBD` and routed to human review — never invented.
- **Rule B — relevance gate:** only score-3 search results (directly changes/confirms/reprioritizes a specific next step from that meeting) are cited in a memo. Lower-scoring evidence is logged as excluded, not silently dropped or smuggled in.
- **Mandatory human-review flags:** pricing, security, legal/regulatory, and major competitive claims are always routed to a human — this skill never resolves them itself.
- **Hard prohibition:** this skill never sends messages, edits CRM records, makes commitments, or gives legal advice. It drafts an internal analysis document only.

See `.claude/skills/bd-market-memo/SKILL.md` for the full rules.

## Testing

See [tests/test_plan.md](tests/test_plan.md) for a complete, runnable test plan covering normal meetings, the vague-notes edge case, and the weak-search-evidence failure case — all runnable in dry-run mode with no API key.
