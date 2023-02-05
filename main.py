print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

    if add_pepperoni=="Y":

        if size=="S":
            bill+=15 
            bill+=2
            print("Your final bill is: $" + str(bill) )

        if size=="M":
            bill+=20
            bill+=3
            print("Your final bill is: $" + str(bill) )

        if size=="L":
            bill+=25
            bil+=3 
            print("Your final bill is: $" + str(bill) )

    elif add_pepperoni == "N":
        if size=="S":
            bill=15 
            print("Your final bill is: $" + str(bill) )

        if size == "M":
            bill=20
            print("Your final bill is: $" + str(bill) )

        if  size == "L":
            bill=25 
            print("Your final bill is: $" + str(bill) )


if extra_cheese == "Y":
    bill=1

if add_pepperoni == "Y":
