from scripts.fetch_data import fetch_data
from scripts.transform_data import transform_data
from scripts.load_to_sqlite import load_to_sqlite
from scripts.visualize import generate_plots
import os

# Define paths
project_root = os.path.abspath(os.path.dirname(__file__))
raw_csv_path = os.path.join(project_root, "data", "raw_data.csv")
clean_csv_path = os.path.join(project_root, "data", "clean_data.csv")

# Define symbols to fetch
symbols = ["AAPL", "MSFT", "GOOG", "TSLA"]

# Run pipeline
print("Step 1: Fetching data...")
fetch_data(symbols, output_file=raw_csv_path)

print("Step 2: Transforming data...")
transform_data(input_file=raw_csv_path, output_file=clean_csv_path)

print("Step 3: Loading to SQLite...")
load_to_sqlite(input_file=clean_csv_path)

print("Step 4: Generating plots...")
generate_plots()

print("Pipeline completed successfully!")
