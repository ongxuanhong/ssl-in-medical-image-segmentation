# C2GMatch: Leveraging Dual-View Cross-Guidance and Co-Guidance Framework for Semi-Supervised Cell Segmentation

## Overview
This repository implements various semi-supervised learning techniques to address the challenges of medical image segmentation using limited labeled data. The project leverages deep learning methods including pseudo labeling, consistency regularization, co-training, and knowledge priors to effectively segment medical images when labeled annotations are scarce.

The codebase aims to facilitate research and development in medical image segmentation, supporting integration with widely-used medical imaging datasets and advanced segmentation methods.

## Features
- Semi-supervised learning strategies: Pseudo labeling, consistency regularization, co-training, adversarial learning, and entropy minimization.
- Supports 2D medical image data.
- Integration with popular segmentation architectures (e.g., U-Net, nnU-Net).
- Modularized code structure for easy customization and experimentation.

## Methods Implemented
1. **Pseudo Labeling**: Generate pseudo labels on unlabeled images, iteratively updating model predictions for enhanced learning.
2. **Consistency Regularization**: Enforce invariance of predictions under various input perturbations (e.g., noise, rotation).
3. **Co-Training**: Utilize two independent networks to learn from diverse views and supervise each other.
4. **Adversarial Learning**: Introduce a discriminator to distinguish between labeled and unlabeled predictions, refining segmentation outputs.
5. **Knowledge Priors**: Use anatomical priors and self-supervised pre-training tasks to inject domain-specific information, enhancing segmentation accuracy.

## Dataset
This repository supports multiple medical imaging datasets, including:
- [LISC](https://drive.google.com/file/d/11CvIkvHW_sWEvLMQHpJpYhuOIwLCfZ0j/view?usp=drive_link) - for white blood cell image segmentation.
- [BCCD](https://drive.google.com/file/d/1rO0D-mmqx4YOXJ7JpEPnU7vT1iXG70Xj/view?usp=sharing ) - for blood cell count detection.
- [Livecells](https://drive.google.com/file/d/1hVX-9G3qFoLg-WMTz2adUKI3-N2BteRm/view?usp=drive_link) - for live-cell microscopy image segmentation.

Each dataset should be downloaded separately and prepared according to the format required by this repository.

## Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/ongxuanhong/ssl-in-medical-image-segmentation
   cd ssl-in-medical-image-segmentation
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training
To train a model using semi-supervised learning (e.g. using fixmatch.py on bbbc dataset)
```bash
python -u fixmatch.py --gpu 0 --seed 1 --exp exp_fixmatch_bbbc --fold 1 --dataset bbbc
--dataset bccd --sup_ratio 0.25 --conf_thres 0.8 --seed 2 --debug 1
```

### How to run grid search
Grid search

```json
{
    "supervised_ratio": [0.01, 0.04],
    "conf_thresh": [0.8, 0.85, 0.9, 0.95],
    "fold": [1, 2, 3, 4, 5],
    "seed": [1, 2, 3]
}
```

```bash
python grid_exp.py
```


### Configuration
Modify the configuration file (`configs/config.yaml`) to set parameters for different semi-supervised methods, dataset paths, and model architecture. Each method's parameters (e.g., confidence threshold for pseudo-labeling, perturbation types for consistency regularization) can be customized within the config file.

## Repository Structure
```
|-data
    |-bccd
        |-images
        |-labels    
    |-lisc
        |-images
        |-labels 
|-processed_data
    |-bccd
        |-images
        |-labels
    |-lisc
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

## Evaluation Metrics
- Dice Similarity Coefficient (DSC)
- Intersection-over-Union (IoU)
- Hausdorff Distance (HD) (for boundary accuracy)