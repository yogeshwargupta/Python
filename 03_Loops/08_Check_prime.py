num = int(input("Enter the num to check: "))
is_prime = True

if num>1:
    for i in range(2,num):
        if num%i==0:
            is_prime = False
            break
print(is_prime)