password = input("Enter your password: ")
lenght = len(password)

if lenght<6:
    type = "Weak"
elif lenght<=10:
    type = "Medium"
else:
    type = "Strong"

print("Password is", type)