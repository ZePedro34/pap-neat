import math
import random
from MathUtils import getAngDegrees, getAngRads, pointRelative
from PreyState import PreyState
from WorldState import WorldState


class BetterHeadFoodPreyController:
    def execute(self, ws: WorldState, preyState: PreyState) -> None:
        #print("--------------------------------------")
        
        if(len(ws.food)):
            nearestFood = ws.getNearestFood(preyState)
            nearestFoodRelative = pointRelative(preyState.transform.pos, preyState.transform.ori, nearestFood.pos)
            preyState.moveForward(nearestFoodRelative[0])
            preyState.rotate(getAngRads(nearestFoodRelative))
            #print("f", nearestFoodRelative, getAngDegrees(nearestFoodRelative))
            #print("p", preyState.transform.pos, getAngDegrees(preyState.transform.ori))
