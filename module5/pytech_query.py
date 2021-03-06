from pymongo import MongoClient
from pprint import pprint
import pymongo

url = "mongodb+srv://admin:admin@cluster0.5b4xbuj.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

client = pymongo.MongoClient(url)
db = client.pytech

students = db.students

docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    pprint(doc)
    print(f"\n")

doc = db.students.find_one({"student_id": "1007"})
print(f"\n")
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find_one() QUERY --")
print(f"\n")
print(doc)