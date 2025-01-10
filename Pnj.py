from typing import List, Callable

import GameManager

class Line:
    def __init__(self, text: str, action: Callable = None):
        self.text: str = text
        self.action: Callable = action

    def execute(self):
        if self.action:
            self.action()


class Dialogue:
    def __init__(self, introDialogues: List[str], qAndA: dict = None, linkedDialogues: List['Dialogue'] = None):
        self.introDialogues: List[str] = introDialogues
        self.qAndA: dict = qAndA if qAndA else {}
        self.linkedDialogues: List[Dialogue] = linkedDialogues if linkedDialogues else []

    def talk(self):
        for introDialogue in self.introDialogues:
            print(introDialogue)
            if introDialogue != self.introDialogues[-1]:
                inputIntro = GameManager.Game.getInput("Continue (y): ", ["y"])
                if GameManager.Game.checkAnwser(inputIntro, "y"):
                    continue

        if self.qAndA:
            inputAnswerList = []
            for i, (choiceText, responseLine) in enumerate(self.qAndA.items()):
                inputAnswerList.append(str(i))
                print(f"{choiceText} ({i})")

            inputAnswer = GameManager.Game.getInput(
                GameManager.Game.getCommandRequestMessage() +
                "(" + "/".join(inputAnswerList) + "): ",
                inputAnswerList
            )

            selectedAnswerIndex = int(inputAnswer)
            selectedChoice = list(self.qAndA.keys())[selectedAnswerIndex]
            responseLine: Line = self.qAndA[selectedChoice]

            # Display response and execute action
            print(responseLine.text + "\n")
            responseLine.execute()

            # Launch linked dialogue if it exists
            if selectedAnswerIndex < len(self.linkedDialogues) and self.linkedDialogues[selectedAnswerIndex]:
                self.linkedDialogues[selectedAnswerIndex].talk()


class Pnj:
    def __init__(self, dialogues: List[Dialogue]):
        self.dialogues = dialogues

    def interactPlayer(self):
        for dialogue in self.dialogues:
            dialogue.talk()