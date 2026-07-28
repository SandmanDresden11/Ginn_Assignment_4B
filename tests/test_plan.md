# Test Plan — bd-market-memo batch pipeline

All commands below use `--dry-run`, so **no Anthropic API calls or API keys are required** to run this entire plan. Dry-run mode still exercises every deterministic part of the pipeline: file discovery/matching, `.docx` text extraction, research-evidence parsing, the Rule B relevance gate, prompt-packet assembly, audit-record generation, and `validate_outputs.py`. Only the actual memo prose (Shape 1 body) requires a live API call, which is intentionally out of scope until the dry-run output is approved.

## 1. Normal meeting tests (≥3 required)

The repo ships all 8 real classroom meetings already paired in `01_Meeting_Notes/` and `03_Live_Research/`. Run the full batch in dry-run mode (all 8 doubles as "at least 3 normal meetings" — meetings 01, 04, and 05 are good representative picks if you want to spot-check individually):

```bash
python scripts/batch_process.py \
  --notes-dir 01_Meeting_Notes \
  --research-dir 03_Live_Research \
  --out-dir tests/tmp/normal_run \
  --dry-run
```

**Expected result:** 8 meetings processed, each with `status: ok` and `mode: dry_run` in its audit JSON, since every meeting has ≥2 score-3 sources per `stage1_signoff.md`. Each `*_prompt_packet` memo file contains the full SKILL.md + references system prompt and a user message embedding that meeting's notes and research evidence. Exit code 0.

Then validate:

```bash
python scripts/validate_outputs.py --out-dir tests/tmp/normal_run
```

**Expected result:** dry-run rows are reported as "schema checks not applicable" (Shape 1 memo-section checks don't apply to a prompt packet) but each row still reports `sources_total`, `sources_eligible`, and `human_review_flags` pulled from the parsed research-evidence file, e.g. meeting 03 (Harborline) should show human-review flags including `Security` and `Legal/regulatory`, meeting 05 (BrightPath) should show `Pricing`.

**Manual spot-check (recommended before approving live mode):** open 2-3 of the generated prompt-packet files in `tests/tmp/normal_run/` and confirm:
- [ ] The system prompt includes Rule A, Rule B, the human-review flag categories, and the prohibited-actions list verbatim from SKILL.md.
- [ ] The user message contains the actual meeting notes text (not truncated/garbled) and the actual research evidence markdown.
- [ ] No API key or secret appears anywhere in the packet file.

## 2. Vague-notes edge case

`tests/fixtures/edge_case_vague_notes.md` is meeting notes prose with a date, participants, and discussion (so it should NOT be rejected as empty/malformed) but deliberately has **no named owner, no specific date, and no confident commitment** in its "Where the Meeting Was Left" section. This exercises Rule A (never invent an owner/date — mark TBD).

Because `batch_process.py` requires `.docx` input for notes, convert the fixture to `.docx` first:

```bash
python - <<'PY'
import docx
from pathlib import Path

src = Path("tests/fixtures/edge_case_vague_notes.md").read_text(encoding="utf-8")
out_dir = Path("tests/tmp/vague_notes/notes")
out_dir.mkdir(parents=True, exist_ok=True)

doc = docx.Document()
for line in src.splitlines():
    doc.add_paragraph(line)
doc.save(out_dir / "09_Cascade_Retail_Partners.docx")
PY

mkdir -p tests/tmp/vague_notes/research
cp 03_Live_Research/01_research_evidence.md tests/tmp/vague_notes/research/09_research_evidence.md

python scripts/batch_process.py \
  --notes-dir tests/tmp/vague_notes/notes \
  --research-dir tests/tmp/vague_notes/research \
  --out-dir tests/tmp/vague_notes/out \
  --dry-run
```

(We pair the vague notes with a normal, score-3 research file so the run reaches the prompt-packet stage rather than short-circuiting on the research side — that keeps this test isolated to the notes-side judgment rule.)

**Expected result:** `status: ok`, `mode: dry_run`, exit code 0. The prompt packet is produced successfully (dry-run mode doesn't evaluate note quality — that judgment happens when a model actually drafts the memo).

**What this test actually proves in dry-run mode:** the pipeline doesn't choke on sparse/vague prose, and the assembled prompt correctly carries both the vague notes text and Rule A's explicit "never invent a missing owner or date... mark TBD" instruction. **Full behavioral confirmation** (that the model actually writes TBD instead of guessing "Maya" or "next Friday") requires either a live API run or manual review by a human drafting the memo using the packet's instructions — flag this file for that manual/live check before relying on it for grading.

## 3. Weak-search failure case

`tests/fixtures/weak_search_evidence.md` has two candidate sources, both scoring ≤2. This is fully deterministic and testable in dry-run mode — the Rule B relevance gate runs inside `batch_process.py` itself, independent of any LLM call.

```bash
mkdir -p tests/tmp/weak_search/notes tests/tmp/weak_search/research
cp 01_Meeting_Notes/01_Northstar_Advisory_Discovery.docx tests/tmp/weak_search/notes/09_Cascade_Retail_Partners.docx
cp tests/fixtures/weak_search_evidence.md tests/tmp/weak_search/research/09_research_evidence.md

python scripts/batch_process.py \
  --notes-dir tests/tmp/weak_search/notes \
  --research-dir tests/tmp/weak_search/research \
  --out-dir tests/tmp/weak_search/out \
  --dry-run

python scripts/validate_outputs.py --out-dir tests/tmp/weak_search/out
```

**Expected result:** meeting `09` audit JSON shows `status: insufficient_input`, `source_count: 2`, `eligible_source_count: 0`, `relevance_failures` listing both sources with their scores. The memo file is the Shape 2 "Insufficient Input" status report (not a prompt packet, since the pipeline never reaches the API-call stage). `validate_outputs.py` confirms the Shape 2 required sections (`What was checked`, `What is missing`, `What a human needs to supply or fix`) are present. Batch exit code is still 0 (insufficient-input is a clean, expected outcome, not a processing failure) — only unhandled exceptions should cause a non-zero exit.

## 4. Mismatched-prefix / missing-file case (bonus robustness check)

Run against a notes-dir or research-dir with a meeting number that has no counterpart on the other side, and confirm `status: insufficient_input` with a clear "file not found for this prefix" message rather than a crash.

## 5. Before/after time estimate

Illustrative estimates for a BD professional producing one memo like this, for classroom discussion — not a rigorous benchmark:

| Step | Manual (no tooling) | With this pipeline |
|---|---|---|
| Re-read meeting notes and extract issues | 10-15 min | 0 min (done once, feeds prompt) |
| Web research per issue + credibility triage | 30-45 min | 0 min (already completed in Stage 1, upstream of this skill) |
| Draft memo, separate fact/inference/recommendation, apply flags | 20-30 min | ~1-3 min (API call, live mode) |
| Human review of flagged items + TBD assignment | 10-15 min | 10-15 min (unchanged — this step is intentionally never automated) |
| **Total** | **~70-105 min** | **~11-18 min** |

The time savings come entirely from drafting mechanics (structuring, cross-referencing, applying the schema consistently); the human-review step is deliberately preserved at full length since Rule A/B and the flag policy exist specifically to keep judgment calls with a person.

## Running everything at once

```bash
python -m py_compile scripts/batch_process.py scripts/validate_outputs.py
```

Then run sections 1 through 4 above in order.
