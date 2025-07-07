def deposit(balance, amount):
    new_balance = balance + amount
    return new_balance

def withdraw(balance, amount):
    if amount <= balance:
        new_balance = balance - amount
        return new_balance
    else:
        print("Hisobingizda yetarli mablag' yo'q.")
        new_balance = balance

def check_balance(balance):
    print(f"Sizning balansingiz: {balance} sum")


balance = 1000000   
    
amount = float(input("Qancha deposit qilmoqchisiz? "))
balance = deposit(balance, amount)
check_balance(balance)

amount = float(input("Qancha pul chiqarmoqchisiz? "))
balance = withdraw(balance, amount)
check_balance(balance)