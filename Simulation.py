import time
from BetterHeadFoodPreyController import BetterHeadFoodPreyController
from ForwardPreyController import ForwardPreyController
from HeadFoodPreyController import HeadFoodPreyController
from PyGameRenderer import PyGameRenderer
from RandomPreyController import RandomPreyController
from SimulationLogic import SimulationLogic

from WorldState import WorldState

if __name__ == '__main__':

    renderer = PyGameRenderer(False)
    preyCtrl = BetterHeadFoodPreyController()
    simLogic = SimulationLogic()

    ws = WorldState()
    framerate = 60
    timestamp = 0
    while(timestamp < 15):

        for p in ws.preys:
           preyCtrl.execute(ws, p)
        
        simLogic.run(ws)

        renderer.render(ws)

        time.sleep(1/framerate)
        timestamp += 1/framerate



    renderer.destroy()
