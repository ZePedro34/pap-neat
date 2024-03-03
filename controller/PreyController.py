from MathUtils import getAngDegrees, getAngRads, pointRelative
from PreyState import PreyState
from WorldState import WorldState


class PreyController:
    def execute(self, ws: WorldState, preyState: PreyState) -> None:
        #print("--------------------------------------")

        if(len(ws.food) > 0):
            nearestFood = ws.getNearestFood(preyState.transform.pos)
            nearestFoodRelative = pointRelative(preyState.transform.pos, preyState.transform.ori, nearestFood.pos)
            preyState.moveForward(nearestFoodRelative[0])
            preyState.rotate(getAngRads(nearestFoodRelative))
            preyState.energy -= 1
            #print("f", nearestFoodRelative, getAngDegrees(nearestFoodRelative))
            #print("p", preyState.transform.pos, getAngDegrees(preyState.transform.ori))
