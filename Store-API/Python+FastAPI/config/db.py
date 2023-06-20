from pymongo import MongoClient
import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()
CONNECTION_STR = os.getenv('MONGO_URI')

client = motor.motor_asyncio.AsyncIOMotorClient(CONNECTION_STR)
db = client.college
db = client["STORE-API"]
