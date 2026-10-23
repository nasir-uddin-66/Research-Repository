Pentacam external-validation dataset for the four-channel ORBSCAN model

This is a derived, non-destructive copy of the Kaggle dataset elmehdi12/keratoconus-detection
(https://www.kaggle.com/datasets/elmehdi12/keratoconus-detection).
Only Normal and Keratoconus cases are included; all Suspect cases are excluded.

Clinical modality mapping:
  Elv_A -> anterior (anterior elevation)
  Sag_A -> axial (anterior sagittal / axial curvature)
  CT_A  -> pachymetry (corneal thickness)
  Elv_P -> posterior (posterior elevation)

EC_A, EC_P, and Sag_P were not copied because they have no direct model channel counterpart.

File pattern: P0001_<Pentacam map code>_<common modality>.jpg; for example,
P0001_Sag_A_axial.jpg. The original Pentacam modality is retained in every filename.
IMPORTANT: patient_id is a generated case surrogate (P0001, etc.), not a verified patient identifier.
eye is UNK in manifest.csv because source metadata provides no laterality. source_case_id preserves its original ID.
Use only for external evaluation; never train, tune, or select a threshold on this dataset.
