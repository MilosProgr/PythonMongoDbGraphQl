from pymongo import AsyncMongoClient

class MongoDB:
    client: AsyncMongoClient = None
    database = None
db = MongoDB()

async def connect_to_mongo(uri:str):
    db.client = AsyncMongoClient(uri)
    db.database = db.client["test_db"]  

    print("Connected to MongoDB")

async def close_mongo_connection():
    db.client.close()
    print("Closed MnogoDB Connection")