# run_pipeline.py

import subprocess
import os

print("🚀 Running full ETL + Visualization pipeline...")

# Step 1: Fetch data
print("\nStep 1: Fetching data...")
subprocess.run(["python", os.path.join("scripts", "fetch_data.py")], check=True)

# Step 2: Visualize (includes data cleaning inside visualize.py)
print("\nStep 2: Transform & Generate plots...")
subprocess.run(["python", os.path.join("scripts", "visualize.py")], check=True)

print("\n✅ Pipeline completed successfully!")
