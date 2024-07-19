from pymongo import MongoClient
from dotenv import load_dotenv
import os

CLIENT = os.getenv("CLIENT")

client = MongoClient(CLIENT)
db = client['mydatabase']
users_collection = db['users']
    