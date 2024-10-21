###
# A program that prints your height both in cm and in feet and inches.
#
cm = 183
inches = cm/2.54
feet=inches//12
# calculate the number of feet
inches = inches - feet*12
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')