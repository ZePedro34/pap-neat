import math
from Transform import Transform

class PreyState:
    def __init__(self, pos=(0, 0), ori= (1, 0)):
        self.transform = Transform(pos, ori)
        self.maxTheta = math.radians(10)
        self.maxDl = 4
        self.maxEnergy = 100
        self.energy = self.maxEnergy
        self.isTired = False
        self.age = 0
        self.died = False
        self.foodEaten = 0
        self.viewDistance = 200
        self.viewAngle = math.radians(30)

    def rotate(self, angRads):
        self.energy -= 1
        if (self.energy < 10):
            self.isTired = True
        if(not self.isTired):
            if(angRads>0):
                self.transform.rotate(min(angRads, self.maxTheta))
            else:
                self.transform.rotate(max(angRads, -self.maxTheta))

    def moveForward(self, dl):
        self.energy -= 1
        if (self.energy < 10):
            self.isTired = True
        if(not self.isTired):
            if(dl>0):
                self.transform.moveForward(min(dl, self.maxDl))
            else:
                self.transform.moveForward(max(dl, -self.maxDl))

    def rest(self):
        self.energy += 1
        if (self.energy > 50):
            self.isTired = False

    def eat(self):
        self.energy = self.maxEnergy
        self.foodEaten += 1

    def stepAge(self):
        self.age += 1

    def score(self):
        return self.age * 5 + self.foodEaten