import random
from PreyState import PreyState
from WorldState import WorldState


class BetterHeadFoodPreyController:
    def execute(self, ws: WorldState, preyState: PreyState):
        if len(ws.food) > 0:
            f = ws.getNearestFood(preyState)
            if f.posX < preyState.posX and not self.isPreyInPosition(ws, preyState.posX - 1, preyState.posY):
                preyState.posX -= 1
            elif f.posX > preyState.posX and not self.isPreyInPosition(ws, preyState.posX + 1, preyState.posY):
                preyState.posX += 1
            elif f.posY < preyState.posY and not self.isPreyInPosition(ws, preyState.posX, preyState.posY - 1):
                preyState.posY -= 1
            elif f.posY > preyState.posY and not self.isPreyInPosition(ws, preyState.posX, preyState.posY + 1):
                preyState.posY += 1

    def isPreyInPosition(self, ws: WorldState, x: int, y: int):
        for prey in ws.preys:
            if prey.posX == x and prey.posY == y:
                return True
        return False

    def rotateRight(self, preyState: PreyState):
        if preyState.oriX == 1:  # head right
            preyState.oriX = 0
            preyState.oriY = 1
        elif preyState.oriY == 1:  # head up
            preyState.oriX = -1
            preyState.oriY = 0
        elif preyState.oriX == -1:  # head left
            preyState.oriX = 0
            preyState.oriY = -1
        else:  # head down
            preyState.oriX = 1
            preyState.oriY = 0

    def rotateLeft(self, preyState: PreyState):
        if preyState.oriX == 1:  # head right
            preyState.oriX = 0
            preyState.oriY = -1
        elif preyState.oriY == -1:  # head down
            preyState.oriX = -1
            preyState.oriY = 0
        elif preyState.oriX == -1:  # head left
            preyState.oriX = 0
            preyState.oriY = 1
        else:  # head up
            preyState.oriX = 1
            preyState.oriY = 0
