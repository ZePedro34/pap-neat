from FoodState import FoodState
from PreyState import PreyState
from WorldState import WorldState


class HeadFoodPreyController:
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
