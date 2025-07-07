def calculate_tax(salary: float) -> float:
    if salary > 5_000_000:
        tax = salary * 0.2
    else:
        tax = salary * 0.13
    return tax

def calculate_net_salary(salary: float) -> float:
    net_salary = salary - tax 
    return net_salary

salary = float(input("Oylik maoshingizni kiriting: "))

tax = calculate_tax(salary)
net_salary = calculate_net_salary(salary)
print(f"Soliq miqdori: {tax:,.2f}, Sof maosh: {net_salary:,.2f}")
