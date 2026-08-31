# 🧠 Brain-CNNViT: Lightweight CNN-ViT Hybrid TinyML Framework for Brain Tumor Classification

> **Status:** 🔄 Under Peer Review — *Journal of Umm Al-Qura University for Medical Science* (Springer Nature)  
> **Code & full details:** Will be released upon acceptance and publication.

**Authors:** Khandoker Momotaz Ferdouse · Ali Mohammad Nasir Uddin *(Corresponding)*  
**Affiliation:** Department of Computer Science and Engineering, IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh

![Status](https://img.shields.io/badge/Status-Under%20Peer%20Review-yellow)
![Journal](https://img.shields.io/badge/Journal-Springer%20Nature-red)
![Domain](https://img.shields.io/badge/Domain-Medical%20AI%20%7C%20TinyML-blue)
![Task](https://img.shields.io/badge/Task-Brain%20Tumor%20Classification-lightblue)

---

## 📌 Overview

This paper presents **Brain-CNNViT**, a compact hybrid CNN–Vision Transformer architecture for four-class brain tumor classification from MRI, co-designed from the ground up for TinyML deployment on microcontroller-class hardware.

The work addresses a gap that is largely overlooked in the brain tumor classification literature: most high-performing deep learning models are designed for workstation- or cloud-scale compute, with no consideration of deployment feasibility on resource-constrained devices. Brain-CNNViT proposes a solution that jointly optimises for diagnostic accuracy, quantization robustness, and verified edge-deployment feasibility — within a strict sub-1 MB Flash and 512 KB SRAM budget.

---

## 🔬 Key Contributions

- A custom lightweight hybrid CNN–ViT architecture trained from scratch, designed to satisfy microcontroller-class memory constraints after full INT8 post-training quantization.
- Comprehensive benchmarking of four quantization regimes (FP32, Full INT8, Dynamic-Range, Float16) with static TFLite Micro footprint analysis confirming pre-deployment feasibility.
- Strict experimental design: 3-fold filename-derived grouped cross-validation, a held-out test split, and external validation on an independently acquired cohort to assess cross-dataset generalisability.
- Statistical equivalence testing (McNemar's test) confirming that INT8 quantization does not significantly alter the model's prediction behavior relative to the FP32 reference.
- Post-hoc explainability analysis using gradient-free methods compatible with quantized TFLite models.

---

## 📦 Datasets

Both datasets used are publicly available:

- **Hira Brain Tumor MRI Dataset** — [doi:10.17632/zwr4ntf94j.6](https://doi.org/10.17632/zwr4ntf94j.6) *(primary training and test)*
- **BRISC Dataset** — [doi:10.1038/s41597-026-06753-y](https://doi.org/10.1038/s41597-026-06753-y) *(independent external validation)*

Classification task: **Glioma · Meningioma · Pituitary · No-Tumor**

---

## 📄 Citation

```bibtex
@unpublished{ferdouse2025braincnnvit,
  author      = {Khandoker Momotaz Ferdouse and Ali Mohammad Nasir Uddin},
  title       = {Lightweight {CNN-ViT} Hybrid {TinyML} Framework for Brain Tumor Classification},
  year        = {2025},
  note        = {Under review, Journal of Umm Al-Qura University for Medical Science (Springer Nature)},
  institution = {IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh}
}
```

---

## 💻 Code

Full code, architecture details, and results will be made publicly available in this repository upon acceptance and publication.

---

**Ali Mohammad Nasir Uddin** *(Corresponding Author)*  

