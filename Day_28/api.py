from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# base de données
students = {
    1: {"name": "Asabeneh", "country": "Finland", "age": 38},
    2: {"name": "David", "country": "UK", "age": 34},
    3: {"name": "John", "country": "Sweden", "age": 28},
}


# Récupérer tous les étudiants
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


# Récupérer un étudiant par ID
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = students.get(student_id)
    if student:
        return jsonify(student)
    else:
        abort(404, description="Student not found")


# Créer un nouvel étudiant
@app.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    if not data or "name" not in data or "country" not in data or "age" not in data:
        abort(400, description="Invalid data")

    new_id = max(students.keys()) + 1 if students else 1
    students[new_id] = {
        "name": data["name"],
        "country": data["country"],
        "age": data["age"],
    }
    return jsonify({"id": new_id}), 201


# Mise à jour d'un étudiant existant
@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    if student_id not in students:
        abort(404, description="Student not found")

    data = request.get_json()
    if not data:
        abort(400, description="Invalid data")

    # Mise à jour des champs fournis
    student = students[student_id]
    student["name"] = data.get("name", student["name"])
    student["country"] = data.get("country", student["country"])
    student["age"] = data.get("age", student["age"])

    return jsonify(student)


# Suppression
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        return jsonify({"message": f"Student {student_id} deleted"})
    else:
        abort(404, description="Student not found")


if __name__ == "__main__":
    app.run(debug=True)
