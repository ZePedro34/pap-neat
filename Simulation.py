import time
from PyGameRenderer import PyGameRenderer
from SimulationLogic import SimulationLogic

from WorldState import WorldState
from controller.PredatorController import PredatorController
from controller.PreyController import PreyController


def runSimulation():
    renderer = PyGameRenderer(False)
    preyCtrl = PreyController()
    predatorCtrl = PredatorController()
    simLogic = SimulationLogic()

    ws = WorldState()
    framerate = 30
    timestamp = 0
    while(timestamp < 15):

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

    if (len(ws.preys) > 0):
        return ws.preys[0].score()
    else:
        return ws.deadPreys[0].score()



if __name__ == '__main__':
    runSimulation()

    #for i in range(30):
     #   score = runPreySimulation(1000, PreyController())
      #  print(score)