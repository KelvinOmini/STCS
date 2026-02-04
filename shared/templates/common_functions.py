import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def missing_value_report(df):
    """
    Returns a DataFrame showing the count and percentage of missing values per column.
    """
    missing_count = df.isnull().sum()
    missing_pct = 100 * df.isnull().sum() / len(df)
    report = pd.concat([missing_count, missing_pct], axis=1)
    report.columns = ['Missing Count', 'Missing Percentage']
    return report[report['Missing Count'] > 0].sort_values(by='Missing Percentage', ascending=False)

def outlier_iqr_removal(df, column):
    """
    Removes outliers from a column using the IQR method.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

def plot_price_vs_area(df, price_col='Price', area_col='Area'):
    """
    Plots a scatter plot of Price vs Area using Plotly.
    """
    fig = px.scatter(df, x=area_col, y=price_col, trendline="ols",
                     title=f"Relationship between {area_col} and {price_col}",
                     labels={area_col: f"{area_col} (sqft)", price_col: f"{price_col} ($)"},
                     template="plotly_white")
    return fig

def correlation_heatmap(df):
    """
    Plots a correlation heatmap for numerical features.
    """
    corr = df.select_dtypes(include=[np.number]).corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap of Numerical Features")
    plt.show()
