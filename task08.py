with open("Input/numbers.txt", "r") as f:
    result = f.read()

numbers = list(map(int, result.split()))
total = sum(numbers)

with open("Output/output08.txt", "w") as f2:
    f2.write(f"Yig'indi: {total}")


