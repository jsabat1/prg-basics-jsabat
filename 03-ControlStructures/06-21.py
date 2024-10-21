amount = int(input("Enter the amount in PLN: "))
amount2 = amount
five_pln_coins = 0
two_pln_coins = 0
one_pln_coins = 0

if amount >= 5:
    five_pln_coins = amount // 5
    amount %= 5

if amount >= 2:
    two_pln_coins = amount // 2
    amount %= 2

one_pln_coins = amount
print("The amount of PLN", amount2, "in coins:")
print(f"5 PLN coins: {five_pln_coins}")
print(f"2 PLN coins: {two_pln_coins}")
print(f"1 PLN coins: {one_pln_coins}")
