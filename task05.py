text = input("Matn kiriting: ")
counts = {}

for word in text.split():          
    counts[word] = counts.get(word, 0) + 1

print(counts)            
