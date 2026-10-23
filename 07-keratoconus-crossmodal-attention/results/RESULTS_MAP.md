# Which file feeds what

| Item | File |
|---|---|
| Main model, internal and external metrics with CIs | `main/overall_test_performance.csv` |
| AUC (DeLong), sensitivity and specificity (exact CIs), calibration | `main/statistical_validation.csv` |
| Eye-level scores, internal test | `main/test_predictions.csv` |
| Case-level scores, Pentacam | `main/external_pentacam_predictions.csv` |
| Training curve data | `main/training_history.csv` |
| Seed, threshold, all metrics in one row | `main/seed_results.csv` |
| Backbone ablation tables | `backbone_ablation/ablation_internal_table.csv`, `ablation_external_table.csv` |
| Backbone cost, cutoff and weight hash | `backbone_ablation/ablation_cost_and_operating_points.csv` |
| Fusion ablation tables | `fusion_ablation/ablation_internal_table.csv`, `ablation_external_table.csv` |
| Fusion cost, cutoff and weight hash | `fusion_ablation/ablation_cost_and_operating_points.csv` |
| Every model side by side at its own cutoff | `comparison_with_main.csv` (from `scripts/compare_with_main.py`) |
| Paired AUC tests against the main model | `paired_auc_vs_main.csv` (from `scripts/compare_with_main.py`) |

Figures: `figures/main/` (fig1 to fig9), `figures/backbone_ablation/` and `figures/fusion_ablation/` (ROC, forest plot, size vs AUC, training curves).
