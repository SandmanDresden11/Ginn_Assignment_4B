# 03 — Harborline Legal Security Workshop: Live Research Evidence

**Search date:** 2026-07-28
**Classroom simulation note:** HubSpot is the only real organization. Harborline, its staff, and all commercial details are invented for this exercise.

## Exact queries run

1. `HubSpot role-based access controls and audit logging documentation`
2. `HubSpot AI features: customer data usage and training policy`
3. `Zoho CRM security certifications and compliance documentation for professional services`
4. `Zoho One bundled pricing 2026 vs. HubSpot for small law firms`

## Candidate sources

### 1. HubSpot — "Security and Compliance"
- **Publisher:** HubSpot (first-party trust center)
- **Publication/update date:** Not explicitly dated (current live page as of 2026-07-28)
- **URL:** https://www.hubspot.com/security-and-compliance
- **Factual claim:** HubSpot's permissions model is role-based, covering users, teams, CRM objects, properties, audit logs, and security settings at a granular level. Login history, security-activity, and content-activity logs can be reviewed in-platform or exported to a SIEM/log-analysis tool, and Super Admins can enforce 2FA and review posture through a Security Center.
- **Meeting issue it connects to:** Owen's explicit request for "role-based access, auditability, data-retention controls."
- **What it changes/confirms/deprioritizes:** Confirms the core access-control and audit-log capability Owen asked about exists natively, which should be reflected in Rachel's governance-first demo and Owen's July 22 security questionnaire response.
- **Relevance score:** 3
- **Credibility/recency note:** First-party trust center — high credibility for capability claims, though self-published; confirm current SIEM-export options are enabled on Harborline's target plan/tier before the demo.
- **Human-review flag:** Security

### 2. HubSpot Knowledge Base — "Opt out of HubSpot's AI model training"
- **Publisher:** HubSpot (first-party product documentation)
- **Publication/update date:** Not explicitly dated (current live article)
- **URL:** https://knowledge.hubspot.com/account-management/hubspot-ai-mode-training
- **Factual claim:** By default, HubSpot may use customer data to train its own AI models; customers can opt out via account settings, a change that takes up to one week to fully apply and does not restrict access to AI features. Third-party AI providers (e.g., OpenAI) are contractually barred from using customer data to train their own models, and HubSpot applies zero data retention and data masking before third-party AI processing.
- **Meeting issue it connects to:** Owen's request for "a clear explanation of how AI features use customer data" — the central governance question for this workshop.
- **What it changes/confirms/deprioritizes:** This is the most decision-relevant finding for Harborline: the **default** setting permits HubSpot to use customer data (which could include client-related business-development notes) for its own AI model training unless the firm proactively opts out. For a law firm managing privileged-adjacent information, this default should be surfaced explicitly — and the opt-out toggled — before any pilot begins, not left as an assumption.
- **Relevance score:** 3
- **Credibility/recency note:** First-party, directly on point, and specific — high credibility. No opt-out timing shortcuts should be assumed; verify current toggle location in-product before the workshop.
- **Human-review flag:** Security; Legal/regulatory

### 3. Zoho — "Compliance at Zoho"
- **Publisher:** Zoho Corporation (first-party trust page)
- **Publication/update date:** Not explicitly dated (current live page as of 2026-07-28)
- **URL:** https://www.zoho.com/compliance.html
- **Factual claim:** Zoho states ISO 27001, ISO 27017, and ISO 27018 certification, and SOC 2 Type II compliance across Security, Confidentiality, Processing Integrity, Availability, and Privacy, with annual audits; it also lists support for HIPAA, GDPR, CSA STAR, and PCI frameworks, plus AES-256 encryption, audit logs, IP restrictions, and two-factor authentication.
- **Meeting issue it connects to:** "The firm is also looking at Zoho because its bundled pricing appears lower, but no one has completed a security comparison."
- **What it changes/confirms/deprioritizes:** Directly enables the missing security comparison the group flagged. On paper, Zoho's certifications (SOC 2 Type II, ISO 27001/27017/27018) are comparable to what a mainstream CRM vendor would present — meaning Harborline's cost-vs-security tradeoff is likely **not** a "Zoho has weaker security" story, but a question of specific control granularity (e.g., property-level access, audit-log export options) that needs a feature-by-feature comparison, not a certification-only comparison.
- **Relevance score:** 3
- **Credibility/recency note:** First-party, self-reported trust page — standard for vendor compliance pages but not independently audited within this search; if this comparison goes into a client-facing document, request current SOC 2 report attestation dates from both vendors rather than relying on the marketing page alone.
- **Human-review flag:** Security; Legal/regulatory

### 4. Forbes Advisor — "HubSpot Vs. Zoho CRM (2026 Comparison)"
- **Publisher:** Forbes Advisor (editorial buying-guide vertical, third-party)
- **Publication/update date:** 2026
- **URL:** https://www.forbes.com/advisor/business/software/hubspot-vs-zoho/
- **Factual claim:** Comparison sources in this space generally describe Zoho One as a lower-cost bundled offering relative to HubSpot's per-seat Professional-tier pricing, though the exact price points cited vary across outlets and were not independently confirmed against Zoho's or HubSpot's own current pricing pages in this search.
- **Meeting issue it connects to:** Harborline's belief that "Zoho's bundled pricing appears lower" than HubSpot.
- **What it changes/confirms/deprioritizes:** Directionally supports the premise that Zoho is priced lower, but the specific dollar figures are not yet verified against primary sources, so this should not be quoted to Harborline as a precise number.
- **Relevance score:** 2 — directional context only; not yet reliable enough to change the pricing conversation on its own.
- **Credibility/recency note:** Third-party comparison/affiliate-style content; treat specific price figures as unverified until checked against zoho.com/one and hubspot.com/pricing directly.
- **Human-review flag:** Pricing

## Evidence sufficiency check

3 of 4 candidate sources scored 3 (HubSpot access/audit controls, HubSpot AI data-training policy, Zoho compliance certifications). The pricing query returned only directional, unverified figures (score 2). **Recommend refining this query** to pull directly from primary pricing pages, e.g. `site:zoho.com Zoho One pricing plans` and `site:hubspot.com pricing professional tier`, before citing specific dollar amounts to Harborline.
