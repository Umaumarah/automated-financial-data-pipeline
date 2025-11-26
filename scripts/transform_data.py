import pandas as pd
import os

def transform_data(input_file, output_file):
    # Read raw CSV
    df = pd.read_csv(input_file)

    # 1. Standardize column names
    df.columns = [col.strip().replace(" ", "_").lower() for col in df.columns]

    # 2. Convert 'date' column to datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    # 3. Handle missing values (drop rows where 'close' is missing)
    if 'close' in df.columns:
        df = df.dropna(subset=['close'])

    # 4. Sort by date
    if 'date' in df.columns:
        df = df.sort_values(by='date')

    return df

if __name__ == "__main__":
    # Define paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    input_file = os.path.join(project_root, "data", "raw_data.csv")
    output_file = os.path.join(project_root, "data", "clean_data.csv")

    # Transform data
    clean_df = transform_data(input_file, output_file)

    # Save cleaned CSV
    clean_df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

