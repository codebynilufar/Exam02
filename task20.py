students = [
    {'name': 'Ali', 'age': 18},
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Muhammad', 'age': 21}
]

names = [student['name'] for student in students]

shortest = names[0]
for name in names:
    if len(name) < len(shortest):
        shortest = name

print(shortest)

