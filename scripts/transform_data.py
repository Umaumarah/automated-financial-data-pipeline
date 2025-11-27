
import pandas as pd
import os

def transform_data(input_file):
    # Read CSV, skip the first row which is a duplicate header
    df = pd.read_csv(input_file, skiprows=[0])

    # The first column contains dates, so rename it
    df.rename(columns={df.columns[0]: 'date'}, inplace=True)

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Inspect columns
    print("Columns after renaming:", df.columns.tolist())

    # Define symbols and their wide-format columns
    symbols = {
        'AAPL': ['Open','High','Low','Close','Adj Close','Volume'],
        'MSFT': ['Open.1','High.1','Low.1','Close.1','Adj Close.1','Volume.1'],
        'BTC-USD': ['Open.2','High.2','Low.2','Close.2','Adj Close.2','Volume.2'],
        'EURUSD=X': ['Open.3','High.3','Low.3','Close.3','Adj Close.3','Volume.3']
    }

    tidy_dfs = []

    for sym, cols in symbols.items():
        available_cols = [c for c in cols if c in df.columns]
        if len(available_cols) < 4:
            continue

        temp = df[['date'] + available_cols].copy()

        # Standardize column names
        standard_cols = ['date', 'open', 'high', 'low', 'close', 'adj_close', 'volume']
        temp.columns = ['date'] + standard_cols[1:len(temp.columns)]

        temp['symbol'] = sym
        tidy_dfs.append(temp)

    # Combine all symbols into one DataFrame
    tidy_df = pd.concat(tidy_dfs, ignore_index=True)

    # Drop rows with missing date or close
    tidy_df = tidy_df.dropna(subset=['date', 'close'])

    return tidy_df

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_file = os.path.join(project_root, "data", "raw_data.csv")
    output_file = os.path.join(project_root, "data", "clean_data.csv")

    clean_df = transform_data(input_file)
    clean_df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

