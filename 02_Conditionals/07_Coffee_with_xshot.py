order_size = input("Please enter the coffee size: ")
extra_shot = bool(input("Do you need extra shot: "))

if extra_shot:
    coffee = order_size + " coffee with extra shot"
else:
    cofee = order_size + "coffee"

print("Order: ",coffee)