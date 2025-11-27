

import pandas as pd
import sqlite3
import os

if __name__ == "__main__":
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_file = os.path.join(project_root, "data", "clean_data.csv")
    db_file = os.path.join(project_root, "data", "finance.db")

    # Ensure data folder exists
    os.makedirs(os.path.dirname(db_file), exist_ok=True)

    # Read cleaned CSV
    df = pd.read_csv(input_file)

    # Connect to SQLite (creates DB if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS financial_data (
        date TEXT,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        adj_close REAL,
        volume INTEGER,
        symbol TEXT,
        fetched_at TEXT
    )
    """)

    # Insert data into table (replace existing data)
    df.to_sql("financial_data", conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()

    print(f"Cleaned data loaded into SQLite database: {db_file}")

