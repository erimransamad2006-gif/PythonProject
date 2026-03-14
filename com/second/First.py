# Take input from user


num = int(input("Enter a number: "))

# Find the number of digits
order = len(str(num))

# Initialize sum
sum = 0

# Temporary variable to store the original number
temp = num

while temp > 0:
    digit = temp % 10          # Get last digit
    sum += digit ** order      # Add digit raised to the power of number of digits
    temp //= 10                # Remove the last digit

# Check if original and sum are same
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")