car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]


def swap(x, y):
    return y, x


###
# Bubble sort
#
def bubble_sort1(arr):
    help = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if car_fuel_consumption[j] > car_fuel_consumption[j + 1]:
                help = car_fuel_consumption[j]
                car_fuel_consumption[j] = car_fuel_consumption[j + 1]
                car_fuel_consumption[j + 1] = help
    return car_fuel_consumption


def bubble_sort2(arr):
    help = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if bank_transactions[j] > bank_transactions[j + 1]:
                help = bank_transactions[j]
                bank_transactions[j] = bank_transactions[j + 1]
                bank_transactions[j + 1] = help
    return bank_transactions


print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort1(car_fuel_consumption)
print(sorted_car_fuel_consumption)

print(bank_transactions)
sorted_bank_transactions = bubble_sort2(bank_transactions)
print(sorted_bank_transactions)
