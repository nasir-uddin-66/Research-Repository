# 🫀 Missingness-Aware Domain Generalization for Cross-Site Cardiovascular Disease Prediction

> **Status:** 🔧 Early-Stage Research — Baseline experiments completed, proposed method under development

**Researcher:** Ali Mohammad Nasir Uddin  
**Affiliation:** Department of Computer Science and Engineering, IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh

![Status](https://img.shields.io/badge/Status-Early%20Stage-orange)
![Domain](https://img.shields.io/badge/Domain-Clinical%20ML%20%7C%20Domain%20Generalization-blue)
![Task](https://img.shields.io/badge/Task-Cardiovascular%20Disease%20Prediction-red)

---

## 📌 Overview

Most cardiovascular disease prediction models are evaluated using random train/test splits — a protocol that allows patients from the same clinical site to appear in both training and testing. While this typically produces high reported accuracy, it can mask a fundamental problem: the model may fail when applied to a completely new clinical site it has never seen during training.

This research investigates that gap directly. Using four clinical sites from the UCI Heart Disease collection as independent domains, the study evaluates how well cardiovascular disease models generalize to **entirely unseen clinical environments** — and whether explicitly modeling site-specific missing-data patterns can improve both discrimination and calibration under this harder evaluation.

---

## 🔬 Research Question

> *Does explicitly modeling site-specific missingness patterns as an auxiliary domain signal, combined with calibration-aware domain-generalization training, improve both discrimination and calibration when cardiovascular disease models are evaluated on completely unseen clinical sites?*

---

## 🔑 Key Motivation

Preliminary experiments reveal a substantial gap between conventional random-split performance and Leave-One-Site-Out (LOSO) evaluation — where the model is tested on a clinical site it has never seen during training. This gap motivates the core research question.

Beyond discrimination, calibration under site shift is equally important: a model can retain moderate ranking ability while producing unreliable probability estimates on an unseen population — a critical failure mode for clinical risk stratification.

---

## 📦 Dataset

**UCI Heart Disease Dataset** — four processed clinical sites used as independent domains:

| Site | N | Notes |
|---|---|---|
| Cleveland | 303 | Low missingness |
| Hungary | 294 | Moderate missingness |
| Switzerland | 123 | High missingness · extreme disease prevalence |
| VA Long Beach | 200 | Highest missingness · hardest generalization target |

**Total:** N = 920 harmonized records · Binary classification: disease present / absent

> Note: The dataset contains site-specific differences in disease prevalence, feature distributions, and missingness patterns — making it a meaningful multi-domain benchmark for generalization research.

---

## 🔬 Research Direction

The proposed framework investigates **missingness-aware domain generalization**, combining:

- Explicit modeling of site-specific missing-data patterns as auxiliary signals
- Domain generalization training to improve robustness on unseen clinical sites
- Post-hoc probability calibration for reliable risk estimates

Evaluation follows **Leave-One-Site-Out (LOSO)** — each site is held out entirely as an unseen test domain while the model trains on the remaining three sites.

---

## 📍 Current Stage

- ✅ Dataset audit and harmonization
- ✅ Baseline conventional ML experiments (Random Split and LOSO)
- ✅ Missingness analysis and calibration analysis across sites
- ✅ Initial literature review and research gap identification
- 🔧 Proposed method design and implementation *(in progress)*
- ⬜ Ablation study
- ⬜ Statistical comparison and uncertainty analysis
- ⬜ Paper writing

---

## 💻 Code

Code and notebooks will be made publicly available upon completion of the research.

---

## 📬 Contact

**Ali Mohammad Nasir Uddin**  
BSc in Computer Science and Engineering, IUBAT  
📧 22103395@iubat.edu  
🔗 [LinkedIn](#) · [ResearchGate](#)
