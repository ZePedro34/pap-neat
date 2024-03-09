import math

from mymath.MathUtils import rotate

class Transform:
    def __init__(self, pos=(0, 0), ori=(1, 0)) -> None:
        self.pos = pos
        self.ori = ori

    def moveForward(self, dl): 
        newX = self.pos[0] + dl * self.ori[0]
        newY = self.pos[1] + dl * self.ori[1]
        self.pos = (newX, newY)

    def rotate(self, angRads):
        self.ori = rotate(self.ori, angRads)

