# timed mental maths challenge code
# Defaults: Multiplication (2,100) + (2,100), Division is same but reversed (only integers allowed), Addition (2,100) (2, 100), Subtraction (2,100) (2,100)

from random import randint

def multiplication(minimum=2,maximum=100):
    firstMult, secondMult = randint(minimum,maximum), randint(minimum,maximum) #assigning random numbers
    return firstMult, secondMult, "*", firstMult*secondMult #returning both multipliers, symbol and answer

def division(minimum_1=2,maximum_1=1000,minimum_2=2,maximum_2=15):
    firstDiv = 3 #default values to enter loop
    secondDiv = 5
    while max(firstDiv,secondDiv)%min(firstDiv,secondDiv) != 0: #checking if the biggest/smallest gives an integer
        firstDiv, secondDiv = randint(minimum_1,maximum_1), randint(minimum_2, maximum_2) #assigning random numbers
    firstDiv, secondDiv = max(firstDiv,secondDiv),min(firstDiv,secondDiv) #putting numbers in order
    return firstDiv, secondDiv, "/", firstDiv//secondDiv
    

def askResponse(first,second,symbol):
    while True:
        try:
            return int(input(f"{first} {symbol} {second}: "))
        except ValueError:
            print("ERROR: Not an integer")

def checkResponse(response,answer):
    if response == answer:
        return True
    return False

def main():
    first, second, symbol, answer = division()
    response = askResponse(first,second,symbol)
    correct = checkResponse(response, answer)
    if correct:
        print("You got it correct")
    else:
        print(f"You got it wrong the answer was {answer}")

main()
