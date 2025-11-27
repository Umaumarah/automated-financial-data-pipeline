import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt

# -----------------------------
# Paths
# -----------------------------
db_path = os.path.join("data", "finance.db")
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# -----------------------------
# Connect to SQLite
# -----------------------------
conn = sqlite3.connect(db_path)

# Auto-detect table name
table = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchone()
if not table:
    raise Exception("❌ No table found inside finance.db")

table_name = table[0]
print(f"📌 Detected table: {table_name}")

# Read data
df = pd.read_sql(f"SELECT * FROM {table_name}", conn)

# -----------------------------
# Clean Data
# -----------------------------
# Drop rows with missing dates or symbols
df = df[df["date"].notna() & df["symbol"].notna()]

# Convert numeric columns
num_cols = ["open", "high", "low", "close", "adj_close", "volume"]
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows where all numeric columns are NaN
df = df.dropna(subset=num_cols, how="all")

# Convert date column
df["Date"] = pd.to_datetime(df["date"], errors="coerce")
df = df[df["Date"].notna()]

# -----------------------------
# Remove tickers with no price data
# -----------------------------
tickers_to_remove = []
for ticker, group in df.groupby("symbol"):
    if group["close"].isna().all():
        tickers_to_remove.append(ticker)

if tickers_to_remove:
    print(f"⚠️ Removing tickers with no price data: {tickers_to_remove}")
    df = df[~df["symbol"].isin(tickers_to_remove)]
    # Optional: remove permanently from DB
    for t in tickers_to_remove:
        conn.execute(f"DELETE FROM {table_name} WHERE symbol = ?", (t,))
    conn.commit()

# -----------------------------
# Generate plots
# -----------------------------
tickers = df["symbol"].unique()
group = df.groupby("symbol")

print("\nGenerating plots...\n")
for ticker in tickers:
    df_t = group.get_group(ticker)
    
    if df_t["close"].isna().all():
        print(f"⚠️ Skipping {ticker} — no price data available")
        continue

    # Forward/backward fill missing close values
    df_t["Close"] = df_t["close"].fillna(method="ffill").fillna(method="bfill")

    plt.figure(figsize=(10, 5))
    plt.plot(df_t["Date"], df_t["Close"])
    plt.title(f"{ticker} Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")

    output = os.path.join(output_dir, f"{ticker}_plot.png")
    plt.savefig(output)
    plt.close()
    print(f"✅ Saved plot: {output}")

conn.close()
print("\nAll plots generated!\n")

# -----------------------------
# Optional: preview first 5 rows
# -----------------------------
print(df.head())
print("Columns:", df.columns.tolist())
