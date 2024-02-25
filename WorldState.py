import random
from FoodState import FoodState
from PreyState import PreyState


class WorldState:
    def __init__(self):
        self.timestamp = 0
        self.numCols = 30
        self.numRows = 30

        self.preys = []
        self.food = []

        for i in range(4):
            self.preys.append(PreyState(random.randint(0, self.numCols-1), random.randint(0, self.numRows-1), 1, 0))

        for i in range(15):
            self.food.append(FoodState(random.randint(0, self.numCols-1), random.randint(0, self.numRows-1)))


    def getNearestFood(self, preyState: PreyState):
        distanceFood = []
        for f in self.food:
            dist = self.manhattanDistance(preyState, f)
            distanceFood.append((dist, f))

        distanceFood.sort(key=lambda x: x[0])

        return distanceFood[0][1]

    def isActive(self):
        return len(self.food) > 0
    
    def manhattanDistance(self, ps: PreyState, fs: FoodState):
        return abs(ps.posX - fs.posX) + abs(ps.posY - fs.posY)