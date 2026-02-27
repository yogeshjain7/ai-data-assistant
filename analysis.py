import pandas as pd

def load_data(file):
    return pd.read_csv(file)


def generate_basic_insights(df):
    insights = []

    # Dataset size
    insights.append(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

    # Missing values
    total_missing = df.isnull().sum().sum()
    insights.append(f"Total missing values: {total_missing}")

    # Duplicate rows
    duplicates = df.duplicated().sum()
    insights.append(f"Duplicate rows detected: {duplicates}")

    # Text column insight
    cat_cols = df.select_dtypes(include='object').columns
    if len(cat_cols) > 0:
        top_col = cat_cols[0]
        top_value = df[top_col].value_counts().idxmax()
        insights.append(f"Most frequent value in '{top_col}' is '{top_value}'.")

    # Numeric column insight
    num_cols = df.select_dtypes(include='number').columns
    if len(num_cols) > 0:
        top_numeric = num_cols[0]
        max_val = df[top_numeric].max()
        insights.append(f"Highest value in '{top_numeric}' is {max_val}.")

    return "\n".join(insights)