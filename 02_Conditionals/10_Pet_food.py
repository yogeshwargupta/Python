pet = input("Enter type of pet: ")
age = int(input("Enter the age of pet: "))

if pet=="Dog" and age<2:
    food = "Puppy food"
elif pet=="Dog" and age<5:
    food = "Jr. Dog food"
elif pet=="Dog" and age>=5:
    food = "Sr. Dog food"
elif pet=="Cat" and age<2:
    food = "Kitten food"
elif pet=="Cat" and age<5:
    food = "Jr. Cat food"
elif pet=="Cat" and age>=5:
    food = "Sr. Cat food"
else:
    print("OOps! We don't have info of other pets than dog and cat")
    exit()

print("Type of food to be served is:",food)