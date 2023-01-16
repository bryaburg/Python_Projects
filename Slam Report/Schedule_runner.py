import schedule
import time
import subprocess

def job1():
    subprocess.run(["python", "Pulling_Report.py"])

def job2():
    subprocess.run(["python", "Slack_Bot.py"])

schedule.every(2).hours.do(job1)
schedule.every(2).hours.do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)
