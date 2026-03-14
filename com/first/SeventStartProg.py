numbers = [5, 1, 1, 4, 1, 1, 1]  # pattern for letter F

# first way
"""for i in number:
    print(i*"*")
    print("---------SECOND---------------")"""
# second way
for x_count in numbers:
    output = ""
    for count in range(x_count):
        output += "X"
    print(output)
