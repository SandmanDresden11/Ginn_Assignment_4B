# Validation Note — bd-market-memo Skill

Two tests actually run, 2026-07-28/29. Both used the live pipeline (`scripts/batch_process.py`) and, where noted, a live model drafting pass or a live web search — nothing here is a hypothetical walkthrough of `tests/test_plan.md`.

## Test 1: Edge case — vague notes paired with mismatched research

`tests/fixtures/edge_case_vague_notes.md` (Cascade Retail Partners: no owners, no exact date, no specific issue named) was converted to `.docx` and run through `batch_process.py --dry-run`, paired — per the test plan, since the fixture ships no evidence file of its own — with `03_Live_Research/01_research_evidence.md`, which is actually **Meeting 01's (Northstar's)** research file.

The dry run reported `status: ok`, exit code 0. Its mechanical Rule B check only verifies that at least one source carries `relevance_score: 3` — it can't check whether that source's "meeting issue connection" names anything in the meeting it's paired with. That's a real false-positive risk: in isolation, "ok, exit 0" reads as a green light to draft. It isn't — all four eligible sources named Northstar people (Dana, Priya, Sam, Eli), none of whom appear in Cascade's notes.

I then ran the live drafting step myself — the part `--dry-run` skips — applying `SKILL.md` directly. The relevance rubric warns a score-3 label doesn't transfer blindly; re-checked against Cascade's actual notes, none of the four sources survive, and Cascade names no specific issue to test anything against regardless. Correct output: Shape 2, "Insufficient Input" (`tests/tmp/vague_notes/out/09_Cascade_Retail_Partners_memo.md`). Rule A never entered the picture — the memo never reached a follow-up table to guess an owner or date on.

**Takeaway:** dry-run's `ok` status means "not obviously broken," not "ready to draft." The semantic half of Rule B only runs at the live-drafting step — a meeting/evidence mismatch will sail through the mechanical gate.

## Test 2: Search failure — refining a weak query

Meeting 02's original research pass queried `HubSpot approval workflows for AI-generated sales outreach by role` to answer Lynn's question about role-based governance of AI outreach. It returned a general "review before sending" blog post, scored 2 — it confirmed a draft/approve step exists but said nothing about role-specific control.

I re-ran the exact refinement `stage1_signoff.md` recommended but never executed: `HubSpot Sales Hub user permissions and content approval settings`. This surfaced HubSpot's own "Overview of approvals in HubSpot" and user-permissions knowledge-base pages, naming specific controls — a "Prospecting agent assignment" toggle, per-user Templates edit access, Super-Admin-gated approval setup, multi-approver pipeline stages — materially more specific than the first pass.

**Takeaway:** refining improved relevance but didn't fully close the gap to a clean score 3. The new sources confirm granular, named permission controls exist, but neither states that "Prospecting agent assignment" governs *AI-drafted outreach content* specifically, versus general tool access. A human would still need one more targeted check before citing this as settling Lynn's question. Refinement narrowed the gap; it didn't close it — useful signal this claim stays below score-3 and belongs in Excluded Evidence, not the memo body.
