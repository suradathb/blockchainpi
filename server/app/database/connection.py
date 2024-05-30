from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")

db = client.presale


get_db = client.presale
collection_name = db["todo_collection"]
products_collection = db["product"]
users_collection = db["users"]
addresses_collection = db["addresses"]
profiles_collection = db["profiles"]
