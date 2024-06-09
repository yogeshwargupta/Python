fruit = input("Enter the name of fruit: ")
color = input("Enter the color of fruit: ")
if fruit=="Banana":   
    if color=="Green":
        print("Banana is Unripe")
    elif color=="Yellow":
        print("Banana is Ripe")
    elif color=="Brown":
        print("Banana is Overripe")
    else:
        print("Please enter correct color!")
else:
    print("OOps! We don't have data of other fruits than banana")