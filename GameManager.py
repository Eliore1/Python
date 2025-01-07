import random
from audioop import minmax
from enum import Enum
from turtledemo.paint import switchupdown

from Player import Player


class STATE(Enum):
    BEGIN = 1
    PLAYING = 2
    PAUSE = 3
    END = 4

class COMMAND(Enum):
    PLAY = "play"
    PAUSE = "pause"
    QUIT = "quit"
    CANCEL = "cancel"
    CONFIRM = "confirm"

class Game:
    def __init__(self):
       self.running = True
       self.state = STATE.BEGIN


       self._hasShowWelcome = False
       self._hasStarted = False


    def run(self):
        while self.running:
            if self.state == STATE.BEGIN:
                self.begin()

            elif self.state == STATE.PLAYING:
                print("You are playing")

            elif self.state == STATE.PAUSE:
                print("You are paused")

            elif self.state == STATE.END:
                print("You are end")

            else:
                quit()
        quit()

    def begin(self):
        if (self._hasShowWelcome == False):
            print("#####################################################\n"
                  "#                                                   #\n"
                  "#  |     W  EEEEE  L      CCCC   OOO  M   M  EEEEE  #\n"
                  "#  W     W  E      L     C      O   O MM MM  E      #\n"
                  "#  W  W  W  EEEE   L     C      O   O M M M  EEEE   #\n"
                  "#  W W W W  E      L     C      O   O M   M  E      #\n"
                  "#   W   W   EEEEE  LLLLL  CCCC   OOO  M   M  EEEEE  #\n"
                  "#                                                   #\n"
                  "#####################################################\n")

            print("           play                       quit           \n")
            self._hasShowWelcome = True

        inputBegin = self.receiveInput()
        if (inputBegin == "play"):
            print("Launching game\n")
            self.state = STATE.PLAYING
        elif (inputBegin == "quit"):
            print("Quitting game\n")
            self.running = False
        else:
            print("Invalid command\n")


    def play(self):
        if self._hasStarted == False:
            pass

    def end(self):
        print("Game ended")
        self.running = False
    random.randrange(0.0, 3.0)

    random.randbytes(0.0, 3.0)
    def receiveInput(self):
        player_input = input("Enter your command: ")
        return player_input

    def startingGame(self):
        self._hasStarted = True
