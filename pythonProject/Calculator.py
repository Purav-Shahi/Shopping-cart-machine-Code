print ("** Calculation with Purav **")
while True:
    print ("""press 1 to get the are of square 
    press 2 to get the area of rectangle
    press 3 to get the area of circle
    press 4 to get the area of triangle""")

    choice = int(input("Enter the number between 1-4: "))

    if choice == 1:
        while True:
            side = float(input("Enter the length of one side: "))
            area = side**2
            print ("the are of square is",area)
            repeat = input("Do you want to try again with square?")
            if repeat == "no":
                break




    elif choice == 2:
        while True:
            length = float(input("Enter the length of rectangle: "))
            width = float(input("Enter the width of rectangle: "))
            area = length*width
            print ("the area of rectangle",area)
            repeat = input("Do you want to try again with rectangle?")
            if repeat == "no":
                break


    elif choice == 3:
        while True:
            radius = float(input("Enter the radius of circle: "))
            area = ((22/7)*(radius**2))
            print ("the area of circle",area)
            repeat = input("Do you want to try again with circle?")
            if repeat == "no":
                break


    elif choice == 4:
        while True:
            base = float(input("Enter the base of triangle: "))
            height = float(input("Enter the height of triangle: "))
            area = 0.5*base*height
            print ("the area of triangle",area)
            repeat = input("Do you want to try again with triangle?")
            if repeat == "no":
                break


    repeat1 = input("Do you want to repeat the menu again?")
    if repeat =="no":
        break
