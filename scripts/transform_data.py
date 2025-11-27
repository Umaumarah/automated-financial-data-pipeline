import pandas as pd
import os

def transform_data(input_file=None, output_file=None):
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    if input_file is None:
        input_file = os.path.join(project_root, "data", "raw_data.csv")
    if output_file is None:
        output_file = os.path.join(project_root, "data", "clean_data.csv")
    
    df = pd.read_csv(input_file)
    
    # Ensure consistent column names
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # If 'adj_close' doesn't exist, create it as a copy of 'close'
    if 'adj_close' not in df.columns:
        if 'close' in df.columns:
            df['adj_close'] = df['close']
        else:
            raise ValueError("No 'close' column found in raw data")

    # Ensure 'date' column exists
    if 'date' not in df.columns:
        if 'index' in df.columns:
            df = df.rename(columns={'index': 'date'})
        elif 'date' not in df.columns:
            raise ValueError("No 'date' column found in raw data")
    
    # Keep relevant columns
    df = df[['date', 'open', 'high', 'low', 'close', 'adj_close', 'volume', 'symbol']]
    
    df.to_csv(output_file, index=False)
    print(f"Clean data saved to: {output_file}")
