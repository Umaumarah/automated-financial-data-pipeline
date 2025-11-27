

import matplotlib
matplotlib.use("Agg")  # Use non-GUI backend to avoid memory/GUI issues

import matplotlib
matplotlib.use("Agg")  # non-GUI backend

import pandas as pd
import matplotlib.pyplot as plt
import os

# rest of your code...

import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_file = os.path.join(project_root, "data", "clean_data.csv")
plots_folder = os.path.join(project_root, "plots")
os.makedirs(plots_folder, exist_ok=True)

# Load cleaned data
df = pd.read_csv(data_file)
df['date'] = pd.to_datetime(df['date'])

# Get all symbols
symbols = df['symbol'].unique()

# Plot each symbol
for sym in symbols:
    symbol_df = df[df['symbol'] == sym]
    plt.figure(figsize=(10, 5))
    plt.plot(symbol_df['date'], symbol_df['close'], marker='o')
    plt.title(f"{sym} Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.grid(True)

    # Save plot
    plot_file = os.path.join(plots_folder, f"{sym.lower().replace('=','').replace('-','')}_plot.png")
    plt.savefig(plot_file, dpi=300, bbox_inches="tight")
    plt.close()
    print(f"Plot saved: {plot_file}")
