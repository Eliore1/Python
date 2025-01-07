from enum import Enum
from turtledemo.paint import switchupdown

from Player import Player


class STATE(Enum):
    BEGIN = 1
    PLAYING = 2
    PAUSE = 3
    END = 4

class Game:
    def __init__(self):
       self.running = True
       self.state = STATE.BEGIN

    def run(self):
        while self.running:
            if self.state == STATE.BEGIN:
                print("WElCOME !")
                print("play     quit")
                input1  = input("Enter your action : ")
                if (input1 == "play"):
                    self.state = STATE.PLAYING
                elif (input1 == "quit"):
                    print("your are quitting")
                    self.running = False
                else:
                    print("invalid input")
            elif self.state == STATE.PLAYING:
                print("You are playing")


    def end(self):
        pass