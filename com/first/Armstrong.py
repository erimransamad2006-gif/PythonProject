number = 153
original = number
total = 0

while number > 0:
    digit = number % 10  # 3
    total = total + digit ** 3 # 27
    number = number // 10  # 15

if total == original:
    print("Armstrong")
else:
    print("Not")

