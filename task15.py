import csv

with open("Input/grades.csv", "r", encoding="utf-8") as f:
    students = list(csv.DictReader(f))

top_student = max(students, key=lambda s: int(s["grade"]))

with open("Output/output15.txt", "w") as f2:
    f2.write(f"Bahosi eng yuqori o‘quvchi: {top_student['name']} ({top_student['grade']})")
