import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def calculate_var(df, confidence_level=0.95):
    returns = df['returns']
    sorted_returns = np.sort(returns)
    var = sorted_returns[int((1-confidence_level) * len(sorted_returns))]
    return var

def save_var(var, file_path):
    with open(file_path, 'w') as f:
        f.write(str(var))

if __name__ == "_main_":
    processed_data_path = 'data/processed/financial_data_processed.csv'
    var_output_path = 'data/processed/var_value.txt'

    df = load_data(processed_data_path)
    var = calculate_var(df)
    save_var(var, var_output_path)