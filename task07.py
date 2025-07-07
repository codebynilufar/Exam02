cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}

total = 0

for item in cart:
    total += cart[item]['price'] * cart[item]['quantity']

print("Umumiy summa:", total)


