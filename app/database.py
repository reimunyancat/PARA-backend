from pymongo import MongoClient

client = MongoClient('')
db = client['mydatabase']
users_collection = db['users']
    
