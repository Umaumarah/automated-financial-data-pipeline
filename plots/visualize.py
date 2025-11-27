import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.plot(df['date'], df['close'])
plt.title("AAPL Closing Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.savefig("plots/aapl_plot.png", dpi=300, bbox_inches="tight")
plt.close()


plt.savefig("plots/aapl_plot.png", dpi=300, bbox_inches="tight")

