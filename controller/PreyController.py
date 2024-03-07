from mymath.MathUtils import getAngDegrees, getAngRads, pointRelative
from state.PreyState import PreyState
from state.WorldState import WorldState


class PreyController:
    def execute(self, ws: WorldState, preyState: PreyState) -> None:
        #print("--------------------------------------")

        if(len(ws.food) > 0):
            nearestFood = ws.getNearestFood(preyState.transform.pos)
            nearestFoodRelative = pointRelative(preyState.transform.pos, preyState.transform.ori, nearestFood.pos)
            preyState.moveForward(nearestFoodRelative[0])
            preyState.rotate(getAngRads(nearestFoodRelative))
            #print("f", nearestFoodRelative, getAngDegrees(nearestFoodRelative))
            #print("p", preyState.transform.pos, getAngDegrees(preyState.transform.ori))
