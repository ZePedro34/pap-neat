import math
from Transform import Transform

class PreyState:
    def __init__(self, pos=(0, 0), ori= (1, 0)):
        self.transform = Transform(pos, ori)
        self.maxTheta = math.radians(10)
        self.maxDl = 4
        self.energy = 100
        self.age = 0
        self.died = False
        self.foodEaten = 0

    def rotate(self, angRads):
        if(self.energy > 0):
            if(angRads>0):
                self.transform.rotate(min(angRads, self.maxTheta))
            else:
                self.transform.rotate(max(angRads, -self.maxTheta))

    def moveForward(self, dl):
        if(self.energy > 0):
            if(dl>0):
                self.transform.moveForward(min(dl, self.maxDl))
            else:
                self.transform.moveForward(max(dl, -self.maxDl))

    def eat(self):
        self.energy = 100
        self.foodEaten += 1

    def stepAge(self):
        self.age += 1

    def score(self):
        return self.age * 5 + self.foodEaten