import random
from enum import Enum
import os
import sys

import GameManager
from Player import Player
from Ennemies import Wyvern
import Pnj
import pytest

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
       self.running:bool = True
       self.state:STATE = STATE.BEGIN

       self._hasStarted:bool = False
       self.test:bool = False

       self.player:Player = Player("Default", 10,4)
       self.wyvern:Wyvern = Wyvern(10,3)
       self.pnj:Pnj
       self.createVillager()

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
                assert False, "Unknown state"
        quit()

    def begin(self):
        Game.welcomeMessage()
        print("           play                       quit           \n")

        inputBegin = Game.getInput(Game.getCommandRequestMessage() + "(play/quit): ", ["play", "quit"])

        if Game.checkAnwser(inputBegin, "play"):
            inputName = input("Enter your name: ")
            self.player.name = inputName
            print("Here are your stats : \n")
            print(self.player)
            print("Good luck " + inputName + '\n')
            print("Launching game\n")
            self.state = STATE.PLAYING
        elif Game.checkAnwser(inputBegin, "quit"):
            print("Quitting game\n")
            self.running = False



    def play(self):
        self.handleVillage()

        if self.state != STATE.PLAYING:
            return

        print("After long hours of climbing you arrived at cross path, wich way will you choose")
        inputPath = Game.getInput(Game.getCommandRequestMessage() + "(left/right) :", ["left", "right"])
        if Game.checkAnwser(inputPath, "left"):
            print("It was not a wise choice, due to a rock falling you loose 2 hp...\n")
            self.player.life -= 2
        elif Game.checkAnwser(inputPath, "right"):
            print("It was a good choice\n")

        print("You arrived at the entry of a cave and entered it, as you walk inside you see 2 way. \n"
              
              "One is leading to something like a ruin and the other go deeper inside the cave")

        inputEntry = Game.getInput(Game.getCommandRequestMessage() + "(deeper/ruin) : \n", ["deeper", "ruin"])
        if Game.checkAnwser(inputEntry, "deeper"):
            pass
        elif Game.checkAnwser(inputEntry, "ruin"):
            self.handleRuin()

        print("You arrived at the entry of the wyvern nest, there lie the dreadful create\n")
        print("What will you do?\n ")
        print("Fight \n")
        print("Run \n")
        inputWyvern = Game.getInput(Game.getCommandRequestMessage() + " (fight/run): ", ["fight", "run"])
        if Game.checkAnwser(inputWyvern, "fight"):
            self.handleWyvernFight()
        elif inputWyvern == "run":
            print("The wyvern catch you while you were trying to flee and swallow you...")
            self.state = STATE.END
            return


    def end(self):
        print("Game ended")
        print(self.state)
        inputRestart = Game.getInput("Do you want to play again? (y/n) : \n", ["y","n"])
        if Game.checkAnwser(inputRestart, "y"):
            self.state = STATE.BEGIN
            print("Restarting...")

        elif Game.checkAnwser(inputRestart, "n"):
            print("Game Shutdown")
            quit()


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
    def checkAnwser(input:str, choice:str) -> bool:
        if input == choice:
            return True
        return False

    @staticmethod
    def getCommandRequestMessage() ->str:
        return "Enter your command: "

    @staticmethod
    def loose(game:GameManager):
        game.state = STATE.END
        game.end()

    @staticmethod
    def givePotion(game:GameManager):
        game.player.potions += 1


    # Story functions
    def createVillager(self):
        # Main Dialogue
        introDialogues = [
            "Villager: Hey you! What do you want?\n",
            "Villager: Why have you come to this place? *Asks the villager angrily*\n"
        ]

        # Main choices and responses
        dict_main = {
            "You: Just checking around\n": Pnj.Line(
                "Villager: There is nothing to see around here. Don't lie! *He pulls out a dagger.*\n"
            ),
            "You: I'm a hunter and looking for work\n": Pnj.Line(
                "Villager: OH, a hunter!? I might have something for you. Sorry for being rude.\n"
            )
        }

        # Sub-dialogue for "Just checking around"
        subIntro1 = ["Villager: *He approaches you.*\n"]
        subDict1 = {
            "Villager: *He stabs you and takes all your belongings.*\n": Pnj.Line(
                "GAME OVER.\n", action=lambda: GameManager.Game.loose(self)
            )
        }
        subDialogue1 = Pnj.Dialogue(subIntro1, subDict1)

        # Sub-dialogue for "I'm a hunter and looking for work"
        subIntro2 = ["Villager: We need your help! There's a dangerous beast nearby. Will you help us?\n"]
        subDict2 = {
            "You: No, I can't help you\n": Pnj.Line(
                "Villager: Coward! *He and the other villagers kill you on the spot.* GAME OVER.\n",
                action=lambda: GameManager.Game.loose(self)
            ),
            "You: Yes, I'll help you\n": Pnj.Line(
                "Villager: Thank you! The village is counting on you. *He hands you a potion.*\n",
                action=lambda: GameManager.Game.givePotion(self)
            )
        }
        subDialogue2 = Pnj.Dialogue(subIntro2, subDict2)

        # Linking sub-dialogues
        linkedDialogues = [subDialogue1, subDialogue2]

        # Main Dialogue Object
        mainDialogue = Pnj.Dialogue(introDialogues, dict_main, linkedDialogues)
        dialogues = [mainDialogue]

        # Assign to the NPC
        self.pnj = Pnj.Pnj(dialogues)



    def handleVillage(self):
        print("In the heart of the Greystone Mountains, the peaceful village of Greystone. You entered the village in the evening\n")
        self.pnj.interactPlayer()

    def handleRuin(self):
        print("You see a chest. Will you open it?")
        inputChest = Game.getInput(Game.getCommandRequestMessage() + "(y/n) :", ["y", "n"])
        if Game.checkAnwser(inputChest, "y"):
            print("You have found a healing potion, congratulations!\n")
            print("You go back to the other way deeper\n")
            self.player.potions += 1
        elif Game.checkAnwser(inputChest, "n"):
            print("You go back to the other way deeper\n")

    def handleWyvernFight(self):
        while not self.player.isDead() and not self.wyvern.isDead():
            print("What do you do? Deal a blow or use a potion (blow/potion) \n:")
            inputChoice = Game.getInput(Game.getCommandRequestMessage() + "(blow/potion) : ", ["blow", "potion"])
            if Game.checkAnwser(inputChoice, "blow"):
                sucess = Dnd.roll(self.player.strength, 10)
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
                    print("You don't have any potions\n")
            elif Game.checkAnwser(inputChoice, "potion"):
                if self.player.potions > 0:
                    self.player.potions -= 1
                    self.player.life += 2
                    print("You use a potion, you have now " + str(self.player.life) + " hp\n")
                else:
                    print("You don't have any potions\n")
        if (self.wyvern.life > self.player.life):
            print("You loose !!!")
        else:
            print("You win !!!")
        self.state = STATE.END
        return
