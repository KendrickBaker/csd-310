from pymongo import MongoClient
import pymongo

url = "mongodb+srv://admin:admin@cluster0.5b4xbuj.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

client = pymongo.MongoClient(url)
db = client.pytech

students = db.students

docs = db.students.find({})

for doc in docs:
    print(doc)

doc = db.students.find_one({"student_id": "1007"})
print(f"\n")
print("Displaying student document from find_one() query: ")
print(f"\n")
print(doc)