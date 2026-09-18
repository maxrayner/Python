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
    length = len(password)
    if length < 8: 
        return "Weak", "X", 0
    elif length < 12:
        return "Medium", "X", 1
    elif length < 16: 
        return "Strong", "✓", 2
    elif length < 20:
        return "Very Strong", "✓", 3
    else:
        return "Extremely Strong", "✓", 4


def checkUpper(password):
    for char in password:
        if char.isupper():
            return "Yes", "✓"
    return "No", "X"

def checkLower(password):
    for char in password:
        if char.islower():
            return "Yes", "✓"
    return "No", "X"


def checkSpecialChar(password):
    for char in password:
        if char in string.punctuation:
            return "Yes", "✓"
    return "No", "X"


def checkNumbers(password):
    for char in password:
        if char in string.digits:
            return "Yes", "✓"
    return "No", "X"

def checkCommon(password,FILENAME):
    try:
        with open(FILENAME,encoding="UTF-8") as f:
            for line in f:
                if password == line.strip():
                    return "Yes", "X"
        return "No", "✓" 
    except FileNotFoundError:
        print("ERROR: File not found")
        return "FNF", "FNF"

def mainOutput():
    print(f"{' PASSWORD SECURITY CHECKER ':=^45}")
    print("")

    password = getPassword()
    correctLength, lengthMarker, overallScore = checkLength(password)
    correctUpper, upperMarker = checkUpper(password)
    correctLower, lowerMarker = checkLower(password)
    correctSpecial, specialMarker = checkSpecialChar(password)
    correctNumber, numberMarker = checkNumbers(password)
    correctCommon, commonMarker = checkCommon(password, FILENAME)

    overallList = [upperMarker,lowerMarker,numberMarker,commonMarker]
    for field in overallList:
        if field == "✓":
            overallScore += 1
    if specialMarker == "✓":
        overallScore += 2


    print(f" \nPassword Analysis\n{"-"*24}")
    output = "{:<24} {:^} {:>}"

    print(output.format("Length:",lengthMarker,correctLength))
    print(output.format("Uppercase Letters:",upperMarker,correctUpper))
    print(output.format("Lowercase Letters:",lowerMarker,correctLower))
    print(output.format("Special Characters:",specialMarker,correctSpecial))
    print(output.format("Numbers:",numberMarker,correctNumber))
    print(output.format("Common Password:",commonMarker,correctCommon))
    
    print(f"\nOverall Analysis: {overallScore}/10")


FILENAME = "common_passwords.txt"
mainOutput()
