hours_parked=int(input('How many hours have you been parked?'))
if hours_parked>6:
    print('The fee is 20pln')
elif hours_parked>2:
    print('The fee is 15pln')
else:
    print('The fee is 5pln')