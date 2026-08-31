# 🧠 Edge-Deployable TinyML Framework for Breast Cancer Detection with Explainable AI from DCE-MRI

> **Bachelor's Thesis** · Department of Computer Science and Engineering
> IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh · Fall 2025

**Authors:** Ali Mohammad Nasir Uddin · Khandoker Momotaz Ferdouse
**Supervisor:** Abdullah Mohammad Sakib, Lecturer, Dept. of CSE, IUBAT

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow)
![TFLite](https://img.shields.io/badge/TFLite-Quantized-green)
![XAI](https://img.shields.io/badge/XAI-LIME-purple)
![Accuracy](https://img.shields.io/badge/Test%20Accuracy-97.0%25-brightgreen)
![Model Size](https://img.shields.io/badge/Model%20Size-%3C5MB-lightblue)

---

## 📌 Overview

Breast cancer is among the leading causes of cancer-related mortality in women worldwide. While Dynamic Contrast-Enhanced MRI (DCE-MRI) offers high diagnostic sensitivity, most deep learning models are too computationally heavy for real-world clinical deployment — especially in low-resource settings such as rural hospitals or mobile screening units.

This thesis proposes a solution at the intersection of three underexplored challenges:

| Challenge | This Work's Answer |
|---|---|
| High model complexity | Custom lightweight CNN-ViT hybrid (~2.3M params) |
| Edge deployment barrier | Post-training quantization → **< 5 MB** model |
| Explainability after quantization | Gradient-free **LIME**-based XAI |

The result: a **97% accurate**, **2.38 MB**, **interpretable** breast cancer detector that runs on TinyML-class devices — without any pretrained backbone.

---

## 🔬 What Makes This Work Novel

1. **Fully custom CNN-ViT hybrid** — designed from scratch (no ImageNet pretraining), tuned for the intensity distribution of pre-contrast MRI.
2. **Pre-contrast T1-weighted MRI only** — avoids gadolinium contrast agents, lowering patient risk and cost, while still achieving high accuracy.
3. **Quantization without accuracy loss** — DRQ model actually *improves* over FP32 (97.0% vs 96.5%), consistent with recent findings that quantization acts as implicit regularization.
4. **LIME on a quantized TFLite model** — gradient-based methods (Grad-CAM, SHAP) break on quantized models; this work applies a model-agnostic approach that works post-quantization.
5. **End-to-end TinyML pipeline** — from raw MRI slices to an edge-deployable, explainable classifier under 5 MB.

---

## 🏗️ Architecture

```
Input MRI Slice (512×512×3)
         │
         ▼
┌─────────────────────────────┐
│  Convolutional Feature      │  4 residual CNN stages
│  Extractor                  │  Channels: 32 → 64 → 128 → 256
│  (Local texture & edges)    │  MaxPooling → 32×32×256
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Patch Extraction &         │  Non-overlapping P×P patches
│  Linear Embedding           │  Dense projection → 128-D
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  CLS Token + Positional     │  Learnable [CLS] prepended
│  Embeddings                 │  Trainable position encoding
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Transformer Encoder × 3    │  Pre-LN architecture
│  (Global context modeling)  │  4-head MHSA
│                             │  MLP dim 256, GELU
│                             │  Residual + Dropout
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Classification Head        │  LN → Dense(128) → Dense(64)
│                             │  → Dense(1) + Sigmoid
└────────────┬────────────────┘
             │
             ▼
      Binary Prediction
   (Tumor Present / Absent)
```

**Total parameters:** ~2.3M · **Optimizer:** Adam + Binary Cross-Entropy + Label Smoothing (ε=0.03) · **LR Schedule:** Warmup-cosine decay · **Regularization:** L2 + Dropout + Early Stopping

---

## 📦 Dataset

**Duke Breast Cancer MRI Dataset** — [The Cancer Imaging Archive (TCIA)](https://doi.org/10.7937/TCIA.e3sv-re93)

| Split | Samples | Class Balance |
|---|---|---|
| Training | 4,000 | 50% positive / 50% negative |
| Validation | 400 | Balanced |
| Test | 400 | Balanced |

- **300 patients** · Axial pre-contrast T1-weighted slices only
- **Positive slices:** confirmed by lesion bounding boxes
- **Negative slices:** ≥ 8 slices away from any tumor-containing slice (minimizes label contamination)
- **Preprocessing:** 512×512 resize · [0,1] normalization · augmentation (flip, ±18° rotation, 0.9–1.1× zoom, ±10% contrast)

---

## 📊 Results

### Classification Performance

| Model | Accuracy | Precision | Recall | F1-Score | Specificity | AUC |
|---|---|---|---|---|---|---|
| CNN-ViT (FP32) | 96.50% | 95% | 98% | 96.00% | 95% | 98% |
| **CNN-ViT (DRQ)** | **97.00%** | **97%** | **97%** | **97.00%** | **97%** | **98%** |
| CNN-ViT (Float16) | 96.75% | 95% | 98% | 96.79% | 95% | 98% |

### Model Size After Quantization

| Variant | Size (MB) | Reduction |
|---|---|---|
| FP32 Baseline | 26.78 MB | — |
| Dynamic-Range Quantization (DRQ) | **2.38 MB** | **~91% ↓** |
| Float16 Quantization | 4.48 MB | ~83% ↓ |

Both quantized variants are **under the 5 MB TinyML threshold** — with no meaningful accuracy degradation.

### Comparison Against Baseline Models

| Model | Quantization | Accuracy | AUC | F1-Score | Size (MB) |
|---|---|---|---|---|---|
| **CNN-ViT Hybrid** | DRQ | **97.00%** | **98%** | **97.00%** | **2.38** |
| **CNN-ViT Hybrid** | F16 | **96.75%** | **98%** | **96.79%** | **4.48** |
| MobileNet-ViT Fusion | DRQ | 95.50% | 97.64% | 95.40% | 2.71 |
| MobileNetV3Small | DRQ | 94.00% | 97.00% | 93.81% | 1.06 |
| Custom ViT | DRQ | 94.25% | 96.00% | 94.24% | 1.53 |
| MobileNetV2 | DRQ | 92.25% | 98.00% | 92.35% | 2.39 |

The CNN-ViT hybrid achieves the **best accuracy-efficiency trade-off** across all models tested.

---

## 🔍 Explainable AI (XAI)

A key clinical challenge with quantized models is that standard gradient-based explainability methods (Grad-CAM, SHAP, Integrated Gradients) **cannot function** on TFLite models — the gradient path is removed during conversion.

This work integrates **LIME (Local Interpretable Model-Agnostic Explanations)**, which:
- Generates perturbations of the input image
- Fits a local surrogate model around each prediction
- Highlights image superpixels most influential to the classification decision
- Requires **no gradient access** → works on any quantized model

LIME visualizations confirmed that the model consistently attends to clinically relevant breast tissue regions — texture patterns (CNN component) and structural morphology (ViT component) — supporting clinical trustworthiness.

> **Limitation acknowledged:** LIME sometimes highlights high-intensity fatty tissue adjacent to tumors due to superpixel segmentation. This is a known limitation of post-hoc superpixel methods and an identified direction for future work.

---

## ⚙️ TinyML Deployment Pipeline

```
Trained FP32 Model (TensorFlow / Keras)
         │
         ├──► Dynamic-Range PTQ  →  Wint8  = Qint8(Wfp32)  →  2.38 MB TFLite model
         │
         └──► Float16 PTQ        →  Wfp16  = Qfp16(Wfp32)  →  4.48 MB TFLite model
```

Both exported models are loadable via `tf.lite.Interpreter` and deployable on Raspberry Pi, microcontrollers, and mobile devices — enabling inference without a GPU.

---

## 🛠️ Tech Stack

| Component | Tool |
|---|---|
| Deep Learning Framework | TensorFlow / Keras |
| Quantization | TensorFlow Lite PTQ |
| Explainability | LIME (`lime` library) |
| Data Source | Duke Breast MRI / TCIA |
| Compute Environment | Kaggle GPU |
| Language | Python 3.x |

---

## 📄 Citation

If you reference this work, please cite:

```bibtex
@unpublished{nasir2025tinyml,
  author    = {Ali Mohammad Nasir Uddin and Khandoker Momotaz Ferdouse},
  title     = {Edge-Deployable TinyML Framework for Breast Cancer Detection
               with Explainable AI from DCE-MRI},
  school    = {International University of Business Agriculture and Technology (IUBAT)},
  year      = {2025},
  type      = {Bachelor's Thesis},
  address   = {Dhaka, Bangladesh},
  note      = {Unpublished bachelor's thesis, Department of Computer Science and Engineering, IUBAT}
}
```

---

## 🎓 Academic Context

This thesis was completed as part of the Bachelor of Computer Science and Engineering (BCSE) program at IUBAT. The work addresses a gap at the intersection of three domains — **medical AI**, **efficient deep learning**, and **explainability** — specifically targeting the deployment constraints of healthcare systems in low-resource settings.

> *"Most hybrid CNN-Transformer models still employ heavy backbone architectures that make them unsuitable for edge deployment. This work proposes a fully custom, quantization-robust alternative validated on a real-world DCE-MRI dataset."*

---

## 📬 Contact

**Ali Mohammad Nasir Uddin**
BSc in Computer Science and Engineering, IUBAT
📧 uddin.nasir.mym@gmail.com

