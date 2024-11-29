# The file pets.txt contains humorous text about animals. Write a program that prints the text and counts the number of words in the text.

# To calculate the number of words in a line, use the split() method, which splits a string into a list where each word is a list item. Then read the length of this list. Use the len() function. Finally, sum the number of words in each line.
with open("pets.txt", "r") as file:
    words = 0
    for line in file:
        words += len(line.split())
print(words)
