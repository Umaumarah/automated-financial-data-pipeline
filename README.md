📈 Automated Financial Data Pipeline
An end-to-end automated financial data pipeline built using Python, APIs, SQLite, and Matplotlib.
This project fetches real-time market data (stocks & crypto), cleans and transforms it, loads it into a SQLite database, and automatically generates visualizations.

This pipeline is designed to run on a single command (python run_pipeline.py), making it ideal for automation, cron jobs, and production-level workflows.

🔥 Key Features
✅ 1. Automated Data Fetching
Fetches data for selected tickers using API
Saves raw data into /data/raw_data.csv

✅ 2. Data Cleaning & Transformation
Fixes missing values
Ensures correct data types
Generates metrics (returns, moving averages, etc.)
Saves output into /data/clean_data.csv

✅ 3. SQLite Database Storage
Loads clean data into finance.db
Creates structured tables for each ticker

✅ 4. Automated Visualization
Generates line charts for each ticker
Saves plots into /plots/

✅ 5. One-Click Pipeline
Run the entire ETL + visualizations using:
python run_pipeline.py

📁 Project Structure
automated-financial-data-pipeline/
│
├── data/
│   ├── raw_data.csv
│   ├── clean_data.csv
│   └── finance.db
│
├── plots/
│   ├── AAPL_plot.png
│   ├── MSFT_plot.png
│   ├── TSLA_plot.png
│   └── BTC_plot.png
│
├── scripts/
│   ├── fetch_data.py
│   ├── transform_data.py
│   ├── load_to_sqlite.py
│   └── visualize.py
│
├── run_pipeline.py
├── requirements.txt
└── README.md

🚀 How to Run the Pipeline
1. Install dependencies
pip install -r requirements.txt

2. Run the full pipeline
python run_pipeline.py

3. Check outputs
Cleaned data → /data/clean_data.csv
SQLite DB → /data/finance.db
Plots → /plots/

📊 Sample Output (Plots)
AAPL	 TSLA

BTC	   MSFT

	
🧠 Technologies Used
Category	Tools
Language	Python
Data Storage	SQLite
APIs	(e.g., MarketStack / Yahoo Finance / Finnhub)
Visualization	Matplotlib
Libraries	Pandas, Requests, SQLite3
🎯 Project Goals

This project demonstrates:
ETL (Extract → Transform → Load) automation
API integration
Data engineering workflow
Database and file management
Visualization and business insights
Clean, reusable, modular Python scripts

Great for Data Analyst, Data Engineer, and Python developer portfolios.
