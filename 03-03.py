# The data below represents monthly expenses divided into categories and weeks. Write a program that calculates and prints:

# total expenses for each category
# total expenses for each week
# total expenses for a month

# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
    [200, 50, 100],  # Week 1
    [180, 60, 110],  # Week 2
    [220, 55, 105],  # Week 3
    [210, 65, 95],  # Week 4
]
week1 = 0
week2 = 0
week3 = 0
week4 = 0
food = 0
transport = 0
utilities = 0
total = 0
for i in monthly_expenses:
    for j in i:
        if monthly_expenses.index(i) == 0:
            week1 += j
        elif monthly_expenses.index(i) == 1:
            week2 += j
        elif monthly_expenses.index(i) == 2:
            week3 += j
        elif monthly_expenses.index(i) == 3:
            week4 += j
        if i.index(j) == 0:
            food += j
        elif i.index(j) == 1:
            transport += j
        elif i.index(j) == 2:
            utilities += j
        total += j
print("MONTHLY EXPENSES")
print("----------------")
print("Food:", food)
print("Transport:", transport)
print("Utilities:", utilities)
print("Week 1:", week1)
print("Week 2:", week2)
print("Week 3:", week3)
print("Week 4:", week4)
print("---------------")
print("TOTAL:", total)
print("---------------")
