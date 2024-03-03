import random
from FoodState import FoodState
from MathUtils import distance
from PreyState import PreyState


class WorldState:
    def __init__(self):
        self.min = (-400, -300)
        self.max = (400, 300)

        self.preys = []
        self.food = []

        self.preys.append(PreyState((0,0), (1,0)))

        for i in range(5):
            self.food.append(FoodState(self.getRandomPos()))

        #self.food.append(FoodState((200, 0)))
        #self.food.append(FoodState((200, 200)))
        #self.food.append(FoodState((0, 200)))
        #self.food.append(FoodState((-200, 200)))
        #self.food.append(FoodState((-200, 0)))
        #self.food.append(FoodState((-200, -200)))
        #self.food.append(FoodState((0, -200)))
        #self.food.append(FoodState((200, -200)))

    def getNearestFood(self, preyState: PreyState):
        distanceFood = []
        for f in self.food:
            dist = distance(preyState.transform.pos, f.pos)
            distanceFood.append((dist, f))

        distanceFood.sort(key=lambda x: x[0])
        return distanceFood[0][1]

    def getRandomPos(self):
        margin = 25
        return random.randint(self.min[0] + margin, self.max[0] - margin), random.randint(self.min[1] + margin, self.max[1] - margin)