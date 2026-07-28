# Relevance Rubric

Every candidate web-search result gets a relevance score from 1-3 against **one specific meeting**. Only score-3 sources are eligible for the memo (Rule B in SKILL.md). This rubric exists so scoring is consistent across meetings and across different people/models applying it.

## Score 3 — Include

The source **directly changes, confirms, or reprioritizes a specific next step** named in that meeting's notes. All three of these must be true:

1. It is traceable to a specific issue, question, or concern actually raised in the meeting (not a generic topic match).
2. It gives new information that would make a reasonable BD professional act differently, feel more confident, or flag a new risk — not just "related background."
3. It has title, publisher, date (or explicitly notes it is undated), and URL.

**Worked example (score 3):** Meeting notes record Dana's concern about "buying an expensive add-on before the underlying data is cleaned." A source describing HubSpot's move to outcome-based pricing (pay only per completed task, not a flat license) directly changes the cost framing Dana was worried about — it reframes whether the sequencing concern still applies. This scores 3.

## Score 2 — Exclude from memo, log in Excluded Evidence

The source is **topically related but does not resolve the specific question** raised in the meeting — it's context, not an answer. Common patterns:
- Confirms a general capability exists but not the specific configuration/permission/scope the meeting asked about (e.g., "AI drafts get human review" when the question was specifically about *role-based* approval).
- Provides directional/unverified figures where the meeting needs a specific, confirmed number (e.g., a third-party pricing comparison citing unverified dollar amounts when the meeting needs primary-source pricing).

**Worked example (score 2):** Lynn asked whether AI-generated outreach can be governed **by role and by approved templates**. A source confirming HubSpot has a general "review before send" step answers a broader question but not the role-based governance Lynn specifically raised. Log this as excluded with the reason, don't cite it as if it settles Lynn's question.

## Score 1 — Exclude, and typically don't even log in per-meeting evidence

Generic or off-topic content that a keyword match surfaced but which doesn't speak to this meeting's actual decisions at all (e.g., generic "AI readiness for consulting firms" content when the meeting needs referral-selling-specific evidence). Usually captured in a rejected-results log with a one-line reason (redundant / off-topic / low authority / commercial conflict of interest / over-generic), not carried into the per-meeting evidence file at all.

## Applying the rubric when scores are already provided

If the research evidence you're given already includes relevance scores (e.g., in a manifest or evidence file), do not re-score from scratch — use the provided scores, but spot-check that a score-3 label actually has a stated "meeting issue connection." If a source is labeled score 3 with no stated connection to a specific meeting issue, treat it as insufficient per the fail-clean rule rather than trusting the label blindly.

## Common failure modes to avoid

- **Score inflation:** don't mark something score 3 just because it's from a first-party/reputable source — credibility and relevance are separate axes. A perfectly credible source that doesn't address this meeting's specific issue is still score ≤2.
- **Silent exclusion:** don't just drop score-2/1 sources with no trace. They belong in the memo's Excluded Evidence section (score 3-only) so a reviewer can see the gate was applied, not skipped.
- **Treating "undated" as disqualifying:** an undated source can still be score 3 if it otherwise meets the bar — just carry the "undated, verify before use" caveat into the memo rather than excluding it solely for lacking a date.
