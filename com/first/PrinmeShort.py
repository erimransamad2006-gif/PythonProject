import math

num = int(input("Enter the number"))

for looptillno in range(2, int(math.sqrt(num)) + 1):
    if (num % looptillno == 0):
        print("NOT a prime number")
        break
else:
        print("Yes its prime number")
