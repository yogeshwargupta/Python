marks = int(input("Enter your marks: "))

if marks<0 or marks>100:
    print("Enter a valid marks")
elif marks<60:
    print("You grade is: F")
elif marks<70:
    print("You grade is: D")
elif marks<80:
    print("You grade is: C")
elif marks<90:
    print("You grade is: B")
else:
    print("You grade is: A")