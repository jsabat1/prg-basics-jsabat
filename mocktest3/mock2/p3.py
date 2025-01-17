def f(d):
    total_passengers = sum(d.values())
    num_flights = len(d)
    average_passengers = total_passengers / num_flights

    count = 0
    for passengers in d.values():
        if passengers > average_passengers:
            count += 1

    return count


print(f({"LO231": 150, "BA787": 120, "NZ15": 30}))  # Output: 2
print(f({"LO231": 150, "BA787": 20, "NZ15": 30}))  # Output: 1
