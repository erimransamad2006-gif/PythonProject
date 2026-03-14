from django.db.models.functions import Reverse

num = "1234"
print(num)
rev = ""
for char in num:
    rev = char + rev
print(rev)
