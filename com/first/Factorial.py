num =  int(input("Enter the num for Fac"))

def Fact(num):
    try:
        factorial = 1
        for i in range(1, num+1):
                factorial  = factorial * i
        print(factorial)
    except ValueError:
        print("ValueError")
Fact(num)