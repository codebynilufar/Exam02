import json

with open("Input/students.json", "r") as f:
    students = json.load(f)

names = [student["name"] for student in students]
names.sort()

with open("Output/output12.json", "w") as f2:
    json.dump({"sorted_names": names}, f2, indent=4)
