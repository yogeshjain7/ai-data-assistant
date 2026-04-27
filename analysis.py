import pandas as pd

def load_data(file):
    return pd.read_csv(file)


def generate_basic_insights(df):
    insights = []

    insights.append(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

    total_missing = df.isnull().sum().sum()
    insights.append(f"Total missing values: {total_missing}")

    duplicates = df.duplicated().sum()
    insights.append(f"Duplicate rows detected: {duplicates}")

    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) > 0:
        top_col = cat_cols[0]
        top_value = df[top_col].value_counts().idxmax()
        insights.append(f"Most frequent value in '{top_col}' is '{top_value}'.")

    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 0:
        top_numeric = num_cols[0]
        max_val = df[top_numeric].max()
        insights.append(f"Highest value in '{top_numeric}' is {max_val}.")

    return "\n".join(insights)


# 🔥 FAST SUMMARY (IMPORTANT)
def create_fast_summary(df):
    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_dict()
    }
    return str(summary)