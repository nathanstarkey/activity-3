# Activity 3
# sets while loop for continue choice
choice = "y"
while choice.lower() == "y":
    print("You will be asked the number of board feet for the purchase and the type of lumber (common or select)")
    board_feet = int(input("Enter number of board feet: \t\t"))
    lumber = int(input("Enter a 1 for select lumber or a 2 for common lumber: \t"))
    select = 2
    common = 1
    discount = 0
    price = 0
# gets price for lumber based off of choice.
    if lumber == 1:
        price = board_feet * 2
    elif lumber == 2:
        price = board_feet * 1
    else:
        print("That is not a valid number. Please enter either a 1 or a 2.")
        break
# adds discount if needed based off of price of lumber.
    if price >= 10000 and price <= 49999:
        price -= price * 0.1
    elif price >= 50000:
        price -= price * 0.2

    print("Total price for the lumber is " + f'{price:,}')
    choice = input ("Continue? y/n: ")
print("Bye!")
# Done!
