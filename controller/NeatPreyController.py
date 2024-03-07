import math
from mymath.MathUtils import distance, getAngDegrees, getAngRads, norm, pointRelative
from state.PreyState import PreyState
from state.WorldState import WorldState


class NeatPreyController:
    def __init__(self, neural_net) -> None:
        self.neural_net = neural_net

    def execute(self, ws: WorldState, preyState: PreyState) -> None:

        foodSensors = self.getFoodSensors(ws, preyState)

        inputs = []
        inputs.append(preyState.isTired)
        for i in foodSensors:
            inputs.append(i)

        outputs = self.neural_net.activate(inputs)
        self.executeAction(outputs, preyState)

        #self.writeOutputs(outputs)

        
        #print("Inputs", inputs)
        #outputs = self.getOutputs(inputs)
        #print("Outputs", outputs)
        

    def getFoodSensors(self, ws: WorldState, preyState: PreyState):
        foodSensors = [0, 0, 0, 0, 0, 0, 0]
        for f in ws.food:
            fRelative = pointRelative(preyState.transform.pos, preyState.transform.ori, f.pos)
            sensorPos = self.getSensorPosition(fRelative)
            sensorStrength = self.getSensorStrength(fRelative, preyState.viewDistance)
            #print(sensorPos, sensorStrength)

            if (self.isFoodReachable(sensorPos, sensorStrength)):
                if(foodSensors[sensorPos-1] < sensorStrength):
                    foodSensors[sensorPos-1] = sensorStrength
        return foodSensors

    def isFoodReachable(self, sensorPos, sensorStrength):
        return sensorPos > 0 and sensorStrength >= 0

    def getSensorStrength(self, point, viewDistance):
        return 1-(norm(point)/viewDistance)

    def getSensorPosition(self, posVector):
        fRelRads = getAngRads(posVector)
        if(fRelRads < math.radians(105) and fRelRads >= math.radians(75)):
            sensor = 1
        elif (fRelRads < math.radians(75) and fRelRads >= math.radians(45)):
            sensor = 2
        elif (fRelRads < math.radians(45) and fRelRads >= math.radians(15)):
            sensor = 3
        elif (fRelRads < math.radians(15) and fRelRads >= math.radians(-15)):
            sensor = 4
        elif (fRelRads < math.radians(-15) and fRelRads >= math.radians(-45)):
            sensor = 5
        elif (fRelRads < math.radians(-45) and fRelRads >= math.radians(-75)):
            sensor = 6
        elif (fRelRads < math.radians(-75) and fRelRads >= math.radians(-105)):
            sensor = 7
        else:
            sensor = -1

        return sensor
    
    def getOutputs(self, inputs):
        outputs = [0, 0, 0, 0, 0]
        if inputs[0] == True:
            outputs[4] = 1
        else:
            outputs[0] = 5
        
        return outputs

    def executeAction(self, outputs, preyState: PreyState):
        outs = []
        counter = 0
        for o in outputs:
            outs.append((o, counter))
            counter += 1
        outs.sort(key=lambda x: x[0])
        
        
        best = outs[0]

        if (best[1] == 0):
            preyState.moveForward(best[0])
        elif (best[1] == 1):
            preyState.moveForward(-best[0])
        elif (best[1] == 2):
            preyState.rotate(best[0])
        elif (best[1] == 3):
            preyState.rotate(-best[0])
        elif (best[1] == 4):
            preyState.rest()

    def writeOutputs(self, outputs):
        f = open("outputs.txt", "a")
        for o in outputs:
            f.write(str(o) + ", ")
        f.write("/n")
        f.close()