import random
dice_roll_1 = random.randint(1,6)
special= dice_roll_1==1 or dice_roll_1==6
print('Dice roll:', dice_roll_1)
print('Special roll:',special)