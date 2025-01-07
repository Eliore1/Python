

class Player:
    def __init__(self, name:str, max_life:float, base_damage:float, level:int, experience:int):
        self.name = name

        self.max_life = max_life
        self.life = max_life

        self.base_damage = base_damage
        self.damage = base_damage

        self.level = level
        self.experience = experience


