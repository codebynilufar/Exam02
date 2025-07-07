names = ['Ali', 'Diyor', 'Jasurbek', 'Muhammad']

longest = names[0]
for name in names:
    if len(name) > len(longest):
        longest = name

print(longest)
