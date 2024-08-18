# MIMIC-CXR Analysis

### Notebook used 
[Colab Notebook](https://colab.research.google.com/drive/1Os9hRnkezUeN0VRgYj1UBpPFyR4PHbQI?usp=sharing)

### Dataset Installation

Due to storage constraints, the full MIMIC-CXR dataset could not be installed locally. Instead, a subset containing images from 70 subjects was used. The dataset was prepared as follows:

1. **Subset Selection**: Only images for the first 70 unique subject IDs were included.
2. **Directory Structure**: Images are stored locally found in this repo `files`
3. **DataFrame Preparation**: Added `image_path` to the original prediction set assumming that the predictions were conducted sequentially

## Data Analysis

### Score Calculation

The maximum prediction score (`max_pred`) for each image was calculated from the prediction scores (`pred_0` to `pred_5`).

### Categorization

Images were categorized into high-scoring and low-scoring based on a threshold (75th percentile of `max_pred`).

### Race Analysis

The impact of race on scoring was examined by:
- Grouping data by `race` and analyzing average scores.
- Categorizing images by race and score category.
- Performing statistical tests (ANOVA) to assess differences in scores across races.

### ml test

A model was trained to predict `max_pred` based on features including `race`. Models used include Linear Regression and Random Forest.

## Please note this is just a base to build on top of
