import json

with open("Input/students.json", "r") as f:
    students = json.load(f)

names = [student["name"] for student in students if len(student["name"]) > 5]


with open("Output/output13.json", "w") as f2:
    json.dump({"long_names": names}, f2, indent=4)
