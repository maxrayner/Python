#16/09/2026
#Password security checker 
#Checks -> Length, Uppercase, Lowercase, Special Characters, Numbers

import string

def getPassword():
    password = ""
    while not password:
        password = input("Enter password: ")
    return password

def checkLength(password):
    if len(password) >= 16:
        return True
    return False

def checkUpper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def checkLower(password):
    for char in password:
        if char.islower():
            return True
    return False


def checkSpecialChar(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False


def checkNumbers(password):
    for char in password:
        if char in string.digits:
            return True
    return False
    
def mainChecks():
    password = getPassword()
    correctLength = checkLength(password)
    correctUpper = checkUpper(password)
    correctLower = checkLower(password)
    correctSpecial = checkSpecialChar(password)
    correctNumber = checkNumbers(password)
    print(correctLength,correctUpper,correctLower,correctSpecial,correctNumber)

mainChecks()
