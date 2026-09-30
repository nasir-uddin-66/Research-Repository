# 🔍 Data Leakage and Undisclosed Provenance in Public Brain Tumor MRI Datasets: A Systematic Audit

> **Status:** 📝 Manuscript Complete · Preparing for journal submission  
> **Full methodology & results:** Will be released upon publication.

**Authors:** Ali Mohammad Nasir Uddin *(Corresponding)* · Khandoker Momotaz Ferdouse  
**Affiliation:** Department of Computer Science and Engineering, IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh

![Status](https://img.shields.io/badge/Status-Manuscript%20Complete-blueviolet)
![Domain](https://img.shields.io/badge/Domain-Medical%20AI%20%7C%20Data--Centric%20AI-blue)
![Task](https://img.shields.io/badge/Task-Dataset%20Integrity%20Audit-lightblue)
![Datasets](https://img.shields.io/badge/Datasets%20Audited-7-green)
![Images](https://img.shields.io/badge/Images%20Audited-34%2C525-green)

---

## 📌 Overview

Brain tumor MRI classification studies routinely report accuracies above 99%. But most public datasets in this domain trace, directly or indirectly, to a single 2015 source collection — and they are frequently combined, cross-validated, or used as "independent" external test sets without accounting for that shared origin.

This work does not propose a new classifier. Instead, it audits **the data that classifiers in this field are evaluated on**, asking whether the benchmarks behind headline accuracy numbers are as independent and leakage-free as they are assumed to be.

---

## ❓ Research Questions

1. **Internal leakage** — Do widely used datasets with predefined train/test splits contain duplicate or near-duplicate images across those splits?
2. **Cross-dataset overlap** — How much image-level overlap exists between datasets that researchers routinely treat as independent, and does it match what each dataset's documentation discloses?
3. **Cost of image-level splitting** — On data where patient identity is recoverable, how much does the common practice of image-level splitting inflate reported accuracy compared with a strict patient-level split?

---

## 📊 Headline Findings

- **Internal leakage is common.** Measurable train/test leakage was found in 3 of the 4 audited datasets that ship predefined splits — including a peer-reviewed dataset and one explicitly described as leakage-free.
- **"Independent" datasets are not independent.** Cross-dataset image overlap of roughly **11–76%** was found between datasets commonly used together, spanning the full spectrum of provenance disclosure.
- **Split methodology alone moves the numbers.** On identical data, image-level splitting produced **~4.3 percentage points higher accuracy** than patient-level splitting — a figure that likely *understates* total inflation once cross-dataset overlap is considered.
- **Detection is validated.** Cross-dataset matches were confirmed by a blind two-rater manual review with perfect agreement (Cohen's κ = 1.00).

---

## 🔬 Contributions

- A quantitative audit of internal train/test leakage across seven widely used brain tumor MRI datasets.
- A cross-dataset provenance analysis mapping undisclosed overlap across the dataset ecosystem, with independent manual validation.
- A controlled experiment isolating the effect of image-level vs. patient-level splitting on reported model performance.
- A practical **checklist for dataset creators and downstream researchers** to prevent the failure modes identified.
- A released image-level manifest and detection pipeline to support future audits.

---

## 📦 Datasets Audited

Seven publicly available brain tumor MRI datasets (34,525 images total), grouped by how clearly they disclose their provenance:

| Dataset | Images | Classes | Provenance category |
|---|---|---|---|
| Figshare (Cheng et al., 2015) | 3,064 | 3 | Anchor source |
| Nickparvar (Kaggle) | 7,200 | 4 | Disclosed derivation |
| BRISC | 6,000 | 4 | Disclosed derivation |
| Sartaj (Kaggle) | 3,264 | 4 | No external source stated |
| Br35H (Kaggle) | 3,000 | 2 | No external source stated |
| Rahman (Mendeley Data) | 6,056 | 3 | Stated clinical collection |
| BDNeuro-MRI (Mendeley Data) | 5,941 | 4 | Stated clinical collection |

---

## 🎯 Why It Matters

- Reported performance in this literature should be interpreted with caution, **independent of any individual study's methodology**.
- Combining named datasets does **not** automatically constitute independent validation.
- The field lacks routine data-curation tooling to verify dataset independence before publication — this work proposes a starting point.

> The aim is diagnostic, not adversarial: the findings point to a structural gap in tooling and convention, not to bad faith by any dataset creator or researcher.

---

## 💻 Code & Data

The image-level manifest and analysis code are available in the companion repository:
**[nasir-uddin-66/Brain-Tumor-Leakage-Audit](https://github.com/nasir-uddin-66/Brain-Tumor-Leakage-Audit)**

The audited datasets are publicly available from their original sources.

---

## 📄 Citation

```bibtex
@unpublished{nasir2026leakageaudit,
  author      = {Ali Mohammad Nasir Uddin and Khandoker Momotaz Ferdouse},
  title       = {Data Leakage and Undisclosed Provenance in Public Brain Tumor {MRI} Datasets: A Systematic Audit},
  year        = {2026},
  note        = {Manuscript in preparation},
  institution = {IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh}
}
```

---

[← Back to Research Portfolio](../README.md)
