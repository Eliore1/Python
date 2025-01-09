import random
from enum import Enum
from Player import Player
from Map import Map
from Ennemies import Wyvern

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

       self.player = Player("Default", 10,4)
       self.wyvern = Wyvern(10,3)

#   Core functions
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
        Game.welcomeMessage()
        print("           play                       quit           \n")

        inputBegin = Game.getInput(Game.getCommandRequestMessage(), ["play", "quit"])

        if (inputBegin == "play"):
            inputName = input("Enter your name: ")
            self.player.name = inputName
            print("Here are your stats : \n")
            print(self.player)
            print("Good luck " + inputName + '\n')
            print("Launching game\n")
            self.state = STATE.PLAYING
        elif (inputBegin == "quit"):
            print("Quitting game\n")
            self.running = False


    def play(self):
        self.beginStory()

        if self.state == STATE.END:
            return

        inputPath = Game.getInput("After long hours of climbing you arrived at cross path, wich way will you choose : (left/right) \n", ["left", "right"])
        if (inputPath == "left"):
            print("It was not a wise choice, due to a rock falling you loose 2 hp...\n")
            self.player.life -= 2
        elif (inputPath == "right"):
            print("It was a good choice\n")

        print("You arrived at the entry of a cave and entered it, as you walk inside you see 2 way. \n"
              
              "One is leading to something like a ruin and the other go deeper inside the cave")
        inputEntry = input("Enter your choice (deeper/ruin : \n")
        while inputEntry != "deeper" and inputEntry != "ruin":
            print("Invalid input. Please try again.")
            inputEntry = input("Enter your choice (deeper/ruin : \n")
        if inputEntry == "ruin":
            print("You see a chest. Will you open it?")
            inputChest = input("Enter your choice: (y/n)\n")
            while inputChest != "y" and inputChest != "n":
                inputChest = input("Invalid input. Please try again: (y/n)\n")
            if inputChest == "y":
                print("You have found a healing potion, congratulations!\n")
                print("You go back to the other way deeper\n")
                self.player.potions += 1
            elif inputChest == "n":
                print("You go back to the other way deeper\n")

        print("You arrived at the entry of the wyvern nest, there lie the dreadful create\n")
        print("What will you do?\n ")
        print("Fight \n")
        print("Run \n")
        inputWyvern = input("Enter your choice: (Fight/Run) \n")
        while inputWyvern != "Run" and inputWyvern != "Fight":
            print("Invalid input. Please try again.")
            inputWyvern = input("Enter your choice: ")
        if inputWyvern == "Fight":
            while not self.player.isDead() and not self.wyvern.isDead():
                inputChoice = input("What do you do? Deal a blow or use a potion (blow/potion) \n:")
                while inputChoice != "blow" and inputChoice != "potion":
                    print("Invalid input. Please try again.")
                    inputChoice = input("Enter your choice: ")
                if inputChoice == "potion":
                    if self.player.potions > 0:
                        self.player.potions -= 1
                        self.player.life += 2
                        print("You use a potion, you have now " + str(self.player.life) + " hp\n")
                    else:
                        print("You don't have any potions\n")
                else:
                    sucess = Dnd.roll(self.player.strength, 15)
                    if sucess:
                        print("You successfully deal a blow!\n")
                        self.wyvern.life -= self.player.damage
                        print("You deal " + str(self.player.damage) + " damage.\n")
                        print("The wyvern have" + str(self.wyvern.life) + " hp.\n")
                    elif sucess == False:
                        print("bad luck ! you failed\n")
                        print("you received " + str(self.wyvern.damage) + " damage.\n")
                        self.player.life -= self.wyvern.damage
                        print("You have  " + str(self.player.life) + " hp\n")
            if (self.wyvern.life > self.player.life):
                print("You loose !!!")
            else:
                print("You win !!!")
            self.state = STATE.END
            return
        elif inputWyvern == "Run":
            print("The wyvern catch you while you were trying to flee and swallow you...")
            self.state = STATE.END
            return


    def end(self):
        print("Game ended")
        inputRestart = input("Do you want to play again? (y/n)")
        if inputRestart == "y":
            self.state = STATE.BEGIN
            #restart stat
        elif inputRestart == "n":
            self.running = False


    # Statics functions
    @staticmethod
    def welcomeMessage():
        print("#####################################################\n"
              "#                                                   #\n"
              "#  |     W  EEEEE  L      CCCC   OOO  M   M  EEEEE  #\n"
              "#  W     W  E      L     C      O   O MM MM  E      #\n"
              "#  W  W  W  EEEE   L     C      O   O M M M  EEEE   #\n"
              "#  W W W W  E      L     C      O   O M   M  E      #\n"
              "#   W   W   EEEEE  LLLLL  CCCC   OOO  M   M  EEEEE  #\n"
              "#                                                   #\n"
              "#####################################################\n")

    @staticmethod
    def getInput(message:str, choices:list) -> str:
        userInput = input(message)
        while userInput not in choices:
            print("Invalid input. Please try again.")
            userInput = input(message).strip().lower()
        return userInput

    @staticmethod
    def getCommandRequestMessage() ->str:
        return "Enter your command: "

    # Story functions
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

    def handleRuin(self):
        pass

