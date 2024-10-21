###
# Program that simulates the operation of an electronic thermometer.
#
temperature = -2
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print ('it is hot')
elif temperature > 14:
    print ('it is warm')
elif temperature >= 0:
    print ('it is cold')
else:
    print('warning, frost')