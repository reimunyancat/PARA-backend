from pymongo import MongoClient

client = MongoClient('mongodb://para5:NoUNoUNoU@HS.5-23.DEV:3000')
db = client['mydatabase']
users_collection = db['users']
    