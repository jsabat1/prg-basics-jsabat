###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print('5.check pin')
    print('6.change pin')

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    elif choice == '4':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    elif choice == '5':
        print(f'your pin is {pin}')
    elif choice == '6':
        entered_pin=int(input('enter your current pin: '))
        if entered_pin!=pin:
            print('incorrect pin try again later')
        else:
            new_pin=input('Enter new pin: ')
            if new_pin.isdigit():
                print('pin updated')
                pin=new_pin
                continue
            else:
                print('incorrect pin try again')
                continue
    else:
        print("Invalid option. Please try again.")