###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enget 2nd letter')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = last_letter_code-first_letter_code
print(f'Between {first} and {last} is {number_of_letters-1} letters')