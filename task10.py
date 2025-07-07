with open("Input/numbers.txt", "r") as f:
    result = f.read()

numbers = list(map(int, result.split()))
numbers.sort()

with open("Output/output10.txt", "w") as f2:
    f2.write(f"Tartiblanga sonlar: {numbers}")
