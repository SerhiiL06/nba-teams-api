import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


DB_NAME = os.getenv("USERNAME")
DB_PASSWORD = os.getenv("PASSWORD")

MONGO_URL = f"mongodb+srv://{DB_NAME}:{DB_PASSWORD}@secretfastapi.hpdseom.mongodb.net/?retryWrites=true&w=majority"


client = MongoClient(MONGO_URL)


db = client.test


teams = db["team"]
