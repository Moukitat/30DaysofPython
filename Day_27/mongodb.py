# Exercice jour27

from flask import Flask
import os
import pymongo
from bson.objectid import ObjectId

MONGODB_URI = "mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority"

client = pymongo.MongoClient(MONGODB_URI)
db = client["thirty_days_of_python"]

app = Flask(__name__)


@app.route("/")
def operations_mongodb():
    student = {"name": "asabeneh", "country": "Finland", "city": "Helsinki", "age": 250}
    db.students.insert_one(student)

    many_students = [
        {"name": "david", "country": "UK", "city": "London", "age": 34},
        {"name": "John", "country": "Sweden", "city": "Stockholm", "age": 28},
        {"name": "Sami", "country": "Finland", "city": "Helsinki", "age": 25},
    ]
    db.students.insert_many(many_students)

    first_student = db.students.find_one()

    example_id = first_student["_id"]
    student_by_id = db.students.find_one({"_id": ObjectId(example_id)})

    query = {"country": "Finland"}
    finnish_students = list(db.students.find(query))

    db.students.update_one({"age": 250}, {"$set": {"age": 38}})

    db.students.delete_one({"name": "John"})

    all_students = list(db.students.find())

    limited_students = list(db.students.find().limit(3))
    sorted_students_asc = list(db.students.find().sort("name", 1))
    sorted_students_desc = list(db.students.find().sort("age", -1))

    return {
        "first_student": str(first_student),
        "student_by_id": str(student_by_id),
        "finnish_students_count": len(finnish_students),
        "all_students_count": len(all_students),
        "limited_students_count": len(limited_students),
        "sorted_students_asc_first": str(
            sorted_students_asc[0] if sorted_students_asc else {}
        ),
        "sorted_students_desc_first": str(
            sorted_students_desc if sorted_students_desc else {}
        ),
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
