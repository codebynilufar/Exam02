def add(a, b):
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
operation = input("Qaysi amalni bajarmoqchisiz? (+, -, *, / )")

if operation == "+":
    print(add(a, b))
elif operation == "-":
    print(subtract(a, b))
elif operation == "*":
    print(multiply(a, b))
elif operation == "/":
    print(divide(a, b))
else:
    print("Noto'g'ri amal")

