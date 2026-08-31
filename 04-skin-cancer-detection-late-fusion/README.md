# 🔬 Multimodal Skin Lesion Triage: CNN-Transformer + Clinical Metadata Fusion

> **Status:** 🔧 Work in Progress

**Researcher:** Ali Mohammad Nasir Uddin  
**Affiliation:** Department of Computer Science and Engineering, IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh

![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-orange)
![Domain](https://img.shields.io/badge/Domain-Medical%20AI%20%7C%20Multimodal%20Learning-blue)
![Task](https://img.shields.io/badge/Task-Skin%20Lesion%20Malignancy%20Triage-lightblue)

---

## 📌 Overview

This project explores a dual-stream multimodal framework for binary skin lesion malignancy
triage, combining smartphone-captured clinical images with structured patient metadata.
Rather than relying on a single modality, the system integrates a hybrid CNN-Transformer
visual classifier with a calibrated gradient-boosted metadata model, fused at the decision
level.

The work is motivated by a real accessibility gap: most automated skin cancer systems
depend on high-fidelity dermoscopic imaging unavailable in primary care or low-resource
settings. This framework is designed to work with smartphone photographs and routine
clinical data alone.

---

## 🔬 Research Focus

- Dual-stream architecture combining image and clinical metadata streams
- Patient-level data partitioning to prevent leakage across train/validation/test splits
- Decision-level late fusion with probability calibration
- Clinically motivated threshold selection to prioritise sensitivity over specificity
- Explainability via Grad-CAM (image stream) and SHAP (metadata stream)

---

## 📦 Dataset

**PAD-UFES-20** — publicly available Brazilian clinical skin lesion dataset  
> Pacheco et al. (2020). *Data in Brief*. [doi:10.1016/j.dib.2020.106221](https://doi.org/10.1016/j.dib.2020.106221)

---

## 💻 Code

Code will be made publicly available upon completion.

---

## 📬 Contact

**Ali Mohammad Nasir Uddin**  
BSc in Computer Science and Engineering, IUBAT  
📧 22103395@iubat.edu  
🔗 [LinkedIn](#) · [ResearchGate](#)
