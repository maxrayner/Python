# Boxing OOP challenge/game
#imports

from random import randint


class Boxer:
    # constructor and attributes
    def __init__(self,name,power,defence,health=100,stamina=100):
        self.__name = name 
        self.__power = power # multiplier of damage (power//50)
        self.__defence = defence # increases chance of defence 
        self.__health = health # overall starting health
        self.__stamina = stamina # overall starting stamina

    # getter and setter methods
    def getName(self):
        return self.__name

    def getPower(self):
        return self.__power

    def getDefence(self):
        return self.__defence

    def getHealth(self):
        return self.__health

    def getStamina(self):
        return self.__stamina

    def setHealth(self, health):
        self.__health = health

    def setStamina(self, stamina):
        self.__stamina = stamina
    
    # main methods
    def punch(self,attack,opponent):
        damage = attack.getDamage()
        stamina = attack.getStamina()
        

    def defend(self):
        pass


class Attack:
    def __init__(self,damage,stamina):
        self.__damage = damage
        self.__stamina = stamina

    def getDamage(self):
        return self.__damage

    def getStamina(self):
        return self.__stamina

        

class Defend:
    def __init__(self):
        pass


# Options of attacking (add overhands, body/head later)
jab = Attack(3,1)
straight = Attack(9,4)
leadHook = Attack(15,7)
rearHook = Attack(20,8)
leadUppercut = Attack(18,6)
rearUppercut = Attack(26,7)


# Options of defending
slip = Defend()
parry = Defend()
roll = Defend()
dip = Defend()
weaving = Defend()
footwork = Defend()
blocking = Defend()
clinching = Defend()


# main game function
def getIntInput(message):
    return int(input(message))

def getInput(message):
    return input(message)

def main():
    print("Boxing Simulator\nBelow you can customise your character")
    userBoxer = Boxer(getInput("Enter name: "),getIntInput("Enter power: "),getIntInput("Enter defence: "),getIntInput("Enter health: "),getIntInput("Enter stamina: "))
    if getIntInput("Do you want to play against a machine (1) or a friend (2): ") == 1:
        machineBoxer = Boxer(getInput("Enter opponents name: "),randint(50,100),randint(50,100))

    



if __name__ == "__main__":
    main()