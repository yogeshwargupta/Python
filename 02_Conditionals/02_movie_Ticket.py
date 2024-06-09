age = int(input("Enter your age: "))
day = input("Enter day of Booking: ")

price = 300 if age >= 18 else 200
if day == "Wednesday":
    price -= 50

print("Ticket price for you is Rs.",price)