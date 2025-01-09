
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Map:
    def __init__(self):
        self.playerPos = Vector2(0, 0)
        self.height = 10
        self.width = 10

    def draw(self):
        i = 0
        j = 0
        currentLine:str = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                if self.playerPos == Vector2(i, j):
                    currentLine += "P"
                else:
                    currentLine += "-"
            print(currentLine)
