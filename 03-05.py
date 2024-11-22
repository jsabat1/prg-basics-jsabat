# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
    ["A", "A", "B", "A", "A"],
    ["A", "B", "B", "A", "A"],
    ["A", "A", "A", "A", "B"],
    ["B", "A", "A", "A", "A"],
    ["A", "B", "A", "A", "A"],
]


def seats_total(seats):
    total = 0
    for i in cinema_seats:
        total += len(i)
    return total


def seats_available(seats):
    total = 0
    for i in cinema_seats:
        for j in i:
            if j == "A":
                total += 1
    return total


def seats_booked(seats):
    total = 0
    for i in cinema_seats:
        for j in i:
            if j == "B":
                total += 1
    return total


def seat_status(seats, row, place):
    if seats[row - 1][place - 1] == "A":
        return "Available"
    else:
        return "Booked"


print("CINEMA INFORMATION TABLE")
print("Total seats:", seats_total(cinema_seats))
print("Seats available:", seats_available(cinema_seats))
print("Seats booked:", seats_booked(cinema_seats))
print("Seat in row 1, place 1:", seat_status(cinema_seats, 1, 1))
print("Seat in row 5, place 5:", seat_status(cinema_seats, 5, 5))
print("Seat in row 3, place 5:", seat_status(cinema_seats, 3, 5))
