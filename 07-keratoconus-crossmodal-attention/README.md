# Keratoconus detection from four corneal maps with cross-modal attention fusion

Code, splits, predictions and released-weight checksum for a keratoconus classifier trained on ORBSCAN maps (CornORB) and tested zero-shot on an independent Pentacam cohort.

Four ResNet-50 encoders (anterior elevation, axial curvature, pachymetry, posterior elevation) are fused with scaled-cosine cross-modal attention and a learned modality gate. The temperature and the decision threshold are fitted on the ORBSCAN validation split only. The external Pentacam cohort stays fully untouched: nothing is tuned, fine-tuned or thresholded on it.

## Main results

Seed 42, threshold 0.808 (set on ORBSCAN validation), 95% bootstrap CIs.

| | Internal ORBSCAN (282 eyes) | External Pentacam (395 cases) |
|---|---|---|
| Accuracy | 0.986 [0.971, 0.997] | 0.954 [0.934, 0.975] |
| Sensitivity | 0.959 [0.913, 0.991] | 0.914 [0.874, 0.953] |
| Specificity | 1.000 [1.000, 1.000] | 0.995 [0.984, 1.000] |
| F1 | 0.979 [0.955, 0.996] | 0.953 [0.930, 0.974] |
| MCC | 0.969 [0.935, 0.993] | 0.912 [0.872, 0.950] |
| ROC-AUC | 1.000 [0.999, 1.000] | 0.993 [0.988, 0.997] |

Internal confidence intervals resample patients, not eyes. Full tables: `results/main/`.

## Ablations

Same data, splits, seed, training recipe and threshold rule for every row. Only the named part changes.

| Variant | Int. acc | Int. AUC | Ext. acc | Ext. AUC |
|---|---|---|---|---|
| **ResNet-50 + cross-attention (main)** | **0.986** | **1.000** | **0.954** | **0.993** |
| ResNet-18 | 0.979 | 0.999 | 0.782 | 0.988 |
| ResNet-34 | 0.979 | 0.998 | 0.696 | 0.983 |
| ResNet-101 | 0.979 | 0.999 | 0.927 | 0.971 |
| DenseNet-121 | 0.979 | 0.999 | 0.608 | 0.979 |
| EfficientNet-B0 | 0.979 | 0.999 | 0.630 | 0.876 |
| ConvNeXt-Tiny | 0.972 | 0.998 | 0.501 | 0.984 |
| Gated fusion (original) | 0.965 | 0.997 | 0.835 | 0.976 |
| Joint self-attention | 0.975 | 0.999 | 0.899 | 0.990 |

Most variants rank Pentacam cases well (external AUC 0.971 to 0.991, for example ConvNeXt-Tiny at 0.984). Their accuracy differs more because each cutoff is fitted on ORBSCAN validation only and shifts when the device changes. The main model's cutoff transfers best (0.954 accuracy, 0.993 AUC), which is the benefit of the cross-attention design. AUC is the threshold-free comparison.

Paired AUC tests against the main model are in `results/paired_auc_vs_main.csv`, and all point metrics (including missed keratoconus and false alarms) are in `results/comparison_with_main.csv`. Regenerate both with:

```
python scripts/compare_with_main.py
```

## Repository layout

```
notebooks/    01 main model, 02 backbone ablation, 03 fusion ablation
splits/       patient-level train / validation / test CSVs
data/         manifests and dataset notes (no images)
results/      predictions, tables and training histories per experiment
figures/      png + pdf for the main model and both ablations
weights/      SHA-256 of the released weights
scripts/      comparison and paired-test script
```

`results/RESULTS_MAP.md` lists which file feeds which table or figure.

## Data

- **CornORB (ORBSCAN)**: 1407 eyes, four maps each. Patient-level split: 899 / 226 / 282 eyes for train / validation / test. Manifest: `data/cornorb_manifest.csv`.
- **Pentacam external cohort**: 395 cases (198 keratoconus, 197 normal), used for evaluation only. Pentacam maps are paired with the ORBSCAN channel they correspond to (Elv_A to anterior, Sag_A to axial, CT_A to pachymetry, Elv_P to posterior). Case IDs are generated surrogates and laterality is unknown. Manifest: `data/pentacam_manifest.csv`.

Sources:

- CornORB: DOI [10.5281/zenodo.17121301](https://doi.org/10.5281/zenodo.17121301).
- Pentacam: Kaggle dataset [elmehdi12/keratoconus-detection](https://www.kaggle.com/datasets/elmehdi12/keratoconus-detection). Suspect cases were excluded.

Images are kept at their original sources, so this repository stays light. The notebooks read working copies from the Kaggle dataset `nasiruddin66/cornorb` (`CornORB/` and `pentacam-external-validation/`).

## Reproduce

1. Open `notebooks/01_main_resnet50_crossattention.ipynb` on Kaggle with a GPU and the dataset attached.
2. Download `keratoconus_released_weights.pt` (395 MB) from the [weights folder on Google Drive](https://drive.google.com/drive/folders/1BUuW3MO1M2LQ5zAYyrJ6-hNHu9t9TNmt?usp=sharing) and put it in the notebook's working folder or attach it as an input. If the file is found, training is skipped and the same weights are evaluated.
3. Run all cells. Check the printed SHA-256 against `weights/SHA256SUMS.txt`:

```
46ff0eea420359fc308835d68c9f4a20915edefdf0d7828857f3ed1308b2d568
```

To retrain instead, run the notebook without the weights file. Training uses seed 42; GPU kernels are not bit-identical, so a retrained model can differ slightly. For exact, verifiable numbers use the released weights, which every reported result comes from.

Notebooks 02 and 03 train every variant and write the tables, figures and a results zip. Each README inside `results/backbone_ablation/` and `results/fusion_ablation/` lists the weight hash of every run.

## Environment

Kaggle, Tesla T4. Backbone ablation: Python 3.12.13, torch 2.10.0+cu128. Fusion ablation: Python 3.13.15, torch 2.11.0+cu128. Packages are in `requirements.txt`.

## Citation

See `CITATION.cff`. Please cite this repository; the paper reference will be added after publication.

## Licence

Code: MIT. The datasets keep their own licences; check them before reuse.
