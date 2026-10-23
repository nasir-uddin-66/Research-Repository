Backbone ablation: cross-modal attention fusion, keratoconus (ORBSCAN -> Pentacam zero-shot)

Backbones: resnet18, resnet34, resnet101, densenet121, efficientnet_b0, convnext_tiny
Seed 42, image size 300, batch 4, max epochs 30, selection by val_loss, EMA 0.99, sensitivity floor 0.95, rule screening
torch 2.10.0+cu128, GPU Tesla T4, python 3.12.13

SHA-256 of the evaluated weights of each run (weights themselves are not included):
  resnet18: fa810b1000f2e93bbc9f505e020187eaedf618faf58fc45e5a33a7198d0560c1
  resnet34: 1937c97487b704afb5010ce15b81a82b2bf7f129333b25e9e1580ced720fae1d
  resnet101: b56896a4b5cafad62ee2ea0d998e52086a451a10b8b7881053d29b08bfa40956
  densenet121: e051b2364131e67eb3c5cda6eb54785638b71f803b0b6cfa7ccb04c225f268c4
  efficientnet_b0: 7a8c792de23893d2b874c6ef474a0eb33360dc70134a7ba1507592af4da4654f
  convnext_tiny: c762edd22539302cc95a4863db04e023747e4a331f7a9cc2e17106c07a3cbcea

Files: ablation_*.csv (tables), one folder per variant (history, predictions, run summary). Splits are in ../../splits, figures in ../../figures/backbone_ablation.
