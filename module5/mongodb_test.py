from pymongo import MongoClient
import pymongo

url = "mongodb+srv://admin:admin@cluster0.5b4xbuj.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

client = pymongo.MongoClient(url)
db = client.pytech
print("-- Pytech Collection List --")
print(db.list_collection_names())