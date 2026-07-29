# Stage 1 Query Plan — Meeting Signal Inventory & Search-Term Brainstorm

**Written:** 2026-07-29, filling a documentation gap. Both `03_Live_Research/stage1_grasp_brief.md` and `03_Live_Research/stage1_signoff.md` reference this file (originally as `meeting_signal_inventory.docx`) as the approved query plan that Stage 1's live searches were run against — but the file was never actually committed to the repo. This is a straight reconstruction, not a re-run: for each meeting, it names the specific signal in the notes that made a generic search inadequate, states the weak/naive query someone might default to, and shows the sharpened query that was actually used in the corresponding `03_Live_Research/NN_research_evidence.md` file. The sharpened queries below are not new — they're pulled verbatim from the "Exact queries run" section of each evidence file. What's new is making visible *why* each one looks the way it does, rather than leaving that judgment implicit in the final query list.

The extension references in `stage1_grasp_brief.md` and `stage1_signoff.md` (`.docx` → `.md`) are corrected to point here as part of this fix.

---

## Meeting 01 — Northstar Advisory Discovery

**Signal:** Priya's board member saw a **Salesforce Agentforce** demo and asked why Northstar isn't using an AI agent for prospecting. Dana won't buy an "expensive add-on" before data is cleaned, and specifically worries about migrating **Pipedrive, Mailchimp, and Zendesk**.

**Weak version:** `AI features in CRM software`

**Sharpened (actually run):**
1. `Salesforce Agentforce prospecting and account-research capabilities 2026`
2. `HubSpot Breeze AI agent features for prospecting vs. Salesforce Agentforce`
3. `HubSpot migration tools for importing Pipedrive, Mailchimp, and Zendesk data`
4. `HubSpot Breeze AI agent add-on pricing 2026`

**Why:** a generic AI/CRM search returns marketing overviews for every vendor. Naming Salesforce's specific product (Agentforce, not "Salesforce AI") answers the exact question the board member's demo raised; naming Northstar's three actual tools instead of "CRM migration" surfaces whether *these specific* migrations are supported, not migration in general.

## Meeting 02 — Meridian Staffing Competitive Evaluation

**Signal:** Carlos is comparing **Microsoft Dynamics 365 Copilot**; Lynn wants AI outreach governed **by role and approved templates**, not just "reviewed"; Meridian keeps **Bullhorn** for candidates; duplicate employer records and national-account ownership are a named 18-office pain point.

**Weak version:** `CRM for staffing companies`

**Sharpened (actually run):**
1. `Microsoft Dynamics 365 Copilot sales-agent features 2026`
2. `HubSpot approval workflows for AI-generated sales outreach by role`
3. `HubSpot Bullhorn ATS integration for staffing and recruiting agencies`
4. `HubSpot duplicate-record management for multi-office account ownership`

**Why:** "CRM for staffing companies" would surface generic staffing-tech listicles, not Bullhorn specifically. Naming Bullhorn directly, and "by role" rather than just "approval workflows," is what later let the pipeline correctly score query 2's actual result as only partially relevant (Test 2 in `tests/validation_note.md` picks this exact gap back up).

## Meeting 03 — Harborline Legal Security Workshop

**Signal:** Owen wants **role-based access, audit logging, data-retention, and AI data-usage** specifics, not general security marketing. Harborline is comparing **Zoho** on price without a security comparison yet.

**Weak version:** `CRM security features for law firms`

**Sharpened (actually run):**
1. `HubSpot role-based access controls and audit logging documentation`
2. `HubSpot AI features: customer data usage and training policy`
3. `Zoho CRM security certifications and compliance documentation for professional services`
4. `Zoho One bundled pricing 2026 vs. HubSpot for small law firms`

**Why:** Owen's list (access, audit, retention, AI data handling) is four distinct claims, not one — a single "security features" search would have returned an overview page that glosses all four instead of documentation specific enough to actually answer his questionnaire. Naming Zoho directly targets the exact comparison the firm is already making internally.

## Meeting 04 — SummitWorks Engineering Integration

**Signal:** Victor thinks **Salesforce** may handle **custom objects and account hierarchies** better; finance runs **Deltek Vantagepoint** and won't accept a shadow ERP; the group is choosing between **scheduled sync and event-based handoff**.

**Weak version:** `CRM for engineering firms`

