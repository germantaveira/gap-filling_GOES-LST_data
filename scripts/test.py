import schedule
import time
import datetime

def job(message='stuff'):
    print("I'm working on:", message)
    print(datetime.datetime.now())


schedule.every(1).minutes.do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().hour.do(job, message='things')
# schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
