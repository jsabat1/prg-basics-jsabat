ean_13 = input("Enter EAN-13 article number: ")

if len(ean_13) == 13 and ean_13.isdigit():
    print("Article number is correct")
    if ean_13[:3] == "590":
        print("Article manufactured in Poland")
else:
    print("Invalid article number!")