import pandas as pd

def load_data(file_path):
    print(f"Loading data from {file_path}")
    return pd.read_csv(file_path)

def preprocess_data(df):
    print("Preprocessing data")
    df = df.dropna()
    df['returns'] = df['price'].pct_change().dropna()
    return df

def save_data(df, file_path):
    print(f"Saving data to {file_path}")
    df.to_csv(file_path, index=False)

if __name__ == "__main__":
    raw_data_path = 'data/raw/financial_data.csv'
    processed_data_path = 'data/processed/financial_data_processed.csv'

    df = load_data(raw_data_path)
    df = preprocess_data(df)
    save_data(df, processed_data_path)
    print("Data preprocessing complete")
