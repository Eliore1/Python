import GameManager

class Pnj:
    def __init__(self, name:str, introDialogues:[], qAndA:{}):
        self.name:str = name
        self.introDialogues:[] = introDialogues
        self.dico:{} = qAndA


    def interactPlayer(self):
        for introDialogue in self.introDialogues:
            print(introDialogue)
            inputIntro = GameManager.Game.getInput("Continue (y) : ", ["y"])
            if GameManager.Game.checkAnwser(inputIntro, "y"):
                continue

        inputAnwserList = []
        for i in range(0, len(self.dico)):
            inputAnwserList.append(str(i))
            print(list(self.dico.keys())[i] + "\n")

        inputAnwser = GameManager.Game.getInput(GameManager.Game.getCommandRequestMessage() + "(" + "".join(str(i) + "/" for i in range(len(self.dico))) + ") : ", inputAnwserList)




class Dialogue:
    def __init__(self, Dialogue:str, choices:[]):
        self.Dialogue = Dialogue
        self.choices = choices
