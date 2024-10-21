# Read a decimal number from the user
decimal_number = int(input("Enter decimal number: "))
decimal_number_2 = decimal_number
binary = ""
if decimal_number == 0:
    binary = "0"
else:
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary = str(remainder) + binary
        decimal_number //= 2

print(f"{decimal_number_2}(10) = {binary}(2)")
