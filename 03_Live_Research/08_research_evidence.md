# 08 — Finley Growth Capital Portfolio: Live Research Evidence

**Search date:** 2026-07-28
**Classroom simulation note:** HubSpot is the only real organization. Finley Growth Capital, its staff, and all commercial details are invented for this exercise.

## Exact queries run

1. `Microsoft Dynamics 365 Copilot sales-agent capabilities 2026 for Azure-standardized companies`
2. `HubSpot data export and API access for CRM offboarding`
3. `HubSpot implementation time and administrative effort for companies under 150 employees`

## Candidate sources

### 1. Microsoft Dynamics 365 Blog — "Moving sales and service organizations forward with agentic CX and Microsoft 365 Copilot"
- **Publisher:** Microsoft (first-party product blog)
- **Publication/update date:** July 7, 2026
- **URL:** https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2026/07/07/moving-sales-and-service-organizations-forward-with-agentic-cx-and-microsoft-365-copilot/
- **Factual claim:** Sales Agent is a role-based Copilot experience unifying AI-powered insights, conversational intelligence, and seller workflows embedded directly in Outlook, Teams, mobile apps, and Copilot chat. The 2026 release wave 1 (rolling out April–September 2026) focuses on making Sales Agent "the daily command center for sellers," expanding conversational access to sales data and deepening configuration, governance, and extensibility at scale.
- **Meeting issue it connects to:** Marcus's rationale for Microsoft — "companies already standardized on Azure and Microsoft 365... a reason to avoid introducing another platform" — citing embedded Copilot/sales-agent capabilities.
- **What it changes/confirms/deprioritizes:** Confirms Marcus's rationale is grounded in a real, actively expanding capability rather than a vague sales pitch. Maya's platform-neutral decision scorecard should reflect this honestly, weighing it against HubSpot's ease-of-adoption advantages for the smaller portfolio companies rather than dismissing either side's argument.
- **Relevance score:** 3
- **Credibility/recency note:** First-party Microsoft blog, dated July 7, 2026 — only three weeks old as of this search. High credibility and highly current.
- **Human-review flag:** Major competitive claim

### 2. HubSpot Developers — "CRM Exports API" guide
- **Publisher:** HubSpot (first-party developer documentation)
- **Publication/update date:** Not explicitly dated (current live documentation)
- **URL:** https://developers.hubspot.com/docs/api-reference/crm-exports-v3/guide
- **Factual claim:** HubSpot supports an account-wide export (Settings > Account Defaults > Privacy & Consent > Export your account data) delivered as a single zip file, positioned as meeting GDPR data-portability requirements, plus a CRM Exports API (POST /crm/v3/exports/export/async) capped at 30 API-based exports per rolling 24-hour window for paid accounts, requiring Super Admin approval to grant the `crm.export` OAuth scope. However, most — not all — data is exportable; exported formats require cleanup before reuse elsewhere; workflows cannot be exported as portable configurations (only cloned within HubSpot); and neither export type preserves property history or object associations in an easily rejoinable way.
- **Meeting issue it connects to:** Lauren's explicit request for "a transparent exit path so portfolio companies can export data and avoid unnecessary lock-in."
- **What it changes/confirms/deprioritizes:** A nuanced and partly unfavorable finding: HubSpot does support export (meeting a baseline "not fully locked in" bar), but practical portability is limited — automation logic and object relationships don't travel cleanly to another system. This should directly shape Marcus's "architecture and data-portability questions for the evaluation" and be disclosed candidly to Lauren rather than assumed to be a clean, complete export.
- **Relevance score:** 3
- **Credibility/recency note:** First-party technical documentation — high credibility and specific.
- **Human-review flag:** Major competitive claim

### 3. Pedowitz Group — "How Long Does a HubSpot CRM Implementation Take? A Realistic Timeline by Company Size"
- **Publisher:** Pedowitz Group (HubSpot solutions-partner agency, third-party)
- **Publication/update date:** Not explicitly dated in search result
- **URL:** https://www.pedowitzgroup.com/blog/how-long-does-a-hubspot-crm-implementation-take-a-realistic-timeline-by-company-size-1
- **Factual claim:** Small businesses with a simple sales process can go live in 2–4 weeks; growing mid-market organizations typically need 2–3 months. DIY HubSpot setup consumes roughly 150–400 internal ops/admin hours for a typical SMB with high rework risk, while partner-led implementation cuts internal team involvement to 20–60 hours. The largest timeline variable is usually how quickly internal stakeholders agree on lifecycle-stage definitions, lead-scoring criteria, and SLA terms — not the software itself.
- **Meeting issue it connects to:** The pilot plan for a 70-person IT services firm and a 140-person compliance consultancy, measured by "time to usable pipeline reporting, seller adoption, data cleanup effort."
- **What it changes/confirms/deprioritizes:** Gives Erin's "faster adoption, simpler administration" argument concrete numbers — a partner-led implementation at 20–60 hours over 2–4 weeks for a simple-process small company is a strong data point in her favor — but the caveat that stakeholder alignment (not the tool) is usually the biggest variable should be flagged so the scorecard doesn't overpromise speed based on platform choice alone.
- **Relevance score:** 3
- **Credibility/recency note:** Third-party HubSpot solutions-partner blog — moderate-to-good credibility; numbers are specific, but the source has a commercial interest in favorable HubSpot timelines, so corroborate with a non-partner source if this figure goes into a client-facing scorecard.
- **Human-review flag:** None

## Evidence sufficiency check

3 of 3 candidate sources scored 3. Sufficient decision-relevant evidence exists for this meeting's approved queries.
