# 🔬 Research Portfolio — Ali Mohammad Nasir Uddin

**BSc in Computer Science and Engineering**  
IUBAT — International University of Business Agriculture and Technology, Dhaka, Bangladesh  
📧 22103395@iubat.edu · 

---

## 👤 About

I am a CSE graduate from IUBAT with a focus on applied machine learning for healthcare. My research sits at the intersection of **medical AI**, **efficient deep learning**, and **trustworthy clinical prediction** — with a particular interest in making models that are not only accurate but deployable, interpretable, and robust under real-world conditions.

I build this expertise independently through research projects. All projects listed here are self-directed or supervisor-guided original research.

---

## 📚 Research Projects

| # | Project | Domain | Status |
|---|---|---|---|
| 01 | [Edge-Deployable TinyML for Breast Cancer Detection](#01-breast-cancer-tinyml) | TinyML · Medical Imaging | ✅ Completed · 📤 Paper Submitted |
| 02 | [Brain-CNNViT: Lightweight TinyML for Brain Tumor Classification](#02-brain-tumor-tinyml) | TinyML · Medical Imaging | 🔄 Under Peer Review (Springer Nature) |
| 03 | [Metadata-Based ML for Skin Lesion Malignancy Prediction](#03-skin-cancer-metadata-ml) | Tabular ML · Clinical AI | 📤 Submitted (Elsevier) |
| 04 | [Multimodal Skin Lesion Triage: CNN-Transformer + Metadata Fusion](#04-multimodal-skin-triage) | Multimodal Learning · Medical AI | 🔧 Work in Progress |
| 05 | [Missingness-Aware Domain Generalization for Cardiovascular Disease](#05-cardiovascular-domain-generalization) | Domain Generalization · Clinical ML | 🔧 Early-Stage Research |

---

## 🔍 Project Summaries

### 01 · Breast Cancer TinyML
**`01-Thesis/`**

A custom lightweight CNN-ViT hybrid model for breast cancer detection from pre-contrast DCE-MRI, designed for TinyML deployment. Post-training quantization reduces the model to under 5 MB while maintaining 97% accuracy. LIME-based explainability is integrated to support clinical transparency on quantized models where gradient-based methods fail. Completed as undergraduate thesis; a journal paper based on this work has been submitted.

📦 Dataset: Duke Breast Cancer MRI (TCIA) · 🛠 TensorFlow, TFLite, LIME

---

### 02 · Brain Tumor TinyML
**`02-brain-tumor-tinyml/`**

A 643K-parameter CNN-ViT hybrid (Brain-CNNViT) for four-class brain tumor classification from MRI, co-designed for MCU-class deployment. Full INT8 post-training quantization produces a 0.798 MB model fitting within a 1 MB Flash and 512 KB SRAM budget — the only architecture among four evaluated to satisfy these constraints. Validated on a primary test set and an independent external cohort. Statistical equivalence of INT8 and FP32 predictions confirmed via McNemar's test.

📦 Datasets: Hira Brain Tumor MRI (Mendeley) · BRISC (external validation) · 🛠 TensorFlow, TFLite, LIME, SHAP  
📰 Under peer review — *Journal of Umm Al-Qura University for Medical Science* (Springer Nature)

---

### 03 · Skin Lesion Malignancy Prediction (Metadata-Only)
**`03-skin-cancer-malignancy-prediction/`**

An imaging-free machine learning framework for binary skin lesion malignancy prediction using only routine clinical metadata — no dermoscopic images required. Seven classifiers and two late-fusion ensembles are benchmarked under strict patient-level cross-validation. A held-out premalignant challenge set (Actinic Keratosis) is used to evaluate classifier behavior on ambiguous boundary cases. Full reliability suite: bootstrap CIs, McNemar's test, calibration curves, decision curve analysis, conformal prediction, SHAP.

📦 Dataset: PAD-UFES-20 · 🛠 XGBoost, LightGBM, scikit-learn, SHAP  
📰 Submitted — *Computers in Biology and Medicine* (Elsevier)

---

### 04 · Multimodal Skin Lesion Triage
**`04-04-skin-cancer-detection-late-fusion/`**

An ongoing project developing a dual-stream framework that integrates smartphone-captured clinical images with structured patient metadata for skin lesion malignancy triage. The system combines a CNN-Transformer visual classifier with a calibrated gradient-boosted metadata model, fused at the decision level. Designed for resource-constrained, primary care settings where dermoscopic imaging is unavailable.

📦 Dataset: PAD-UFES-20 · 🛠 PyTorch, XGBoost, Grad-CAM, SHAP

---

### 05 · Cardiovascular Disease Domain Generalization
**`05-cardiovascular-domain-generalization/`**

An early-stage research project investigating cross-site generalization in cardiovascular disease prediction. Preliminary experiments using Leave-One-Site-Out evaluation reveal a substantial performance gap compared to conventional random-split evaluation — motivating the proposed method: missingness-aware domain generalization. The research examines whether explicitly modeling site-specific missing-data patterns, combined with calibration-aware training, can produce more reliable predictions on completely unseen clinical sites.

📦 Dataset: UCI Heart Disease (4 sites: Cleveland, Hungary, Switzerland, VA Long Beach) · 🛠 PyTorch, scikit-learn, GroupDRO, CORAL

---

## 🛠 Technical Stack

| Area | Tools |
|---|---|
| Deep Learning | TensorFlow · Keras · PyTorch |
| Classical ML | scikit-learn · XGBoost · LightGBM |
| Edge Deployment | TensorFlow Lite · TFLite Micro |
| Explainability | LIME · SHAP · Grad-CAM · Occlusion Sensitivity |
| Evaluation | Bootstrap CI · McNemar's test · DeLong test · Conformal Prediction |
| Languages | Python |
| Environments | Kaggle GPU · Google Colab |

---

## 📄 Research Interests

Medical AI · TinyML & Edge Deployment · Explainable AI · Domain Generalization · Multimodal Learning · Clinical Decision Support · Tabular Machine Learning

---

> *All research conducted independently or under academic supervision at IUBAT. Code for completed and published works will be made publicly available upon publication.*

---
## 📬 Contact

**Ali Mohammad Nasir Uddin**  
BSc in Computer Science and Engineering, IUBAT  
📧 22103395@iubat.edu  
---

