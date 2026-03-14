student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "grades": [88, 92, 79],
    "is_enrolled": True
}

print("1", student)
print("K : ",student.keys())
print("V : ",student.values())
print(student.items())
print("********")
for key, value in student.items():
    print("KEYS and VALUES", key, value)   # key-value pairs

print("********")
for key in student.keys():
    print("KEY:", key)          # just the keys

print("********")
for value in student.values():
    print("VALUE:", value)      # just the values
