"""Compare every ablation variant with the main model from the saved predictions.

Usage (from the repo root):  python scripts/compare_with_main.py

Writes into results/:
  comparison_with_main.csv      point metrics at each model's own validation-fitted cutoff
  paired_auc_vs_main.csv        AUC difference (variant - main), 95% CI, paired DeLong p
"""
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import roc_auc_score, matthews_corrcoef, f1_score

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / 'results'
N_BOOT, SEED = 2000, 42

MODELS = {'ResNet-50 (main)': RES / 'main'}
for name in ['resnet18', 'resnet34', 'resnet101', 'densenet121', 'efficientnet_b0', 'convnext_tiny']:
    MODELS[name] = RES / 'backbone_ablation' / name
for name in ['gated', 'self_all']:
    MODELS[f'fusion: {name}'] = RES / 'fusion_ablation' / name


def load(folder):
    i = pd.read_csv(folder / 'test_predictions.csv')
    e = pd.read_csv(folder / 'external_pentacam_predictions.csv')
    return i, e


def point(y, p, pred):
    tp, fn = np.sum((pred == 1) & (y == 1)), np.sum((pred == 0) & (y == 1))
    tn, fp = np.sum((pred == 0) & (y == 0)), np.sum((pred == 1) & (y == 0))
    return {'accuracy': (tp + tn) / len(y), 'sensitivity': tp / (tp + fn), 'specificity': tn / (tn + fp),
            'f1': f1_score(y, pred), 'mcc': matthews_corrcoef(y, pred), 'roc_auc': roc_auc_score(y, p),
            'missed_kc': int(fn), 'false_alarms': int(fp)}


def midrank(x):
    order = np.argsort(x)
    z = x[order]
    r = np.zeros(len(x))
    i = 0
    while i < len(x):
        j = i
        while j < len(x) and z[j] == z[i]:
            j += 1
        r[i:j] = 0.5 * (i + j - 1) + 1
        i = j
    out = np.empty(len(x))
    out[order] = r
    return out


def delong_paired(y, p1, p2):
    """Paired DeLong test for two AUCs on the same cases (Sun and Xu 2014)."""
    order = np.argsort(-y)
    y = y[order]
    preds = np.vstack([p1[order], p2[order]])
    m = int(y.sum())
    n = len(y) - m
    v01, v10, aucs = [], [], []
    for p in preds:
        pos, neg = p[:m], p[m:]
        tz, tx, ty = midrank(p), midrank(pos), midrank(neg)
        aucs.append((tz[:m].sum() - m * (m + 1) / 2) / (m * n))
        v01.append((tz[:m] - tx) / n)
        v10.append(1 - (tz[m:] - ty) / m)
    s = np.cov(np.array(v01)) / m + np.cov(np.array(v10)) / n
    var = s[0, 0] + s[1, 1] - 2 * s[0, 1]
    z = (aucs[0] - aucs[1]) / np.sqrt(var) if var > 0 else 0.0
    return aucs[0], aucs[1], 2 * stats.norm.sf(abs(z))


def boot_diff(y, p1, p2, groups, rng):
    """Bootstrap of AUC(variant) - AUC(main); resamples patients when groups are given."""
    members = [np.flatnonzero(groups == g) for g in np.unique(groups)] if groups is not None else None
    out = []
    while len(out) < N_BOOT:
        idx = rng.randint(0, len(y), len(y)) if members is None else \
            np.concatenate([members[k] for k in rng.randint(0, len(members), len(members))])
        if len(np.unique(y[idx])) < 2:
            continue
        out.append(roc_auc_score(y[idx], p1[idx]) - roc_auc_score(y[idx], p2[idx]))
    return np.percentile(out, [2.5, 97.5])


data = {k: load(v) for k, v in MODELS.items()}
main_i, main_e = data['ResNet-50 (main)']
for k, (i, e) in data.items():          # every model must score the same eyes in the same order
    assert (i[['patient_id', 'eye', 'label']].values == main_i[['patient_id', 'eye', 'label']].values).all(), k
    assert (e[['patient_id', 'label']].values == main_e[['patient_id', 'label']].values).all(), k

rows, tests = [], []
for k, (i, e) in data.items():
    for cohort, d in (('Internal ORBSCAN', i), ('External Pentacam', e)):
        rows.append({'model': k, 'cohort': cohort, **point(d.label.values, d.p_keratoconus.values, d.prediction.values)})
pd.DataFrame(rows).round(4).to_csv(RES / 'comparison_with_main.csv', index=False)

rng = np.random.RandomState(SEED)
for k, (i, e) in data.items():
    if k.startswith('ResNet-50'):
        continue
    for cohort, d, m, groups in (('Internal ORBSCAN', i, main_i, main_i.patient_id.values),
                                 ('External Pentacam', e, main_e, None)):
        y = d.label.values
        a_var, a_main, p = delong_paired(y, d.p_keratoconus.values, m.p_keratoconus.values)
        lo, hi = boot_diff(y, d.p_keratoconus.values, m.p_keratoconus.values, groups, rng)
        tests.append({'model': k, 'cohort': cohort, 'auc_variant': a_var, 'auc_main': a_main,
                      'difference': a_var - a_main, 'ci_low': lo, 'ci_high': hi, 'delong_p': p})
pd.DataFrame(tests).round(4).to_csv(RES / 'paired_auc_vs_main.csv', index=False)
print(pd.DataFrame(rows).round(3).to_string(index=False))
print(pd.DataFrame(tests).round(4).to_string(index=False))
