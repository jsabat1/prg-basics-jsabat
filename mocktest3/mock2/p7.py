def f(d):
    car_park = {}

    for entry in d:
        reg_number, action = entry
        if action == "in":
            car_park[reg_number] = car_park.get(reg_number, 0) + 1
        elif action == "out":
            if reg_number in car_park and car_park[reg_number] > 0:
                car_park[reg_number] -= 1

    remaining_cars = [car for car, count in car_park.items() if count > 0]
    return sorted(remaining_cars)


# Example usage
cars = [
    ["KR234", "in"],
    ["BA123", "in"],
    ["GX444", "in"],
    ["KR234", "out"],
    ["BA111", "in"],
    ["BA123", "out"],
    ["KR234", "in"],
]
print(f(cars))  # Output: ["BA111", "GX444", "KR234"]

cars1 = [["KR234", "in"], ["KR234", "out"]]
print(f(cars1))  # Output: []
