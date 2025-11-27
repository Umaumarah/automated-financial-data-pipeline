import schedule
import time
import os

# Path to your fetch_data script
fetch_script = os.path.join(os.path.dirname(__file__), "fetch_data.py")

def job():
    print("Fetching latest financial data...")
    os.system(f'python "{fetch_script}"')
    print("Data fetch completed!")

# Schedule the job every day at 10 AM
schedule.every().day.at("10:00").do(job)

print("Scheduler started...")
while True:
    schedule.run_pending()
    time.sleep(60)  # wait 1 minute

