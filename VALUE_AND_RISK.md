# Value & Risk Translation

This document translates the bd-market-memo pipeline's time savings into a dollar figure, names the concrete risks of automating memo drafting, states the mitigation already built into the skill for each, and lays out a 30-day adoption plan. It complements [tests/test_plan.md](tests/test_plan.md), which has the underlying time estimates, and the skill's own [.claude/skills/bd-market-memo/references/human-review-policy.md](.claude/skills/bd-market-memo/references/human-review-policy.md), which has the full flag policy.

## Time → $ math

### Drafting time saved per memo

From [tests/test_plan.md](tests/test_plan.md)'s before/after estimate:

| | Manual | With pipeline |
|---|---|---|
| Total time per memo | ~70-105 min | ~11-18 min |
| Midpoint | ~87.5 min | ~14.5 min |

**Time saved per memo ≈ 73 minutes (~1.22 hours).**

The saved time is entirely in drafting mechanics (re-reading notes, cross-referencing research, structuring fact/inference/recommendation, applying the flag policy consistently) — not in the human-review step, which stays at 10-15 minutes in both columns because Rule A and Rule B exist specifically to keep judgment calls with a person, not to automate them away.

### Dollar value

Assumption (adjust for your own team): a **BD manager or BD-ops analyst** who would otherwise hand-draft these memos costs the org roughly **$60/hour fully loaded** (salary + benefits + overhead — a mid-market planning number, not a real employee's rate; substitute your own).

- **Per memo:** 1.22 hr × $60/hr ≈ **$73 saved**
- **Across the 8 sample meetings** (one batch pass): 8 × $73 ≈ **$584 saved**
- **At a plausible monthly BD cadence** (e.g. 20 qualifying meetings/month needing a memo): 20 × $73 ≈ **$1,460/month**, or **~$17,520/year**

### API cost (the offsetting expense)

Using current Claude Sonnet 5 pricing ($3.00/$15.00 per million input/output tokens; introductory $2.00/$10.00 through 2026-08-31) and a rough token estimate for this specific prompt (system prompt ≈ 6,500 words of skill instructions + references ≈ 8,800 tokens; user message ≈ 2,750 words of meeting notes + research evidence ≈ 3,700 tokens; output ≈ 1,500-word memo ≈ 2,000 tokens):

| | Intro pricing (through 2026-08-31) | Standard pricing |
|---|---|---|
| Per memo | ~$0.045 | ~$0.068 |
| All 8 sample meetings | ~$0.36 | ~$0.54 |
| 20 memos/month | ~$0.90/month | ~$1.36/month |

**API cost is roughly 0.1% of the labor value saved.** Even at 10x this estimate (longer notes, longer research files, a bigger model), API spend stays a rounding error next to the labor saved — the real cost of this pipeline is the human-review time that's deliberately *not* automated, not the API bill.

## Risk and mitigation

Four concrete risks of automating BD memo drafting, and what in this project specifically addresses each — not a generic AI-risk disclaimer.

### 1. Hallucinated or invented follow-up details

**Risk:** a model asked to summarize a meeting's action items can invent a plausible-sounding owner or date when the notes don't actually specify one — exactly the kind of error that's easy to miss on a skim and embarrassing when a BD rep acts on a commitment nobody made.

**Mitigation:** Rule A (`SKILL.md`) requires every follow-up to carry action + owner + timeline + rationale + confidence, and explicitly forbids inventing a missing owner or date — it must be marked `TBD` and routed to the memo's Human Review Required section instead. This is enforced twice: as an instruction to the drafting model, and independently in `validate_outputs.py`, which checks every follow-up row has a non-empty Owner and Timeline (real value or literal `TBD`) and fails validation if a row is silently blank.

### 2. Citing weak or irrelevant evidence as if it settled a question

**Risk:** research gathered for a different, related question can get cited as if it answers the specific question a client raised — the "score 2" failure mode documented in Stage 1's evidence files (e.g., a general AI-outreach post cited as if it settled a *role-based* governance question).

**Mitigation:** Rule B's score-3 relevance gate, enforced in Python inside `batch_process.py` before any model is even called — `parse_research_evidence()` computes eligibility deterministically from the research-evidence file's own relevance scores, and if nothing clears the bar the pipeline produces a Shape 2 "Insufficient Input" report instead of drafting a memo with weak citations. This is the one risk in this list that's checkable **without** a live API call, which is exactly what the weak-search-evidence test case in `tests/test_plan.md` demonstrates.

### 3. Sensitive claims (pricing, security, legal, competitive) presented as settled fact

**Risk:** a pricing figure, a security posture claim, or a competitor comparison gets stated in a memo as if it's current and verified, when it's actually a promotional claim, an unverified third-party figure, or something that's changed since the source was gathered (Stage 1's own signoff flags this explicitly — HubSpot's pricing and partner-terms pages were already known to be changing within weeks of the research date).

**Mitigation:** the human-review-policy.md flag categories (Pricing / Security / Legal-regulatory / Major competitive claim) route every such claim to a checklist item in the memo's Human Review Required section rather than letting it stand as unflagged fact. The skill is explicitly prohibited from resolving these itself — see Prohibited Actions in SKILL.md.

### 4. The skill acting outside its scope (sending messages, editing CRM records, giving legal advice)

**Risk:** an agent with tool access asked to "handle a BD meeting" could plausibly try to send a follow-up email or update a CRM record as a shortcut to being "helpful" — exactly the kind of scope creep that turns a drafting aid into an unauthorized commitment.

**Mitigation:** SKILL.md's Prohibited Actions section is explicit and absolute: never send messages, never modify CRM records, never make or imply a commitment, never give legal advice. The skill's only output is a Markdown file — there is no tool call in `batch_process.py` capable of sending anything anywhere.

## Practical 30-day plan

A phased rollout, not a big-bang switch — matches the trust progression a BD team would reasonably want.

| Days | Milestone |
|---|---|
| **1-3** | Clone the repo, run `batch_process.py --dry-run` across all 8 sample meetings, and have a BD lead read 2-3 assembled prompt packets to confirm the skill's rules match how the team actually wants memos drafted. No API key needed, no cost. |
| **4-7** | Get an `ANTHROPIC_API_KEY`, run live mode on the 8 sample meetings, and have a BD manager read every generated memo against `references/output-schema.md` — specifically checking that TBD-marking and relevance-gating hold up with a real model in the loop, not just in dry-run. |
| **8-14** | Pilot on 5-10 *real* upcoming meetings (not the classroom samples), run in live mode, and route every Human Review Required item to its actual owner. Track: how many follow-ups needed TBD, how many sources got flagged, how long human review actually took vs. the ~10-15 min estimate. |
| **15-21** | Adjust the skill based on pilot friction — likely candidates: refining the relevance rubric if too many/few sources are clearing the bar, or tightening the output schema if reviewers want a different section order. Re-run `validate_outputs.py` after any change to confirm nothing regressed. |
| **22-30** | Roll out to the full BD team for all qualifying meetings (both meeting notes and research evidence present, per the skill's trigger condition). Set a recurring check-in (e.g. monthly) to re-verify sensitive-category sources are still current, since pricing/partner-terms pages are exactly the kind of thing that changes without notice. |

**Go/no-go gate at day 14:** if the pilot shows follow-ups routinely need TBD-correction that a human wouldn't have needed to make from the raw notes (i.e., the skill is *worse* than a human at extracting what's actually in the notes), stop and revisit Rule A's implementation before scaling further — don't roll out on the assumption that "human review catches it," since review fatigue is a real failure mode of any human-in-the-loop system.
