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

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open Jupyter Lab or Notebook:
   ```bash
   jupyter lab
   ```
3. Copy the template from `shared/templates/eda_template.ipynb` to your `notebooks/` folder and start your analysis.
