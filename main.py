# main.py

from celery import Celery
from nepali_date import NepaliDate
from celery.schedules import crontab
from datetime import datetime, timedelta
import time
import pytz
from test import saveBal
from sendnotificaiton import sendEmail
from test import checkbal
from pymongo import MongoClient

nepal_timezone = pytz.timezone('Asia/Kathmandu')
day = 20
hour = 8
minute = 21
second = 10



def send():

  
  timestamp_nepali = NepaliDate.today()
  current_time = datetime.now(nepal_timezone).strftime('%I:%M:%S %p')

  # Check if it's the date and time is same as the date provided
  if timestamp_nepali.day == day and datetime.now(
      nepal_timezone).hour == hour and datetime.now(
          nepal_timezone).minute == minute and datetime.now(
              nepal_timezone).second == second and datetime.now(
                  nepal_timezone).strftime('%p') == 'PM':
   
    
      print(
          f'Starting the task to send emails @:{timestamp_nepali.year}-{timestamp_nepali.month:02d}-{timestamp_nepali.day:02d} {current_time}'
      )
  
      db_url = 'mongodb+srv://sugamf7:%40Safal12345@cluster0.acytgle.mongodb.net/morupayment'
      client = MongoClient(db_url)
      db = client.get_database()
      collection = db.get_collection("User")
      cursor = collection.find()
      print(cursor)

      
  
      for document in cursor:
        # Extract email and name from the document
        email = document.get("email")
        name = document.get("name")

        office= document.get("ElectricityOfficeNo")
        sc= document.get("ElectricityScNo")
        cid= document.get("ElecricityId")
        transid=document.get("transactionId")
        userid=document.get("phone")
        print(office,sc,cid)
        userdata=checkbal(cid=cid,office=office,sc=sc)
        name=userdata['name']

        amount=int (userdata['total_amount'])

        saveBal(amt=amount,userid=userid,password=transid,transid=transid,formonthof='2024-01',scino=sc,customerid=cid,officeID=office)
  
        # Check if both email and name are present
        if email and name:
           sendEmail(name,amount,email)
           

        else:
          print("Skipped document. Email or name missing.")
  
     
  else:
    print('Sorry')  



celery = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)
@celery.task(name='tasks.print_alive', bind=True, ignore_result=True)
def print_alive(self):
   send()
   
       
# Add a periodic task schedule
celery.conf.beat_schedule = {
    'print-alive-every-second': {
        'task': 'tasks.print_alive',
        'schedule': timedelta(seconds=1), #adding the time where the scheduler works
    },
}

# Start Celery beat
celery.conf.timezone = 'UTC'
celery.conf.beat_schedule_filename = 'celerybeat-schedule'
celery.conf.result_backend = 'redis://localhost:6379/0'
celery.conf.broker_url = 'redis://localhost:6379/0'
celery.conf.accept_content = ['json']
celery.conf.result_serializer = 'json'
celery.conf.task_serializer = 'json'
celery.conf.timezone = 'UTC'

