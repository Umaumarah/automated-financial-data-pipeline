
import yfinance as yf
import pandas as pd
import os

def fetch_data(symbols, output_file=None):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if output_file is None:
        output_file = os.path.join(project_root, "data", "raw_data.csv")
    
    all_data = []
    for symbol in symbols:
        df = yf.download(symbol, period="1mo")  # 1 month data
        df.reset_index(inplace=True)
        df['symbol'] = symbol
        all_data.append(df)
    
    final_df = pd.concat(all_data, ignore_index=True)
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    final_df.to_csv(output_file, index=False)
    print(f"Raw data saved to {output_file}")
