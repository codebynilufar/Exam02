with open("Input/numbers.txt", "r") as f:
    result = f.read()

numbers = list(map(int, result.split()))
total = max(numbers)

with open("Output/output09.txt", "w") as f2:
    f2.write(f"Eng katta son: {total}")
