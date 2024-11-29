###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r') as file:
    email = file.read()

# regular expression pattern
# for amounts (assuming amounts are in the format €123)
pattern = r'€\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
    # remove the euro sign and convert to int
    total += int(amount[1:])

# print result
print(f'Total amount spent: €{total}')