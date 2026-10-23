# Data

No images are stored in this repository.

| File | What it is |
|---|---|
| `cornorb_manifest.csv` | One row per eye (1407), labels, map paths, patient ID, clinical fields from the source dataset |
| `cornorb_README.txt` | Notes shipped with the CornORB copy |
| `pentacam_manifest.csv` | One row per case (395), label, and the source Pentacam map used for each channel |
| `pentacam_README.txt` | Notes shipped with the Pentacam copy |

Sources:

- CornORB (ORBSCAN): DOI [10.5281/zenodo.17121301](https://doi.org/10.5281/zenodo.17121301).
- Pentacam external cohort: Kaggle dataset [elmehdi12/keratoconus-detection](https://www.kaggle.com/datasets/elmehdi12/keratoconus-detection). Only Normal and Keratoconus cases were used; Suspect cases were excluded.

Working copies used by the notebooks: Kaggle dataset `nasiruddin66/cornorb`. Check the licence of each original source before reuse.
