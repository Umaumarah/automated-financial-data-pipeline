

import os
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure the plots folder exists
os.makedirs("../plots", exist_ok=True)

# Example: Plot AAPL closing price
plt.figure(figsize=(10, 5))
sns.lineplot(x='date', y='aapl', data=aapl_df)  # use your column names
plt.title("AAPL Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Close Price")

# Save the figure
plt.savefig("../plots/aapl_closing_price.png")  # saved in plots folder
plt.close()  # close figure to prevent overlap
