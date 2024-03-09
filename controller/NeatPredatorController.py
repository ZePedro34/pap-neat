import math
from mymath.MathUtils import distance, getAngDegrees, getAngRads, norm, pointRelative
from state.PredatorState import PredatorState
from state.PreyState import PreyState
from state.WorldState import WorldState


class NeatPredatorController:
    def __init__(self, neural_net) -> None:
        self.neural_net = neural_net

    def execute(self, ws: WorldState, predator: PredatorState) -> None:

        preySensors = self.getPreySensors(ws, predator)

        inputs = []
        inputs.append(0)
        for i in preySensors:
            inputs.append(i)

        outputs = self.neural_net.activate(inputs)
        self.executeAction(outputs, predator)

        

    def getPreySensors(self, ws: WorldState, predator: PredatorState):
        preySensors = [0, 0, 0, 0, 0, 0, 0]
        highestStrength = 0
        for p in ws.preys:
            fRelative = pointRelative(predator.transform.pos, predator.transform.ori, p.transform.pos)
            sensorPos = self.getSensorPosition(fRelative)
            sensorStrength = self.getSensorStrength(fRelative, predator.viewDistance)
            #print(sensorPos, sensorStrength)
            if (highestStrength < sensorStrength): highestStrength = sensorStrength
            #print(highestStrength)

            if (self.isPreyReachable(sensorPos, sensorStrength)):
                if(preySensors[sensorPos-1] < sensorStrength):
                    preySensors[sensorPos-1] = sensorStrength
        
        for i in range(7):
            if (preySensors[i] < highestStrength): preySensors[i] = 0

        
        return preySensors

    def isPreyReachable(self, sensorPos, sensorStrength):
        return sensorPos > 0 and sensorStrength >= 0

    def getSensorStrength(self, point, viewDistance):
        return 1-(norm(point)/viewDistance)

    def getSensorPosition(self, posVector):
        fRelRads = getAngRads(posVector)
        if(fRelRads < math.radians(180) and fRelRads >= math.radians(125)):
            sensor = 1
        elif (fRelRads < math.radians(125) and fRelRads >= math.radians(75)):
            sensor = 2
        elif (fRelRads < math.radians(75) and fRelRads >= math.radians(25)):
            sensor = 3
        elif (fRelRads < math.radians(25) and fRelRads >= math.radians(-25)):
            sensor = 4
        elif (fRelRads < math.radians(-25) and fRelRads >= math.radians(-75)):
            sensor = 5
        elif (fRelRads < math.radians(-75) and fRelRads >= math.radians(-125)):
            sensor = 6
        elif (fRelRads < math.radians(-125) and fRelRads >= math.radians(-180)):
            sensor = 7
        else:
            sensor = -1

        return sensor
    

    def executeAction(self, outputs, predator: PredatorState):
        outs = []
        counter = 0
        for o in outputs:
            outs.append((o, counter))
            counter += 1
        outs.sort(key=lambda x: x[0])
        
        
        best = outs[0]
        #if (best[0]>0.1):
        #    print(best)

        if (best[1] == 0):
            predator.moveForward(best[0]*predator.maxDl)
        elif (best[1] == 1):
            predator.rotate(best[0]*predator.maxTheta)
        elif (best[1] == 2):
            predator.rotate(-best[0]*predator.maxTheta)
        else:
            print("warn: invalid index")
