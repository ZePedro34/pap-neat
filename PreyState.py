import math
from Transform import Transform

class PreyState:
    def __init__(self, pos=(0, 0), ori= (1, 0)):
        self.transform = Transform(pos, ori)
        self.maxTheta = math.radians(10)
        self.maxDl = 5

    def rotate(self, angRads):
        if(angRads>0):
            self.transform.rotate(min(angRads, self.maxTheta))
        else:
            self.transform.rotate(max(angRads, -self.maxTheta))

    def moveForward(self, dl):
        if(dl>0):
            self.transform.moveForward(min(dl, self.maxDl))
        else:
            self.transform.moveForward(max(dl, -self.maxDl))