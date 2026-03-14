# Take input from user
num = int(input("Enter a number: "))

# Prime numbers are greater than 1
if num > 1:
    print(num ** 0.5+1)
    for i in range(2, int(num ** 0.5) + 1):  # only check up to square root
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
