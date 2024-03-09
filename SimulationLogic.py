import random
from state.FoodState import FoodState
from mymath.MathUtils import distance
from state.WorldState import WorldState


class SimulationLogic:
    def run(self, ws: WorldState):
        for p in ws.preys:
            for f in ws.food:
                if (distance(p.transform.pos, f.pos) < 20):
                    p.eat()
                    ws.food.remove(f)
                    ws.food.append(FoodState(ws.getRandomPos()))

        for p in ws.predators:
            for prey in ws.preys:
                if (distance(p.transform.pos, prey.transform.pos) < 20):
                    ws.preys.remove(prey)