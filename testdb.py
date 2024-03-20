from pymongo import MongoClient
from datetime import datetime, timedelta


def saveBal(amt,userid,password,transid,formonthof,scino,customerid,officeID):
    # Connect to MongoDB
    client = MongoClient('mongodb+srv://sugamf7:yunisha123@pyauto.hkt89gc.mongodb.net/test')

    database_name = "your_database_name"  # Replace with your actual database name
    collection_name = "your_collection_name"  # Replace with your actual collection name

    # Create a TTL index on the 'expire_at' field with an expiration time of 60 seconds (1 minute)
    database = client[database_name]
    collection = database[collection_name]
    collection.create_index("expire_at", expireAfterSeconds=60)

    # Define the schema for the documents
    bill_schema = {
        "billamt": str,
        "userId": str,
        "password": str,
        "transid": str,
        "formonthof": str,
        "scino": str,
        "customerid": str,
        "officeID": str,
          # Added a key field as per your example
        "expire_at": datetime  # Added an expiration field
    }

    # Create a document with an expiration time of 1 minute
    data_to_insert = {
        "billamt": amt,
        "userId":userid,
        "password": password,
        "transid": transid,
        "formonthof":formonthof,
        "scino": scino,
        "customerid": customerid,
        "officeID": officeID,
        
        "expire_at": datetime.utcnow() + timedelta(seconds=60)
    }

    # Insert the document into the collection
    collection.insert_one(data_to_insert)

    # Retrieve documents that haven't expired yet
    current_time = datetime.utcnow()
    result = collection.find({"expire_at": {"$gte": current_time}})
    for document in result:
        print(document)
