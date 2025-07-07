import json

with open("Input/students.json", "r") as f:
    students = json.load(f)

names = [student["name"] for student in students if student["name"].startswith("A")]


with open("Output/output14.json", "w") as f2:
    json.dump({"a_names": names}, f2, indent=4)
