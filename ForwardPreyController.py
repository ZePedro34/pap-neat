import random
from PreyState import PreyState
from WorldState import WorldState


class ForwardPreyController:
    def execute(self, ws: WorldState, preyState: PreyState):
        action = random.random()

        if (action < 0.8): # move forward
            newPosX = preyState.posX + preyState.oriX
            newPosY = preyState.posY + preyState.oriY
            if (newPosX >= 0 and newPosX < ws.numCols and newPosY >= 0 and newPosY < ws.numRows):
                preyState.posX = newPosX
                preyState.posY = newPosY
        elif (action >= 0.8 and action < 0.9): # rotate right
            if (preyState.oriX == 1): # head right
                preyState.oriX = 0
                preyState.oriY = 1
            elif (preyState.oriY == 1): # head up
                preyState.oriX = -1
                preyState.oriY = 0
            elif (preyState.oriX == -1): # head left
                preyState.oriX = 0
                preyState.oriY = -1
            else: # head down
                preyState.oriX = 1
                preyState.oriY = 0
        else: # rotate left
            if (preyState.oriX == 1): # head right
                preyState.oriX = 0
                preyState.oriY = -1
            elif (preyState.oriY == -1): # head down
                preyState.oriX = -1
                preyState.oriY = 0
            elif (preyState.oriX == -1): # head left
                preyState.oriX = 0
                preyState.oriY = 1
            else: # head up
                preyState.oriX = 1
                preyState.oriY = 0