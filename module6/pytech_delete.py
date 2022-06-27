from pymongo import MongoClient
from pprint import pprint
import pymongo

url = "mongodb+srv://admin:admin@cluster0.5b4xbuj.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

client = pymongo.MongoClient(url)
db = client.pytech
docs = db.students.find({})
docs2 = db.students.find({})
docs3 = db.students.find({})
students = db.students
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in docs:
    pprint(doc)
    print(f"\n")


Casper={
    "student id":"1010",
    "first_name":"Casper",
    "last_name":"Brown"
}

Casper_student_id=students.insert_one(Casper).inserted_id

print(f"\n")
print("-- Insert Statements --")
print(f"\nInserted student record", Casper, Casper_student_id)
print(f"\n")

print("-- DISPLAYING NEW STUDENTS LIST DOC --")

for doc2 in docs2:
    pprint(doc2)
    print(f"\n")

query = { "student id": "1010"}

students.delete_one(query)

print("-- DELETED STUDENT ID 1010 --")
for doc3 in docs3: 
    pprint(doc3)
    print(f"\n")
