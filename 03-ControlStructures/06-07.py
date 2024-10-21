age=int(input('Enter your age: '))
if age>=65:
    print('Senior')
elif age>19:
    print('Adult')
elif age>12:
    print('Teen')
else:
    print('Child')