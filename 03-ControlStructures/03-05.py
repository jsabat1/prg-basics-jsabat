###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1..12)'))
if month==2:
    print('it has 28 days')
elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print('it has 31 days')
else:
    print(' it has 30 days')