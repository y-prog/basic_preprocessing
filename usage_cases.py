import pandas as pd
import numpy as np
import datetime as dt
import df_preprocessing_methods as dpm


# Perform preprocessing steps
def preprocess_data(df):
    clean_age_df = dpm.fill_nan_with_metric(df, 'Age', 'MEDIAN')
    clean_income_df = dpm.fill_nan_with_metric(clean_age_df, 'Income (£)', 'MEAN')
    clean_date_df = clean_income_df.dropna()
    str_to_datetime_df = dpm.convert_col_to_datetime(clean_date_df, 'SignupDate')
    date_today = dt.date.today()
    days_diff_df = dpm.date_difference(str_to_datetime_df, date_today,
                                       'SignupDate', 'DaysSinceSignup')

    days_diff_df['Purchased'] = days_diff_df['Purchased'].map({'Yes': 1, 'No': 0})
    encoded_df = dpm.encode_cols(days_diff_df, ['Gender'])
    final_df = encoded_df
    return final_df


if __name__ == "__main__":
    cust_df = pd.read_csv('csv_files/cust.csv')  # Uncomment when needed
    processed_df = preprocess_data(cust_df)
    print(processed_df)