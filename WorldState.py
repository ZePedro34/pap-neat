import random
from FoodState import FoodState
from MathUtils import distance
from PredatorState import PredatorState
from PreyState import PreyState


class WorldState:
    def __init__(self):
        self.min = (-400, -300)
        self.max = (400, 300)

        self.preys = []
        self.predators = []
        self.food = []

        self.preys.append(PreyState((-300,0), (1,0)))
        #self.predators.append(PredatorState((-350, 250), (1,0)))

        #for i in range(5):
        #    self.food.append(FoodState(self.getRandomPos()))

        self.food.append(FoodState((50, 0)))
        self.food.append(FoodState((150, 0)))
        self.food.append(FoodState((200, 200)))
        self.food.append(FoodState((0, 100)))
        self.food.append(FoodState((-200, 200)))
        self.food.append(FoodState((-200, 0)))
        self.food.append(FoodState((-200, -200)))
        self.food.append(FoodState((0, -150)))
        self.food.append(FoodState((200, -200)))

    def getNearestPrey(self, point):
        distances = []
        for p in self.preys:
            dist = distance(point, p.transform.pos)
            distances.append((dist, p))
        distances.sort(key=lambda x: x[0])
        return distances[0][1]
    
    def getNearestFood(self, point):
        distances = []
        for f in self.food:
            dist = distance(point, f.pos)
            distances.append((dist, f))
        distances.sort(key=lambda x: x[0])
        return distances[0][1]

    def getRandomPos(self):
        margin = 25
        return random.randint(self.min[0] + margin, self.max[0] - margin), random.randint(self.min[1] + margin, self.max[1] - margin)