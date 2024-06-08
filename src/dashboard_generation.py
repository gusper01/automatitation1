import pandas as pd
import plotly.express as px

def load_data(file_path):
    return pd.read_csv(file_path)

def load_var(file_path):
    with open(file_path, 'r') as f:
        return float(f.read())

def generate_dashboard(df, var):
    fig = px.histogram(df, x='returns', title=f'VaR: {var:.2f}')
    fig.write_html('docs/index.html')

if __name__ == "_main_":
    processed_data_path = 'data/processed/financial_data_processed.csv'
    var_output_path = 'data/processed/var_value.txt'

    df = load_data(processed_data_path)
    var = load_var(var_output_path)
    generate_dashboard(df, var)