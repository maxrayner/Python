# Boxing OOP challenge/game
#imports

from random import randint


class Boxer:
    # constructor and attributes
    def __init__(self,name,power,defence,health=100,stamina=100):
        self.__name = name
        self.__power = power
        self.__defence = defence
        self.__health = health
        self.__stamina = stamina

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
        pass

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
jab = Attack(5,1)
straight = Attack()
leadHook = Attack()
rearHook = Attack()
leadUppercut = Attack()
rearUppercut = Attack()


# Options of defending
slip = Defend()
parry = Defend()
roll = Defend()
dip = Defend()
weaving = Defend()
footwork = Defend()
blocking = Defend()
clinching = Defend()
