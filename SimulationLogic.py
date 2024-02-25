import random
from FoodState import FoodState
from WorldState import WorldState


class SimulationLogic:
    def run(self, ws: WorldState):
        for p in ws.preys:
            for f in ws.food:
                if (p.posX == f.posX and p.posY == f.posY):
                    ws.food.remove(f)
                    ws.food.append(FoodState(random.randint(0, ws.numCols-1), random.randint(0, ws.numRows-1)))