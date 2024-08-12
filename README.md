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
```
