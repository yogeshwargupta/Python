str = input("Enter input: ")

for char in str:
    if str.count(char) == 1:
        print("Char is:", char)
        break