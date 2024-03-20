
from pymongo import MongoClient
from test import checkbal,saveBal
def send():

  
  
    
  
  
      db_url = 'mongodb+srv://sugamf7:%40Safal12345@cluster0.acytgle.mongodb.net/morupayment'
      client = MongoClient(db_url)
      db = client.get_database()
      collection = db.get_collection("User")
      cursor = collection.find()
      for document in cursor:
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
       
             amount=userdata['total_amount']
       
             saveBal(amt=amount,userid=userid,password=transid,transid=transid,formonthof='2024-01',scino=sc,customerid=cid,officeID=office)
       
       
       
      return

send()