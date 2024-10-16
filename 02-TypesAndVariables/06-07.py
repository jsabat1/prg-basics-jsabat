###
# A program that prints a numerical representation of each letter of your name.
#
name = 'Jakub' # replace John with your name
for i in range(0,len(name)):
    print(f'The letter {name[i]} has a code {ord(name[i])}')