def f(mnumbers):
    valid_count = 0
    valid_chars = set("1234567abcdABCD")

    for number in mnumbers:
        if number[0] in "+-":
            number = number[1:]
        if all(char in valid_chars for char in number):
            valid_count += 1

    return valid_count


# Example usage:
print(f(["A15", "-31", "7abC", "+D1", "-gH"]))  # Output: 4
print(f(["A05", "-3+1", "7ab8C", "+D1", "-22k"]))  # Output: 1
