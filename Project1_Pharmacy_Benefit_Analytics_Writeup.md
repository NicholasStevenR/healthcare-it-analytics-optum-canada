# Project 1: Pharmacy Benefit Management Generic Dispensing Analytics

**Employer:** Optum Canada | **Role:** Data Analyst, Population Health and Pharmacy Analytics
**Methods:** XmR Control Chart (Generic Dispensing Rate) + p-Chart (Prior Authorization Approval Rate)
**Tools:** Python (numpy, matplotlib), SPC, CADTH Reference Pricing, pCPA Policy Framework

---

## Business Context

Optum Canada's pharmacy benefit management (PBM) platform administers drug claims for employer group health plans and provincial supplementary benefit programs across Canada. The generic dispensing rate (GDR) and prior authorization (PA) approval rate are primary cost-quality KPIs aligned to CADTH reference pricing standards and pCPA negotiated listing criteria. This project applied SPC to 24 months of claims data spanning cardiovascular (28.4%), metabolic/endocrine (24.4%), CNS (22.4%), and respiratory (24.8%) drug classes.

---

## XmR Analysis: Generic Dispensing Rate (X-bar = 84.2%)

The Individual (X) chart tracked the monthly proportion of eligible drug claims dispensed as generics across all plan members. Control limits: X-bar ± 3σ (σ = MR-bar / 1.128).

**Out-of-Control Events:**

1. **Month 5 — Brand-Preferred Formulary Tier Change (below LCL, 74.8%):** A plan sponsor renegotiated a preferred formulary arrangement with a brand manufacturer, moving three high-volume statin molecules to preferred tier status. GDR fell 9.4pp below X-bar. Cost modelling identified a projected annual incremental cost of CAD 2.3M across the affected plan population.

2. **Month 13 — Generic Promotion Incentive Program (above UCL, 93.4%):** Deployment of an OptumRx point-of-sale generic substitution incentive — a CAD 0 copay for generic vs. CAD 15 for brand equivalents — drove GDR 9.2pp above X-bar. Sustained improvement confirmed over 5 consecutive months; annualised savings estimated at CAD 4.1M.

3. **Month 21 — GLP-1 Brand Surge (below LCL, 72.8%):** The rapid uptake of semaglutide (Ozempic/Wegovy) for both diabetes and weight management — with no generic equivalent available — drove a 11.4pp below-LCL signal. Analysis confirmed this was a structural formulary gap rather than a dispensing behaviour issue; results informed pCPA reference pricing submission timeline.

---

## p-Chart Analysis: Prior Authorization Approval Rate (p-bar = 88.4%, n = 600/month)

The p-chart tracked the proportion of PA requests approved within the defined SLA window. UCL/LCL: p-bar ± 3√(p-bar(1−p-bar)/n).

**Out-of-Control Events:**

1. **Month 6 — Biologic PA Criteria Tightened (below LCL, 83.2%):** Updated CADTH reimbursement criteria for three biologic drugs (adalimumab biosimilars, dupilumab) introduced more stringent step-therapy requirements. Approval rate fell 5.2pp below LCL as the PA team worked through backlog of applications not meeting new criteria. Action: updated PA decision support templates deployed within 3 weeks.

2. **Month 14 — PA Workflow Automation (above UCL, 94.2%):** Implementation of OptumRx AI-assisted PA triage — automatically approving requests meeting defined clinical criteria — reduced median PA decision time from 48 hours to 6 hours and drove approval rate 5.8pp above UCL. Confirmed as a sustained process improvement signal.

3. **Month 22 — GLP-1 Volume Surge Backlog (below LCL, 83.4%):** The semaglutide volume surge that depressed GDR also generated a PA request backlog — a 340% increase in GLP-1 PA submissions within 8 weeks. Approval rate fell 5.0pp below LCL. Response: dedicated GLP-1 PA review team established; queue cleared within 4 weeks.

---

## Key Findings & Impact

- GDR averaged 84.2% — the generic incentive programme produced the largest single sustainable gain (+9.2pp), with estimated annualised savings of CAD 4.1M across the plan population.
- GLP-1 brand surge caused simultaneous GDR and PA approval rate below-LCL events — demonstrating how SPC can surface correlated process failures across different KPI streams from a single root cause.
- PA automation reduced decision time by 87.5% (48h to 6h), improving member experience and reducing pharmacist labour by an estimated 1,200 hours/year.
- SPC findings presented to three plan sponsor advisory groups; GLP-1 formulary gap analysis fed directly into the 2024 pCPA reference pricing submission.
