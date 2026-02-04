# Special Topics in Computer Science – Housing Data Analysis Assessment (Group 1)

## Group Members
- Ekure
- Hillary
- Jesse
- Kelvin
- Mary

## Project Overview
This project involves analyzing five different housing datasets to identify key factors influencing property prices. The team will perform data cleaning, exploratory data analysis (EDA), and create interactive dashboards to visualize insights.

## Repository Structure
The repository follows a hybrid structure to minimize code duplication while allowing individual exploration.

```
STiCS-Assessment/
├── README.md                  ← This file
├── requirements.txt           ← Shared: list of Python packages
├── shared/                    ← Code & resources usable by everyone
│   └── templates/             
│       ├── eda_template.ipynb          ← Skeleton Jupyter notebook for analysis
│       └── common_functions.py         ← Reusable helper functions
├── reports/                   ← Final combined group deliverable
│   └── group_report.docx      
├── ekure/                     ← Individual student folder
│   ├── data/
│   ├── cleaned_data/
│   ├── notebooks/
│   └── images/
├── hillary/                   ← Same sub-structure
├── jesse/                     ← Same sub-structure
├── kelvin/                    ← Same sub-structure
└── mary/                      ← Same sub-structure
```

## Datasets
Each student has an assigned dataset located in their respective `data/` folder.

| Student | Assigned Dataset | Source |
| :--- | :--- | :--- |
| **Ekure** | Ames Housing Dataset | [Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data) |
| **Hillary** | Melbourne Housing Dataset | [Kaggle](https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot) |
| **Jesse** | Boston Housing Dataset | [UCI](https://archive.ics.uci.edu/dataset/222/boston) |
| **Kelvin** | California Housing Dataset | [Scikit-Learn](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset) |
| **Mary** | Bangalore Housing Prices | [Kaggle](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data) |

## Completed Project Dashboard (Phase 3 Finalized)

The team has successfully completed the analysis for all five datasets. Below is a summary of the available resources:

| Student | Dataset | Analysis Notebook | Cleaned Data |
| :--- | :--- | :--- | :--- |
| **Kelvin** | California Housing | [Analysis](../kelvin/notebooks/kelvin_housing_analysis.ipynb) | [CSV](kelvin/cleaned_data/cleaned_california_housing.csv) |
| **Ekure** | Ames Housing | [Analysis](ekure/notebooks/ekure_housing_analysis.ipynb) | [CSV](ekure/cleaned_data/cleaned_ames_housing.csv) |
| **Hillary** | Melbourne Housing | [Analysis](hillary/notebooks/hillary_housing_analysis.ipynb) | [CSV](hillary/cleaned_data/cleaned_melbourne_housing.csv) |
| **Jesse** | Boston Housing | [Analysis](jesse/notebooks/jesse_housing_analysis.ipynb) | [CSV](jesse/cleaned_data/cleaned_boston_housing.csv) |
| **Mary** | Bangalore Housing | [Analysis](mary/notebooks/mary_housing_analysis.ipynb) | [CSV](mary/cleaned_data/cleaned_bangalore_housing.csv) |

### Final Group Report
The synthesized findings and cross-regional comparisons can be found in the [Final Group Report](../reports/group_report.md).

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open Jupyter Lab or Notebook:
   ```bash
   jupyter lab
   ```
3. Navigate to any individual `notebooks/` folder to view the full analysis.
