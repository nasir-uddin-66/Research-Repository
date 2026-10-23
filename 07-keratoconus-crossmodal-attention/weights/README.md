# Released weights

`keratoconus_released_weights.pt` (395 MB) is the evaluated checkpoint of the main model (EMA weights at the epoch chosen on validation loss).

Download it from the [weights folder on Google Drive](https://drive.google.com/drive/folders/1BUuW3MO1M2LQ5zAYyrJ6-hNHu9t9TNmt?usp=sharing) and verify it:

```
sha256sum keratoconus_released_weights.pt
```

Expected: see `SHA256SUMS.txt`.

Load it with the model class in `notebooks/01_main_resnet50_crossattention.ipynb`: `model.load_state_dict(torch.load(path, map_location='cpu', weights_only=True))`. Apply the temperature and threshold printed by the notebook (fitted on ORBSCAN validation).
