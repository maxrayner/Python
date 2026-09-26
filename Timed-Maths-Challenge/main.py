# timed mental maths challenge code
# Defaults: Multiplication (2,100) + (2,100), Division is same but reversed (only integers allowed), Addition (2,100) (2, 100), Subtraction (2,100) (2,100)

from random import randint

def multiplication(minimum=2,maximum=100):
    firstMult, secondMult = randint(minimum,maximum), randint(minimum,maximum)
    answer = firstMult * secondMult
    return firstMult, secondMult, "*", answer

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
    first, second, symbol, answer = multiplication()
    response = askResponse(first,second,symbol)
    correct = checkResponse(response, answer)
    if correct:
        print("You got it correct")
    else:
        print(f"You got it wrong the answer was {answer}")

main()
