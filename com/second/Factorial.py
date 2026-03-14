count = 7

first = 0
second = 1

print(first, second)

for i in range(count - 2):
    next_number = first + second
    print(next_number)

    first = second
    second = next_number