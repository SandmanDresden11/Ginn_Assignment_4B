# Stage 2 GRASP Brief — Skill, Batch Pipeline, and Validation

**Stage:** Memo drafting infrastructure. Takes Stage 1's output (`stage1_manifest.csv`, `stage1_signoff.md`, the 8 `NN_research_evidence.md` files) and the 8 meeting-notes `.docx` files as fixed inputs, and builds the Claude Skill, batch script, and validation tooling that turn them into BD meeting memos — one per meeting.

## Goal

Produce a reusable, testable system — not a one-off set of memos — that any BD professional or instructor can run against these 8 meetings (or new ones with the same file-naming convention) to get a schema-conformant memo per meeting, with a machine-checkable audit trail proving the two hard judgment rules (never invent a missing owner/date; only cite score-3 evidence) were actually followed, not just asserted.

The deliverable is four things working together: `.claude/skills/bd-market-memo/SKILL.md` (the rules), `scripts/batch_process.py` (runs the rules across all 8 meetings, dry-run or live), `scripts/validate_outputs.py` (checks the rules were followed, independent of whatever drafted the memo), and `tests/` (proof the pipeline fails cleanly on bad input instead of producing something plausible-but-wrong).

## Resources

Two fixed inputs, one new artifact class created during this stage:

- **The 8 meeting-notes `.docx` files and Stage 1's research-evidence output** — treated as read-only ground truth. Nothing in this stage edits Stage 1's files or second-guesses its relevance scores; `batch_process.py`'s parser trusts the `Relevance score:` and `Human-review flag:` fields already in each `NN_research_evidence.md` file.
- **Two synthetic test fixtures I wrote** (`tests/fixtures/edge_case_vague_notes.md`, `tests/fixtures/weak_search_evidence.md`) — not real data, built specifically to exercise the two failure modes the assignment asked for: notes with no named owner/date/commitment, and research evidence where nothing clears the relevance-3 bar.
- **This conversation's own back-and-forth** — the batch script's design (parsing research evidence deterministically rather than trusting an LLM to self-report relevance scores) came directly from being asked to "run 3 live and a 4th weak-search test," which is what exposed that the relevance gate needed to be checkable without an API call at all.

## Autonomy limits

**Decided independently:**
- The audit JSON schema (source counts, eligibility, human-review flags, elapsed time) and the decision to compute it deterministically in Python from the research-evidence file, rather than trusting the drafting model to self-report which sources it used — this makes `validate_outputs.py` able to catch a hallucinated citation instead of only checking formatting.
- The two-shape memo design (Shape 1 "Complete" vs. Shape 2 "Insufficient Input") and exactly what triggers each — my judgment call on how to operationalize "fail cleanly" for this specific domain (a memo that only cites score-3 sources but has zero of them isn't a smaller memo, it's a status report).
- The specific wording of Rule A and Rule B in SKILL.md, and the flag categories in human-review-policy.md — I wrote these to match the actual Stage 1 flag vocabulary already in use (Pricing / Security / Legal-regulatory / Major competitive claim), rather than inventing a new taxonomy.
- Bugs I found and fixed while testing (not prescribed by anyone): the `.docx` paragraph/table ordering bug, the compound-flag deduplication bug, and the validate_outputs.py mode-vs-status ordering bug. All three were caught by actually running the pipeline against real data, not by inspection.

**Set or steered by the user:**
- The overall project structure (exact file/folder list) and the two required judgment rules (A and B) — given verbatim in the initial request, not something I chose.
- The requirement that the batch script support both `--dry-run` and live modes, and that live calls wait for explicit approval — this shaped the entire audit-JSON design, since dry-run needed to prove something meaningful without spending API credits.
- The instruction to test with "3 live runs and a 4th weak-search failure" — when no API key turned out to be available, this is what drove the decision to make the Rule B relevance gate fully testable in dry-run mode (a design choice made *because* of that constraint, not despite it).
- The GitHub repo requirement and the discovery, via an actual `git clone` of the pushed repo, that `.claude/` and `.gitignore` had not made it to GitHub through the manual upload — a real gap the user and I found together, not something I'm reporting after the fact.

**The honest tension:** the assignment's judgment rules (A and B) are stated in SKILL.md as instructions to a model, but I also built deterministic Python code that checks the same rules mechanically. That's a real design choice: it means Rule B, in particular, is enforced twice — once by prompting the model to only cite score-3 evidence, and once by the batch script refusing to even build the prompt if no source clears the bar. Which one is "the enforcement" and which is "a safety net" is worth being explicit about: the Python code is the one that actually gates the weak-search-evidence test case, since it runs before any model is ever called.

## Sign-off point

This stage's output is not self-validating from a single run. Two things gate confidence in it:

- All 8 real meetings and both synthetic edge cases pass `validate_outputs.py` in dry-run mode — verified in this session, output pasted into the conversation, not just claimed.
- The live-mode path (an actual model drafting Shape 1 memo content, not a hand-authored stand-in) has **not** been exercised end-to-end in this session, because no `ANTHROPIC_API_KEY` was available. The one "live-style" memo produced (meeting 01, Northstar) was drafted by me directly inside this Claude Code session following SKILL.md's rules by hand, with the source-level audit data computed by the real parser — a reasonable stand-in for demonstrating the schema, but not proof that `batch_process.py`'s live mode, calling the API automatically, produces the same quality of output unattended.

Before relying on this for a real BD workflow, a human should run `batch_process.py` in live mode with a real API key against at least the vague-notes and weak-search fixtures, and read the actual model output — not just the dry-run prompt packets — to confirm Rule A's TBD-marking and Rule B's citation discipline hold up when a model is actually generating prose, not just receiving instructions.

## Proof

- **`tests/test_plan.md`** — the runnable command sequence and expected results for all three required test scenarios (normal meetings, vague notes, weak search), plus a bonus mismatched-file-prefix case, all executable without an API key.
- **This conversation's tool-call transcript** — every `validate_outputs.py` run in this session shows its actual stdout (pass/fail counts, per-meeting notes), not a summary I wrote afterward.
- **`out/01_Northstar_Advisory_Discovery_audit.json`** — the one example audit record, with a `note` field that discloses plainly how it was produced (manually, inside this session, not via `batch_process.py`'s live mode) so a reviewer doesn't mistake it for an automated API run.
