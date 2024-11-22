categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]
max = 0
for i in expenses:
    if i > max:
        max = i
for j in range(len(expenses)):
    if expenses[j] == max:
        print(categories[j], max)
