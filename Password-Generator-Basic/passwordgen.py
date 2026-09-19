# Random Password Generator for passwords that need to be changed
# 30/11/2025 - (uploaded to github on 19/09/26)
from random import randint
import string



def display():

    print(f"{' Password Generator ':=^45}\nEnter yes/no/number if required")


def getInput():
    while True:
        try:
            length = int(input("Enter desired length: "))
            if length > 0:
                break
            print("ERROR: Password cannot be less than 1 character long")
        except ValueError:
            print("ERROR: Not an integer")

    while True:
        characters = "" 
        numbers = input("Do you want numbers? (y/n): ").lower() == "y"
        symbols = input("Do you want symbols? (y/n): ").lower() == "y"
        letters = input("Do you want letters? (y/n): ").lower() == "y"
        
        if numbers:
            characters += string.digits
        if symbols:
            characters += "!@#$%^&*"
        if letters:
            characters += string.ascii_letters

        if not characters:
            print("ERROR: Must select at least one character type")
        else:
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

