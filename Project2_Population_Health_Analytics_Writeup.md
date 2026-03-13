# Project 2: Population Health Risk Stratification and 30-Day Readmission Analytics

**Employer:** Optum Canada | **Role:** Data Analyst, Population Health and Pharmacy Analytics
**Methods:** XmR Control Chart (High-Risk Outreach Completion Rate) + p-Chart (30-Day Readmission Rate)
**Tools:** Python (numpy, matplotlib), SPC, HQO Quality Improvement Plan Benchmarks, OptumIQ

---

## Business Context

Optum Canada's population health management platform stratifies commercial plan members and provincial program beneficiaries into risk tiers using claims, clinical, and social determinants data. Monthly outreach completion for high-risk members (rising-risk 42.4%, high-risk 28.4%, moderate 18.4%, stable 10.8%) and 30-day all-cause readmission rates are the primary population health KPIs aligned to Health Quality Ontario (HQO) Quality Improvement Plan benchmarks. This project applied SPC to 24 months of program data to detect assignable-cause variation and inform care management resource allocation.

---

## XmR Analysis: High-Risk Member Outreach Completion Rate (X-bar = 72.4%)

The Individual (X) chart tracked the monthly proportion of identified high-risk members receiving completed outreach contact (phone, virtual, or in-person) within the target care cycle. Control limits: X-bar ± 3σ (σ = MR-bar / 1.128).

**Out-of-Control Events:**

1. **Month 4 — COVID-19 Clinic Access Loss (below LCL, 62.2%):** Provincial COVID restrictions closed 68% of partner clinic sites used for in-person high-risk outreach. Outreach completion fell 10.2pp below X-bar. Response: telehealth outreach protocol deployed within 3 weeks, recovering completion to baseline by Month 6.

2. **Month 13 — OptumIQ Predictive Model v2.0 Deployment (above UCL, 82.8%):** The upgraded OptumIQ risk stratification model improved high-risk member identification precision by 34%, enabling care managers to prioritise outreach more effectively. Completion rate rose 10.4pp above X-bar — a sustained improvement signal confirmed over 4 consecutive months.

3. **Month 21 — Staffing Agency Contract Gap (below LCL, 61.8%):** A staffing agency contract renewal delay left 14 care manager positions unfilled for 6 weeks, reducing outreach capacity by 22%. Completion fell 10.6pp below X-bar. Corrective action: internal care manager cross-training programme established to reduce agency dependency.

---

## p-Chart Analysis: 30-Day All-Cause Readmission Rate (p-bar = 8.4%, n = 400/month)

The p-chart tracked the proportion of discharged high-risk members readmitted within 30 days. UCL/LCL: p-bar ± 3√(p-bar(1−p-bar)/n).

**Out-of-Control Events:**

1. **Month 6 — COVID Rapid Discharge Acceleration (above UCL, 12.8%):** COVID-era bed pressure protocols accelerated discharge of medically complex patients before optimal readiness, increasing readmission rate 4.4pp above UCL. The XmR outreach completion chart simultaneously showed a below-LCL signal (Month 4-6), confirming that reduced outreach and accelerated discharge were co-contributing to elevated readmissions.

2. **Month 14 — Enhanced Discharge Navigation Programme (below LCL, 4.4%):** Deployment of a structured discharge navigation programme — including pharmacist medication reconciliation, social work discharge planning, and 72-hour post-discharge phone follow-up — drove readmission rate 4.0pp below LCL. Sustained improvement confirmed over 6 consecutive months; the programme was expanded to two additional regions.

3. **Month 22 — Winter Respiratory Surge (above UCL, 13.4%):** A combined RSV, influenza A, and COVID wave drove a 5.0pp above-UCL readmission spike among high-risk respiratory patients (COPD, CHF). Corrective action: seasonal respiratory care pathway activated; proactive outreach frequency doubled for high-risk respiratory cohort during winter months.

---

## Key Findings & Impact

- High-risk outreach completion averaged 72.4% — the OptumIQ v2.0 precision improvement produced the largest sustained gain (+10.4pp), validating the business case for predictive model investment.
- Enhanced Discharge Navigation reduced 30-day readmission by 4.0pp — at the observed cohort volume of 400/month, this represents approximately 16 avoided readmissions per month or ~192 per year across the program.
- Cross-chart analysis confirmed that COVID-era outreach capacity reduction (XmR below-LCL) preceded readmission rate increase (p-chart above-UCL) by approximately 4 weeks — establishing a leading indicator relationship that now informs staffing contingency protocols.
- Findings presented at HQO Quality Improvement Collaborative; Enhanced Discharge Navigation programme adopted as a replicable model by two additional Ontario regional programs.
