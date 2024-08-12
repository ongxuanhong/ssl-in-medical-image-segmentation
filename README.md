# Run 3 first cells in download.ipynb
Folder Organization
```
|-data
    |-isic2018
        |-images
        |-labels
    |-ham10000
        |-images
        |-labels 
|-processed_data
    |-isic2018
        |-images
        |-labels
    |-ham10000
        |-images
        |-labels
|-Configs
|-Datasets
|-Models
|-Utils
|-README.md
|-download.ipynb
|-*.py
```

# How to run
```bash
python -u fixmatch.py --gpu 0 --seed 1 --exp exp_fixmatch_bbbc --fold 1 --dataset bbbc
--dataset bccd --sup_ratio 0.25 --conf_thres 0.8 --seed 2 --debug 1
```

Grid search
```bash
--sup_ratio
--conf_thres
--fold
--seed
```

```json
{
    "supervised_ratio": [0.01, 0.04],
    "conf_thresh": [0.8, 0.85, 0.9, 0.95],
    "fold": [1, 2, 3, 4, 5],
    "seed": [1, 2, 3]
}
```
