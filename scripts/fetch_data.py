import yfinance as yf
import pandas as pd
from datetime import datetime
import os

def fetch_data(symbols, period="1mo", interval="1d"):
    all_data = []
    for sym in symbols:
        # Download data from yfinance
        df = yf.download(sym, period=period, interval=interval, group_by='ticker', auto_adjust=False)
        df.reset_index(inplace=True)
        df['Symbol'] = sym
        df['FetchedAt'] = datetime.now()
        all_data.append(df)
    # Combine all symbols into one DataFrame
    final_df = pd.concat(all_data, ignore_index=True)
    return final_df

if __name__ == "__main__":
    symbols = ["AAPL", "MSFT", "BTC-USD", "EURUSD=X"]  # Example symbols
    df = fetch_data(symbols)  # <- This must exist before saving

    # Define absolute path for Windows
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_folder = os.path.join(project_root, "data")
    os.makedirs(data_folder, exist_ok=True)

    output_file = os.path.join(data_folder, "raw_data.csv")
    df.to_csv(output_file, index=False)
    print(f"Data fetched and saved to {output_file}")



