from MathUtils import getAngRads, pointRelative
from PredatorState import PredatorState
from WorldState import WorldState

class PredatorController:
    def execute(self, ws: WorldState, predatorState: PredatorState) -> None:
        if(len(ws.preys) > 0):
            nearestPrey = ws.getNearestPrey(predatorState.transform.pos)
            nearestPreyRelative = pointRelative(predatorState.transform.pos, predatorState.transform.ori, nearestPrey.transform.pos)
            predatorState.moveForward(nearestPreyRelative[0])
            predatorState.rotate(getAngRads(nearestPreyRelative))
