import Player


class Wyvern:
    def __init__(self, life:int, damage:int):
        self.life = life
        self.damage = damage

    def attack(self, player:Player):
        player.life -= self.damage

    def isDead(self):
        return self.life > 0