import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    # Paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_file = os.path.join(project_root, "data", "finance.db")

    # Connect to SQLite
    conn = sqlite3.connect(db_file)

    # Load data
    df = pd.read_sql("SELECT * FROM financial_data", conn)
    conn.close()

    # Print column names to check
    print("Columns in DB:", df.columns)

    # Convert date to datetime
    df['date'] = pd.to_datetime(df['date'])

    # --- Filter for AAPL rows first ---
    aapl_df = df[df['symbol'] == 'AAPL']

    # Rename columns for plotting
    aapl_df = aapl_df.rename(columns={
        "aapl": "open",
        "aapl.1": "high",
        "aapl.2": "low",
        "aapl.3": "close",
        "aapl.4": "adj_close",
        "aapl.5": "volume"
    })

    # Plot Closing Price
    plt.figure(figsize=(12,6))
    sns.lineplot(x='date', y='close', data=aapl_df)
    plt.title("AAPL Closing Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Close Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Plot Volume
    plt.figure(figsize=(12,6))
    sns.barplot(x='date', y='volume', data=aapl_df)
    plt.title("AAPL Trading Volume")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