**Sharpened (actually run):**
1. `Salesforce custom objects and account hierarchy capabilities for engineering and AEC firms`
2. `HubSpot custom objects and account hierarchy support 2026`
3. `HubSpot Deltek Vantagepoint integration options`
4. `HubSpot event-based workflow triggers for staged handoff to an external ERP`

**Why:** "CRM for engineering firms" answers nothing about the actual blocker, which is a specific technical capability (custom objects/account hierarchies) and a specific named ERP (Deltek Vantagepoint). Naming the integration *pattern* (event-based vs. scheduled) instead of just "integration" targets the exact unresolved design question Ben and Eli were left with.

## Meeting 05 — BrightPath Training Procurement

**Signal:** Devon asked specifically about **HubSpot's Revenue Hub** and the CRM/quote-to-cash boundary, and is comparing **Zoho One** as cheaper. Reese wants attribution from **webinar registration through renewal** specifically.

**Weak version:** `HubSpot pricing`

**Sharpened (actually run):**
1. `HubSpot Revenue Hub current pricing and packaging 2026`
2. `HubSpot Revenue Hub quote-to-cash and payment collection features`
3. `Zoho One pricing 2026 for training and education businesses`
4. `HubSpot marketing attribution reporting from webinar registration to renewal`

**Why:** "HubSpot pricing" alone is too broad to answer Devon's actual question, which was about one specific product (Revenue Hub) and one specific functional boundary (quote-to-cash vs. CRM). Reese's attribution ask is similarly specific to a named funnel (webinar → renewal), not attribution reporting in general.

## Meeting 06 — BluePeak RevOps Partner

**Signal:** Simone wouldn't promise specifics without confirming **current partner-program terms**; Alana is blocked on **certification time and delivery capacity**; Greg's economics question is about **co-selling/referral margin**.

**Weak version:** `HubSpot partner program`

**Sharpened (actually run):**
1. `HubSpot Solutions Partner Program tiers and requirements 2026`
2. `HubSpot partner certification time and training requirements`
3. `HubSpot partner co-selling and referral margin structure`

**Why:** a single "partner program" search returns marketing/recruitment copy, not the three separate things actually asked about in the room — program tiers/requirements (Simone), certification time (Alana), and margin structure (Greg). Splitting the query into three matches the three separate owners who each need a different specific answer.

## Meeting 07 — NABC Association Partnership

**Signal:** Elena wants content on AI + **referral-based selling and proposal development** specifically, for **boutique/small consulting firms** — not enterprise AI content. Mark and Jules need **member-data consent standards for a sponsored webinar**, not general privacy law.

**Weak version:** `AI in professional services`

**Sharpened (actually run):**
1. `AI adoption in referral-based business development for small professional-services firms`
2. `Data-readiness challenges for AI-assisted proposal development in consulting firms` *(run twice — first attempt returned enterprise-scale AI-readiness content aimed at large firms; second attempt narrowed explicitly to boutique/referral-selling context)*
3. `Association member-data consent standards for vendor-sponsored webinars`

**Why:** this is the one query in the whole set that had to be corrected mid-search rather than getting it right on the first sharpened attempt — a general "AI-readiness for consulting firms" search still skewed toward large-firm content, so it had to be narrowed a second time to boutique/referral-selling specifically once the first result set came back off-target. Query 3 is sharpened to the exact governance question raised (member data, *sponsorship*, consent) rather than data privacy generally, which would have returned GDPR/CCPA overview content with no association-specific relevance.

## Meeting 08 — Finley Growth Capital Portfolio

**Signal:** Marcus favors Microsoft because portfolio companies are **Azure-standardized** with embedded **Copilot**; Lauren wants a **transparent exit path / data portability**, explicitly to avoid lock-in; pilot companies are **under 150 employees**.

**Weak version:** `CRM for private equity portfolio companies`

**Sharpened (actually run):**
1. `Microsoft Dynamics 365 Copilot sales-agent capabilities 2026 for Azure-standardized companies`
2. `HubSpot data export and API access for CRM offboarding`
3. `HubSpot implementation time and administrative effort for companies under 150 employees`

**Why:** "CRM for PE portfolios" would return generic multi-entity-CRM thought leadership, not Marcus's actual Azure/Copilot rationale or Lauren's specific lock-in concern. Naming "offboarding" instead of "data portability" targets Lauren's exact worry (can we leave cleanly) rather than the more common but less relevant question of importing data in.
