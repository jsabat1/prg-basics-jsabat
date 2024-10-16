###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('title in capital letters: ',movie.upper())

# print title in small letters
print('title in small letters: ',movie.lower())

# print how many times the vowel "e" appears in the title
print('e appears in title this number of times:', movie.count('e'))

# print where in the text is the word "Lord"
print('Lord: ', movie.find('Lord'))

# print where in the text is the word "dragon"
print('dragon: ', movie.find('dragon'))