from pymongo import MongoClient
import pymongo

url = "mongodb+srv://admin:admin@cluster0.5b4xbuj.mongodb.net/?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"

client = pymongo.MongoClient(url)
db = client.pytech

students = db.students

Kendrick ={
    "student id":"1007",
    "first_name":"Kendrick",
    "last_name":"Baker"
}

Kendrick_student_id=students.insert_one(Kendrick).inserted_id

Camden ={
    "student id":"1008",
    "first_name":"Camden",
    "last_name":"Jones"
}

Camden_student_id=students.insert_one(Camden).inserted_id

Lisa ={
    "student id":"1009",
    "first_name":"Lisa",
    "last_name":"Woo"
}

Lisa_student_id=students.insert_one(Lisa).inserted_id

print("-- Insert Statements --")

print(f"\nInserted student record", Kendrick, Kendrick_student_id)
print(f"\nInserted student record", Camden, Camden_student_id)
print(f"\nInserted student record", Lisa, Lisa_student_id)