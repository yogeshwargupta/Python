weather = input("How is the weather: ")

if weather=="Sunny":
    activity = "Go for a walk"
elif weather=="Rainy":
    activity = "Read a book"
elif weather=="Snowy":
    activity = "Build a snowman"
else:
    print("Enter correct weather")
    exit()

print(activity)