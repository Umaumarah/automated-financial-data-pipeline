import pandas as pd
import sqlite3
import os

def load_to_sqlite(input_file=None):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if input_file is None:
        input_file = os.path.join(project_root, "data", "clean_data.csv")
    db_file = os.path.join(project_root, "data", "finance.db")
    
    df = pd.read_csv(input_file)
    
    conn = sqlite3.connect(db_file)
    df.to_sql("financial_data", conn, if_exists="replace", index=False)
    conn.close()
    
    print(f"Cleaned data loaded into SQLite database: {db_file}")

