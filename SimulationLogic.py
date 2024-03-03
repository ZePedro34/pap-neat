import random
from FoodState import FoodState
from MathUtils import distance
from WorldState import WorldState


class SimulationLogic:
    def run(self, ws: WorldState):
        for p in ws.preys:
            for f in ws.food:
                if (distance(p.transform.pos, f.pos) < 20):
                    p.eat()
                    ws.food.remove(f)
                    ws.food.append(FoodState(ws.getRandomPos()))