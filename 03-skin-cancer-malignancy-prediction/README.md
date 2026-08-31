# 🔬 Patient-Aware Metadata-Based Machine Learning for Skin Lesion Malignancy Prediction

> **Status:** 📤 Submitted — *Computers in Biology and Medicine* (Elsevier) · Currently with Editor  
> **Code & full details:** Will be released upon acceptance and publication.

**Authors:** Ali Mohammad Nasir Uddin *(Corresponding)* · Khandoker Momotaz Ferdouse  
**Affiliation:** Department of Computer Science and Engineering, IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh

![Status](https://img.shields.io/badge/Status-Submitted-orange)
![Journal](https://img.shields.io/badge/Journal-Elsevier-red)
![Domain](https://img.shields.io/badge/Domain-Medical%20AI%20%7C%20Tabular%20ML-blue)
![Task](https://img.shields.io/badge/Task-Skin%20Cancer%20Malignancy%20Prediction-lightblue)

---

## 📌 Overview

This paper presents an imaging-free machine learning framework for binary skin lesion malignancy prediction using only routine clinical metadata — no dermoscopic images, no CNN embeddings, no specialized imaging hardware required at any stage.

The work targets a real-world accessibility gap: dermoscopic imaging and trained dermatologists are unavailable in large parts of the world, yet routine clinical information such as patient demographics, lesion morphology, symptoms, and behavioral history is universally collectible. This study investigates how far that information alone can take a malignancy classifier.

---

## 🔬 Key Contributions

- A fully metadata-driven binary malignancy classification pipeline with strict patient-level leakage prevention across all preprocessing, cross-validation, threshold selection, and evaluation stages.
- Comprehensive benchmarking of seven classifiers and two late-fusion ensemble strategies under patient-aware stratified cross-validation and a locked held-out test partition.
- A held-out premalignant challenge evaluation: Actinic Keratosis (ACK) cases — a premalignant condition occupying an ambiguous biological position — are withheld from training and used as an independent challenge set to assess where they fall within the model's learned decision boundary. This analysis is not addressed in prior work on this dataset.
- A full reliability and interpretability suite: bootstrap confidence intervals, McNemar's test, probability calibration, decision curve analysis, conformal prediction uncertainty quantification, SHAP-based feature attribution, and feature group ablation.
- Structural missingness analysis identifying a strong association between a joint missing-data pattern and malignancy status, with implications for the interpretation and transportability of reported performance.

---

## 📦 Dataset

**PAD-UFES-20** — publicly available Brazilian skin lesion dataset  
> Pacheco et al. (2020). PAD-UFES-20: A skin lesion dataset composed of patient data and clinical images collected from smartphones. *Data in Brief*. [doi:10.1016/j.dib.2020.106221](https://doi.org/10.1016/j.dib.2020.106221)

Classification task: **Binary malignancy prediction** (Malignant: BCC, SCC, MEL · Benign: NEV, SEK)  
Challenge set (held-out): **Actinic Keratosis (ACK)** — premalignant, excluded from training

---

## 📄 Citation

```bibtex
@unpublished{nasir2025skinlesion,
  author      = {Ali Mohammad Nasir Uddin and Khandoker Momotaz Ferdouse},
  title       = {Patient-Aware Metadata-Based Machine Learning for Skin Lesion Malignancy Prediction},
  year        = {2025},
  note        = {Submitted, Computers in Biology and Medicine (Elsevier)},
  institution = {IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh}
}
```

---

## 💻 Code

Full code and results will be made publicly available in this repository upon acceptance and publication.

---

## 📬 Contact

**Ali Mohammad Nasir Uddin** *(Corresponding Author)*  
