> Part of the [GRC Toolkit](https://github.com/ebohc/grc-toolkit) — a broader collection of GRC artifacts.
>
>
> # Vendor Risk Assessment Framework

A practical, ready-to-use framework for scoring and managing third-party vendor risk.
Built on real GRC workflows — no expensive software required.

---

## Download the Template

**[Vendor Risk Assessment Template (Excel)](./Vendor_Risk_Assessment_Template.xlsx)**

Enter your vendors, score them across four factors, and get automatic risk ratings.
Formulas pre-loaded. Works in Excel and Google Sheets.

---

## What's in this repo

| Folder/File | What's inside |
|-------------|---------------|
| `Vendor_Risk_Assessment_Template.xlsx` | Excel risk register with auto-scoring |
| `samples/assessment.md` | Worked assessment example — Amazon AWS |
| `process/vendor-review-process.md` | Step-by-step vendor review workflow |

---

## How the scoring model works

Every vendor is scored across four factors:

| Factor | Column | Weight | Why |
|--------|--------|--------|-----|
| Data access | C | 40% | Drives the most breach impact |
| Integration depth | D | 30% | Determines how far a breach can spread |
| Business criticality | E | 20% | Operational exposure if vendor fails |
| Security posture | F | 10% | Certifications and questionnaire response |

Each factor is scored 1 (low risk) to 3 (high risk).
The template calculates a weighted score and assigns High, Medium, or Low automatically.

**Thresholds:**
- High — score 2.5 and above → quarterly review
- Medium — score 1.5 to 2.4 → annual review
- Low — below 1.5 → biennial review

---

## What the template includes

The Excel file has four tabs:

- **Vendor Risk Register** — live register with auto-calculated scores and portfolio summary
- **Scoring Guide** — complete 1–2–3 reference for every factor
- **Sample: Amazon AWS** — fully worked real-world assessment
- **Blank Template** — 30 rows ready for your own vendors

---

## Disclaimer

This repository contains sample assessments for educational and portfolio purposes only.
Where real-world vendors are referenced, assessments are based entirely on publicly
available information. No proprietary or confidential data is included.

---

## About

Built by a GRC practitioner for GRC practitioners.
If you find this useful, feel free to fork it, adapt it, or share it with your team.
