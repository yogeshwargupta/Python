Distance = int(input("Enter the distance in Km: "))

if Distance <0:
    print("Enter a valid distance")
    exit()
elif Distance<3:
    mode = "Walk"
elif Distance<=15:
    mode = "Bike"
else:
    mode = "Car"

print(mode)