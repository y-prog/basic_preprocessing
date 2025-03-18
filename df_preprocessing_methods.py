import pandas as pd
import numpy as np
import datetime as dt

import pandas as pd
import numpy as np

def fill_nan_with_metric(df: pd.DataFrame, col: str, metric: str) -> pd.DataFrame:
    """Fill NaNs using mean, median, or mode."""
    metric = metric.lower()
    try:
        if metric == 'mean':
            df[col] = df[col].fillna(df[col].mean())
        elif metric == 'median':
            df[col] = df[col].fillna(df[col].median())
        elif metric == 'mode':
            mode_values = df[col].mode()
            if len(mode_values) > 1:
                df[col] = df[col].fillna(mode_values[int(np.mean(mode_values))])
            else:
                df[col] = df[col].fillna(df[col].median())
        else:
            raise ValueError("Use 'mean', 'median', or 'mode'.")
    except Exception as e:
        print(f"Error: {e}")
    return df

def encode_cols(df: pd.DataFrame, cols_to_encode: list) -> pd.DataFrame:
    """One-hot encode categorical columns."""
    return pd.get_dummies(df, columns=cols_to_encode, drop_first=True)

def convert_col_to_datetime(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Convert a column to datetime."""
    df.loc[:, col] = pd.to_datetime(df[col])  # Use .loc to avoid warnings
    return df

def date_difference(df: pd.DataFrame, date_1: dt.date, date_2_col: str, date_diff_new_col: str) -> pd.DataFrame:
    """Calculate days between a fixed date and a column."""
    fixed_date = pd.to_datetime(date_1)  # Ensure fixed date is a datetime object
    col_date = pd.to_datetime(df[date_2_col])  # Ensure fixed date is a datetime object
    df[date_diff_new_col] = (fixed_date - col_date).dt.days
    return df
