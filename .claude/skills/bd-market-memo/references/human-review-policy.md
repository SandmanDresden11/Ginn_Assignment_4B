# Human Review Policy

This skill never resolves the categories below on its own — it flags them and routes them to a human. This file defines each category so flagging is consistent.

## Why this exists

A memo that quietly states a pricing figure, a security posture claim, a legal conclusion, or a head-to-head competitive claim as settled fact creates real risk if it's wrong, stale, or shared externally without a second look. Flagging costs one line; an unflagged bad claim costs a client relationship or a compliance incident. When in doubt, flag it.

## Flag categories

### Pricing

Any dollar figure, discount, tier name/threshold, promotional rate, effective/expiration date for a rate, or partner/commission economics.

*Examples:* "$95/user/month Professional tier," "promotional rate expires September 2026," "20% partner commission for 3 years."

*Why flagged:* prices change without notice, promotional pricing has expiration dates, and quoting a stale or unverified number externally can create a commitment the company didn't intend to make.

### Security

Any claim about access control, permissions, audit logging, data retention, encryption, authentication, or overall security/trust posture — for the vendor's own platform or a competitor's.

*Examples:* "role-based access down to the property level," "SOC 2 Type II across five trust categories," "AI features apply zero data retention before third-party processing."

*Why flagged:* security claims are exactly the kind of thing a prospect will hold the company to; self-reported vendor claims (including HubSpot's own) should be confirmed against the prospect's actual required tier/configuration, not assumed from marketing copy.

### Legal/regulatory

Any claim touching data protection law (GDPR, CCPA, etc.), consent requirements, compliance certifications treated as legal sufficiency, or regulatory exposure.

*Examples:* "opt-out required for AI model training on customer data," "member data requires explicit consent under GDPR/CCPA before sharing with a sponsor."

*Why flagged:* this skill is prohibited from providing legal advice. A legal/regulatory claim in a memo is *evidence for counsel to review*, not a conclusion the BD team can act on unassisted — especially for regulated-adjacent prospects (law firms, associations handling member PII, etc.).

### Major competitive claim

Any claim comparing the vendor's capability, pricing, or positioning to a **named competitor** (Salesforce, Microsoft/Dynamics 365, Zoho, etc.), in either direction.

*Examples:* "Agentforce requires Data Cloud configuration and higher license spend, unlike HubSpot's embedded agents," "native Salesforce account hierarchies are actually as limited as HubSpot's."

*Why flagged:* competitive claims are often sourced from vendor marketing (promotional, not independently verified) or from consultancies with a commercial stake in one platform. These claims are also the most likely to be quoted directly back to a board or decision committee, so they need verification before that happens.

## How to flag in the memo

- Flag at the **claim** level. If one source contains both a flagged claim and ordinary/unflagged content, only the flagged claim needs the callout — don't blanket-flag an entire source if only part of it is sensitive.
- A claim can carry more than one flag (e.g., a source about AI training on customer data for a law firm is both **Security** and **Legal/regulatory**).
- Every flagged claim gets a checklist line in the memo's **Human Review Required** section (see output-schema.md), not just an inline tag — the flag must be actionable, not decorative.
- Never resolve the flag yourself by picking a side, confirming a number is current, or issuing a legal conclusion. Route it.

## What this does NOT cover

Routine product-capability claims with no pricing, security, legal, or named-competitor angle (e.g., "HubSpot's Smart Transfer supports importing from Pipedrive") don't need a human-review flag — they still need a source citation (title/publisher/date/URL), just not the escalation checklist treatment.
