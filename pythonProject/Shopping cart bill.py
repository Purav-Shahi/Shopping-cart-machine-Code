while True:
    name = input("Enter customer name: ")
    total = 0

    while True:
        print ("Enter the amount and quantity ")
        amount = float(input("Enter amount: "))
        quantity = float(input("Enter quantity: "))
        total += amount * quantity
        repeat = input("Do you want to add more items? (Yes/no):")
        if repeat == "no" or repeat =="No":
             break

    print ("-"*45)
    print ("Name",name)
    print ("Amount to be paid: ", total)
    print ("-"*45)
    print ("**************Happy shopping**************")

    repeat1 = input("do you want to go to next customer? (Yes/no):")
    if repeat1 == "no" or repeat == "No":
        break