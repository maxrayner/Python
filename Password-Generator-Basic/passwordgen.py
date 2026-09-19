# Random Password Generator for passwords that need to be changed
# 30/11/2025 - (uploaded to github on 19/09/26)
from random import randint
import string

split = "-"
characters = string.ascii_letters + string.digits

splits = 5
length = 8

fullword = ""
count = 0

for i in range(splits):
    for j in range(length):
        num = randint(0,len(characters)-1)
        fullword += characters[num]
    if count != splits-1:
        fullword += str(split)
        count += 1

print(fullword)
