# 04 — SummitWorks Engineering Integration: Live Research Evidence

**Search date:** 2026-07-28
**Classroom simulation note:** HubSpot is the only real organization. SummitWorks, its staff, and all commercial details are invented for this exercise.

## Exact queries run

1. `Salesforce custom objects and account hierarchy capabilities for engineering and AEC firms`
2. `HubSpot custom objects and account hierarchy support 2026`
3. `HubSpot Deltek Vantagepoint integration options`
4. `HubSpot event-based workflow triggers for staged handoff to an external ERP`

## Candidate sources

### 1. Salesforce Ben — "How to Build a Salesforce Account Hierarchy"
- **Publisher:** Salesforce Ben (independent Salesforce practitioner community, third-party)
- **Publication/update date:** Not explicitly dated in search result
- **URL:** https://www.salesforceben.com/how-to-build-a-salesforce-account-hierarchy/
- **Factual claim:** Native Salesforce account-hierarchy functionality is described as minimal — limited to the Account object's parent-child relationship and a finite number of nodes. Building a more usable hierarchy (e.g., a "Global Ultimate Parent" lookup and hierarchy-tier field, or a dedicated third-party hierarchy automation platform) requires custom fields or add-on tooling, not an out-of-the-box feature.
- **Meeting issue it connects to:** Victor's belief that "Salesforce may handle complex account hierarchies and custom pursuit objects more naturally" than HubSpot.
- **What it changes/confirms/deprioritizes:** This complicates rather than confirms Victor's claim — native Salesforce hierarchy support requires the same kind of custom-field or custom-object engineering work that HubSpot would also need. Worth raising at the next architecture review as a counterpoint to the "Salesforce is more natural" assumption.
- **Relevance score:** 3
- **Credibility/recency note:** Reputable independent Salesforce practitioner site, not an official Salesforce source, but consistent with Salesforce's own developer documentation on the topic. No AEC/engineering-specific data was found — a real gap this search did not close.
- **Human-review flag:** Major competitive claim

### 2. HubSpot Developers — "Developer updates for June 2026"
- **Publisher:** HubSpot (first-party developer changelog)
- **Publication/update date:** June 2026
- **URL:** https://developers.hubspot.com/changelog/june-2026-rollup
- **Factual claim:** HubSpot custom objects support many-to-many relationships beyond standard objects, enabling complex, multi-location account structures. An Enterprise-tier account is capped at 10 custom objects, and some HubSpot reporting, automation triggers, and email tools have limited support for custom objects. June 2026 updates added account-link/account-default/account-unlink capabilities for project-specific account associations.
- **Meeting issue it connects to:** The same hierarchy/custom-object comparison Victor raised, now from HubSpot's side.
- **What it changes/confirms/deprioritizes:** Confirms HubSpot can model complex hierarchies via custom objects, but with a real constraint — the 10-object cap and partial tool support — that SummitWorks (six offices, long pursuits, teaming partners) should test against its actual data model before assuming HubSpot can match a bespoke Salesforce build. Neither platform offers this "for free"; both require custom engineering.
- **Relevance score:** 3
- **Credibility/recency note:** First-party, dated June 2026 — current and high credibility.
- **Human-review flag:** Major competitive claim

### 3. HubSpot App Marketplace (SyncMatters listing) — "Deltek Vantagepoint Integration – iPaaS and Connector App for HubSpot"
- **Publisher:** SyncMatters (third-party integration vendor), listed on HubSpot's official App Marketplace
- **Publication/update date:** Not explicitly dated in search result
- **URL:** https://ecosystem.hubspot.com/marketplace/listing/deltek-vantagepoint-integration
- **Factual claim:** A marketplace-listed connector syncs project, client, and opportunity data between HubSpot and Deltek Vantagepoint, with configurable field mapping and no-code setup, intended to automate handoffs between sales, project management, and finance without manual re-entry.
- **Meeting issue it connects to:** Whether a "controlled integration" is feasible where HubSpot manages pursuit activity and approved project data flows to Deltek only after a defined stage.
- **What it changes/confirms/deprioritizes:** Confirms an existing, marketplace-vetted integration already exists rather than requiring a from-scratch custom build — this should reduce the perceived integration risk flagged in Stage 1 and gives Eli a concrete starting point for the "two integration patterns" he plans to present once the handoff checklist is approved.
- **Relevance score:** 3
- **Credibility/recency note:** Third-party vendor, but the listing is hosted and vetted on HubSpot's own App Marketplace — moderate-to-good credibility. Confirm the connector's exact stage-gating and field-mapping behavior directly with SyncMatters/Deltek before committing to it in the architecture review, since marketplace copy can overstate ease of setup.
- **Human-review flag:** None

### 4. HubSpot — "Quick Guide to Workflow Automation with HubSpot"
- **Publisher:** HubSpot (first-party product documentation)
- **Publication/update date:** Not explicitly dated (current live page as of 2026-07-28)
- **URL:** https://www.hubspot.com/products/workflow-automation-guide
- **Factual claim:** HubSpot workflows support webhook actions that send record data (e.g., a deal reaching a specific stage) to external systems — including ERP, billing, or project-management tools — in real time, enabling event-based, staged handoffs rather than only scheduled batch syncs.
- **Meeting issue it connects to:** Eli's plan to present "two integration patterns: scheduled synchronization and event-based handoff" once SummitWorks finalizes its handoff-checklist workflow document.
- **What it changes/confirms/deprioritizes:** Confirms the event-based handoff pattern is available today via native webhook workflow actions, not a hypothetical future capability — this should let Eli present it as a proven pattern at the next session, directly unblocking the sequencing the group agreed to (workflow document first, architecture second).
- **Relevance score:** 3
- **Credibility/recency note:** First-party HubSpot documentation for the core webhook mechanism — high credibility. A supplementary detail about "quote-based workflow triggers" came from a third-party blog (Vantage Point) and should be confirmed directly in-product before relying on it.
- **Human-review flag:** None

## Evidence sufficiency check

4 of 4 candidate sources scored 3. Sufficient decision-relevant evidence exists for this meeting's approved queries. One residual gap: no AEC/engineering-industry-specific account-hierarchy data was found for either platform — if that specificity matters to Victor, refine query 1 to something like `Salesforce account hierarchy case study architecture engineering construction firm`.
