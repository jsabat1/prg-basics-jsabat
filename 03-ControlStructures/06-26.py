correct_pin = "0805"
attempts = 3

for i in range(attempts):
    entered_pin = input("Enter the PIN code: ")

    if entered_pin == correct_pin:
        print("Access granted.")
        break
    else:
        print("Incorrect...")
        if i == attempts - 1:
            print("Sorry, your payment card has been blocked.")
