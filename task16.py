import csv

with open("Input/grades.csv", "r") as f:
    students = list(csv.DictReader(f))

max_grade = max(int(s["grade"]) for s in students)

top_students = [s["name"] for s in students if int(s["grade"]) == max_grade]

with open("Output/output16.txt", "w") as f2:
   
 f2.write(f"Bahosi eng yuqori o‘quvchilar: {top_students}")
