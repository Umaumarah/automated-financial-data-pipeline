import pandas as pd

def clean_data(input_file="data/raw_data.csv", output_file="data/clean_data.csv"):
    df = pd.read_csv(input_file)

    # Drop rows where any essential price column is missing
    df = df.dropna(subset=["Open", "High", "Low", "Close"])

    # Convert Date to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Sort data properly
    df = df.sort_values(["Symbol", "Date"])

    df.to_csv(output_file, index=False)
    print(f"Clean data saved to: {output_file}")

