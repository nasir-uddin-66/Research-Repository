Fusion ablation (ResNet-50 encoders): cross-modal attention fusion, keratoconus (ORBSCAN -> Pentacam zero-shot)

Variants: gated, self_all
Seed 42, image size 300, batch 4, max epochs 30, selection by val_loss, EMA 0.99, sensitivity floor 0.95, rule screening
torch 2.11.0+cu128, GPU Tesla T4, python 3.13.15

SHA-256 of the evaluated weights of each run (weights themselves are not included):
  gated: ae0b47b138b3e4386bfead001de14737191b1a0622b612a39cdffd1fcfac1a31
  self_all: 3ffa8e6e645e1337743cb5dd89bf30f46204fc4b3c28391dfd9408b91260b906

Files: ablation_*.csv (tables), one folder per variant (history, predictions, run summary). Splits are in ../../splits, figures in ../../figures/fusion_ablation.
