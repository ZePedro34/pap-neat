import random
from PreyState import PreyState
from WorldState import WorldState


class RandomPreyController:
    def execute(self, ws: WorldState, preyState: PreyState):
        action = random.randint(1, 4)
        match action:
            case 1:
                if (preyState.posX + 1 < ws.numCols):
                    preyState.posX += 1
            case 2:
                if (preyState.posX - 1 >= 0):
                    preyState.posX -= 1
            case 3:
                if (preyState.posY + 1 < ws.numRows):
                    preyState.posY += 1
            case 4:
                if (preyState.posY - 1 >= 0):
                    preyState.posY -= 1