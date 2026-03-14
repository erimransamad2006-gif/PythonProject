text = "banana"
result = ""

for char in text:
    if char not in result:
        result += char

print(result)

#count duplicate
text = "banana"
result = ""
count = 0
for char in text:
    if char not in result:
        result += char
        count = len(result)
print(count)