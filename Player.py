import random

class Player:
    def __init__(self, name:str, life:int, damage:int):
        self.name:str = name
        self.life:int = life
        self.damage:int = damage
        self.potions = 0

        self.strength:int = random.randint(-5,5)
        self.dexterity:int = random.randint(-5,5)
        self.constitution:int = random.randint(-5,5)
        self.intelligence:int = random.randint(-5,5)
        self.wisdom:int = random.randint(-5,5)
        self.charisma:int = random.randint(-5,5)

    def __str__(self):
        return "strength : " + str(self.strength) + '\n' + "dexterity :" + str(self.dexterity) + '\n' + "constitution : " + str(self.constitution) + '\n' + "intelligence : " + str(self.intelligence) + '\n' + "wisdom : " + str(self.wisdom) + '\n' + "charisma : " + str(self.charisma) + '\n'

    def attack(self, target):
        pass

    def talk(self, target):
        pass

    def defend(self, target):
        pass

    def run(self):
        pass

    def isDead(self):
        if self.life <= 0:
            return True
        return False



