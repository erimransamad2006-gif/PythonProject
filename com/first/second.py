import re

message = "python programming"
course = "Python for beginners"

print("Title:", message.title())  # 'Python Programming'
print("Find 'P':", message.find("P"))  # -1 for 1st index and same -1 for the word that not there i.e Z
print("Replace 'Python' with 'Java':", message.replace("Python", "Java"))  # unchanged, case sensitive
print("Replace 'python' with 'Java':", message.replace("python", "Java"))  # 'Java programming'
contains = "Python" in course
print("Contains 'Python' in course:", contains)  # True

message1 = "python programming"
new_message = re.sub("python", "Java", message1, flags=re.IGNORECASE)

print(new_message)  # Java programming