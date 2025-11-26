
import pandas as pd
import sqlite3
import os

if __name__ == "__main__":
    # Paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_file = os.path.join(project_root, "data", "clean_data.csv")
    db_file = os.path.join(project_root, "data", "finance.db")

    # Read cleaned CSV
    df = pd.read_csv(input_file)

    # Connect to SQLite (creates DB if it doesn't exist)
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create table (if not exists)
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
        fetchedat TEXT
    )
    """)

    # Insert data into table
    df.to_sql("financial_data", conn, if_exists="replace", index=False)

    # Commit and close
    conn.commit()
    conn.close()

    print(f"Cleaned data loaded into SQLite database: {db_file}")
