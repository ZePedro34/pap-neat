import time
from render.PyGameRenderer import PyGameRenderer
from SimulationLogic import SimulationLogic

from state.WorldState import WorldState
from controller.NeatPreyController import NeatPreyController
from controller.PredatorController import PredatorController
from controller.PreyController import PreyController


def runSimulation(preyCtrl: PreyController):
    renderer = PyGameRenderer(False)
    predatorCtrl = PredatorController()
    simLogic = SimulationLogic()

    ws = WorldState()
    framerate = 120
    timestamp = 0
    while(timestamp < 600):

        for p in ws.preys:
            preyCtrl.execute(ws, p)
            p.stepAge()
        
        for p in ws.predators:
            predatorCtrl.execute(ws, p)

        simLogic.run(ws)

        renderer.render(ws)

        time.sleep(1/framerate)
        timestamp += 1/framerate

    print("==========================")
    print("Report: ")
    print("Preys: ")
    for p in ws.preys:
        print(p.score())
    print("==========================")

    renderer.destroy()



def runPreySimulation(cycles, preyCtrl: PreyController):
    simLogic = SimulationLogic()
    ws = WorldState()

    for i in range(cycles):

        for p in ws.preys:
            preyCtrl.execute(ws, p)
            p.stepAge()

        simLogic.run(ws)

    return ws.preys[0].score()



if __name__ == '__main__':
    pass
    #runSimulation()

    #for i in range(1):
    #    score = runPreySimulation(600, NeatPreyController())
    #    print(score)