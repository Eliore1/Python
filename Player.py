import random

class Player:
    def __init__(self, name:str):
        self.name:str = name

        self.strength:int = random.randint(-5,5)
        self.dexterity:int = random.randint(-5,5)
        self.constitution:int = random.randint(-5,5)
        self.intelligence:int = random.randint(-5,5)
        self.wisdom:int = random.randint(-5,5)
        self.charisma:int = random.randint(-5,5)

    def __str__(self):
        return "strength : " + str(self.strength) + '\n' + "dexterity :" + str(self.dexterity) + '\n' + "constitution : " + str(self.constitution) + '\n' + "intelligence : " + str(self.intelligence) + '\n' + "wisdom : " + str(self.wisdom) + '\n' + "charisma : " + str(self.charisma) + '\n'




