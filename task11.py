import json

with open("Input/students.json", "r") as f:
    students = json.load(f)

count = len(students)

with open("Output/output11.json", "w") as f2:
    json.dump({"count": count}, f2, indent=4)

