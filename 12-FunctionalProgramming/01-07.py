# Define an anonymous function to check if a number is even
is_even = lambda number: number % 2 == 0

# Test the function with some examples
test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print the results
for number in test_numbers:
    print(f"{number} is even: {is_even(number)}")