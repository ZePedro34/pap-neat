import time
from PyGameRenderer import PyGameRenderer
from SimulationLogic import SimulationLogic

from WorldState import WorldState
from controller.PredatorController import PredatorController
from controller.PreyController import PreyController

if __name__ == '__main__':

    renderer = PyGameRenderer(False)
    preyCtrl = PreyController()
    predatorCtrl = PredatorController()
    simLogic = SimulationLogic()

    ws = WorldState()
    framerate = 60
    timestamp = 0
    while(timestamp < 15):

        for p in ws.preys:
           preyCtrl.execute(ws, p)
        
        for p in ws.predators:
            predatorCtrl.execute(ws, p)
            
        simLogic.run(ws)

        renderer.render(ws)

        time.sleep(1/framerate)
        timestamp += 1/framerate



    renderer.destroy()
