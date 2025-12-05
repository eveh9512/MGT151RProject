# Project Submission: Follower Size and Engagement Rate Analysis

## Research Question
**Does follower size predict engagement rate across different categories?**

## Overview
This folder contains the core analysis files for investigating the relationship between influencer follower count and engagement rates across different influencer categories. The analysis reveals important insights about how follower size predicts engagement differently depending on the influencer's category.

## Files Included

### 1. `data_cleaning.ipynb`
- **Purpose**: Data cleaning and preprocessing pipeline
- **Contents**: 
  - Data extraction and validation
  - Handling missing values and outliers
  - Data type conversions and standardization
  - Creation of cleaned dataset ready for analysis

### 2. `Insight_Visualization.ipynb`
- **Purpose**: Statistical analysis and visualization of the research question
- **Contents**:
  - Descriptive statistics by category
  - Regression analysis (follower size vs. engagement rate)
  - Category-specific scatter plots with regression lines
  - Correlation matrix analysis
  - Key visualizations demonstrating the inverse relationship between follower size and engagement rate

### 3. `data_validation_plots.png`
- **Purpose**: Dashboard visualization of dataset characteristics
- **Contents**:
  - Distribution of posts per influencer
  - Distribution of engagement rates
  - Distribution of total engagement
  - Scatter plots showing relationships between key variables
  - Category breakdown of influencers
  - Summary statistics

### 4. `datasets/cleaned_dataset_filtered.csv`
- **Purpose**: Final cleaned dataset used for analysis
- **Contents**:
  - 20,648 influencer records
  - Key variables: follower count, engagement rate, category, likes, comments, total engagement
  - Filtered and validated data ready for statistical analysis

## Key Findings

1. **Inverse Relationship**: Follower size predicts engagement rate inversely - larger follower counts correlate with lower engagement rates across all categories.

2. **Category-Specific Patterns**: The strength of the inverse relationship varies by category, indicating that follower size predicts engagement differently depending on the influencer's industry.

3. **Multi-Metric Approach**: Follower count alone is not a strong predictor; engagement metrics (likes, comments, total engagement) provide better signals for influencer selection.

## Usage

1. Review `data_cleaning.ipynb` to understand the data preprocessing steps
2. Examine `Insight_Visualization.ipynb` for the complete statistical analysis and visualizations
3. Reference `data_validation_plots.png` for an overview of dataset characteristics
4. Use `datasets/cleaned_dataset_filtered.csv` to reproduce or extend the analysis

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- statsmodels

## Notes

All analysis was performed using only the files included in this submission folder. The dataset contains 20,648 influencers across 9 categories (fashion, beauty, fitness, food, travel, family, pet, interior, other).

