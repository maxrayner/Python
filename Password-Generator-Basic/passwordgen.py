# Random Password Generator for passwords that need to be changed
# 30/11/2025 - (uploaded to github on 19/09/26)
from random import randint
import string



def display():

    print(f"{' Password Generator ':=^45}\nEnter yes/no/number if required")


def getInput():

    length = int(input("Enter desired length: "))
    numbers = input("Do you want numbers? (y/n): ").lower() == "y"
    symbols = input("Do you want symbols? (y/n): ").lower() == "y"
    letters = input("Do you want letters? (y/n): ").lower() == "y"
    characters = ""

    if numbers:
        characters += string.digits
    if symbols:
        characters += "!@#$%^&*"
    if letters:
        characters += string.ascii_letters

    return length, characters

def main():
    display()
    length, characters = getInput()
    password = ""
    for _ in range(length):
        num = randint(0,len(characters)-1)
        password += characters[num]

    print(password)

main()

