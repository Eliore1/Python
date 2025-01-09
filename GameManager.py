import random
from enum import Enum
from Player import Player
from Map import Map


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


class Dnd:
    def __init__(self):
        pass

    @staticmethod
    def roll(stat:int, difficulty:int):
        roll = random.randint(1, 20)
        if roll + stat >= difficulty:
            return True
        return False

class Game:
    def __init__(self):
       self.running = True
       self.state = STATE.BEGIN

       self._hasStarted = False
       self.test = False

       self.player = Player("Default", 10)


    def run(self):
        while self.running:
            if self.state == STATE.BEGIN:
                self.begin()

            elif self.state == STATE.PLAYING:
                self.play()

            elif self.state == STATE.PAUSE:
                print("You are paused")

            elif self.state == STATE.END:
                self.end()

            else:
                quit()
        quit()

    def begin(self):
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

        inputBegin = input("Enter your command: ")
        while inputBegin != "play" and inputBegin != "quit":
            print("Invalid input. Please try again.")
            inputBegin = input("Enter your command: ")

        if (inputBegin == "play"):
            inputName = input("Enter your name: ")
            self.player.name = inputName
            print("Here are your stats : \n")
            print(self.player)
            inputConfirm = input("Do you want to continue? (y/n) ")
            print("Good luck " + inputName + '\n')
            print("Launching game\n")
            self.state = STATE.PLAYING
        elif (inputBegin == "quit"):
            print("Quitting game\n")
            self.running = False


    def play(self):
        self.beginStory()

        inputPath = input("After long hours of climbing you arrived at cross path, wich way will you choose : (left/right) \n")
        while inputPath != "left" and inputPath != "right":
            print("Invalid input. Please try again.")
            inputPath = input("(left/right) : \n)")
        if (inputPath == "left"):
            print("It was not a wise choice, due to a rock falling you loose 2 hp...\n")
            self.player.life -= 2
        elif (inputPath == "right"):
            print("It was a good choice\n")

        print("You arrived at the entry of a cave and entered it, there a beautiful but dreadful wyvern is waiting for you. \n")
        # modifier pour rajouter le choix de check avant pour pas casser les couilles

        print("What will you do?\n ")
        print("Fight \n")
        print("Run \n")
        print("Check the surrounding\n")
        inputWyvern = input("Enter your choice: (Fight/Run/Check) \n")
        while inputWyvern != "Run" and inputWyvern != "Fight" and inputWyvern != "Check":
            print("Invalid input. Please try again.")
            inputWyvern = input("Enter your choice: ")
        if inputWyvern == "Check":
            print("You see a chest. Will you open it?")
            inputChest = input("Enter your choice: (y/n)\n")
            while inputChest != "y" and inputChest != "n":
                inputChest = input("Invalid input. Please try again: (y/n)\n")
            if inputChest == "y":
                print("You have found a healing potion, congratulations!\n")
                self.player.potions += 1
            elif inputChest == "n":
                print("You go back to the wyvern nest\n")

        if inputWyvern == "Fight":
            sucess = Dnd.roll(self.player.strength, 15)
            print("fight")
            if sucess:
                print("You have sucessful fight.")
                self.state = STATE.END
                return
        elif inputWyvern == "Run":
            print("The wyvern catch you while you were trying to flee and swallow you...")
            self.state = STATE.END
            return


    def end(self):
        print("Game ended")
        input = input("Do you want to play again? (y/n)")
        if (input == "y"):
            self.state = STATE.BEGIN
        else:
            self.running = False

    def beginStory(self):
        print("In the heart of the Greystone Mountains, the peaceful village of Greystone was plagued by a terrible threat. Each night, a shadowy wyvern descended, snatching sheep and cattle, leaving the villagers in terror.\n" +
              "Desperate they turn to you and seek for help \n")

        inputBegin = input("Will you helped them: (y/n)\n")
        while inputBegin != "y" and inputBegin != "n":
            print("Invalid input. Please try again.")
            inputBegin = input("Will you helped them: (y/n)\n")
        if (inputBegin == "y"):
            pass
        elif (inputBegin == "n"):
            print("Coward ! Say the village chief before murdering you...\n")
            self.state = STATE.END

