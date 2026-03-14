txt = input("Enter to check Palindrome")

if txt == txt[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")