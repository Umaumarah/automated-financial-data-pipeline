import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

def generate_plots():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_file = os.path.join(project_root, "data", "finance.db")
    
    conn = sqlite3.connect(db_file)
    df = pd.read_sql("SELECT * FROM financial_data", conn)
    conn.close()
    
    # Ensure lowercase column names
    df.columns = [col.lower() for col in df.columns]

    symbols = df['symbol'].unique()
    plots_dir = os.path.join(project_root, "plots")
    os.makedirs(plots_dir, exist_ok=True)

    for symbol in symbols:
        df_symbol = df[df['symbol'] == symbol]
        plt.figure(figsize=(10,5))
        plt.plot(df_symbol['date'], df_symbol['close'], marker='o')  # lowercase 'close'
        plt.title(f"{symbol} Price Over Time")
        plt.xlabel("Date")
        plt.ylabel("Close Price")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(plots_dir, f"{symbol}_plot.png"))
        plt.close()
    print(f"Plots saved to: {plots_dir}")
