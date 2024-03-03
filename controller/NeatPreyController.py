import math
from MathUtils import distance, getAngDegrees, getAngRads, norm, pointRelative
from PreyState import PreyState
from WorldState import WorldState


class NeatPreyController:
    def execute(self, ws: WorldState, preyState: PreyState) -> None:
        print("------------------------------")

        foodSensors = self.getFoodSensors(ws, preyState)

        inputs = []
        inputs.append(preyState.isTired)
        for i in foodSensors:
            inputs.append(i)
        print("Inputs", inputs)

        outputs = self.getOutputs(inputs)
        print("Outputs", outputs)

        self.executeAction(outputs, preyState)

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
            outputs[0] = 1
        
        return outputs

    def executeAction(self, outputs, preyState: PreyState):
        if (outputs[0] != 0):
            preyState.moveForward(preyState.maxDl)
        elif (outputs[4] != 0):
            preyState.rest()