students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}

average = sum(students) / len(students)
print("O'rtacha ball:", average)

for name in students:
    if students[name] > average:
        print(name)



