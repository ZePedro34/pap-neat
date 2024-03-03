import math

def distance(p1, p2):
    return math.dist(p1, p2)

def norm(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2)

def getAngRads(vector):
    return math.atan2(vector[1], vector[0])

def getAngDegrees(vector):
    return math.degrees(getAngRads(vector))

def rotate(point, angRads):
        newX = math.cos(angRads) * point[0] - math.sin(angRads) * point[1]
        newY = math.sin(angRads) * point[0] + math.cos(angRads) * point[1]
        return (newX, newY)

def pointRelative(refPos, refOri, pointPos):
    rpX = pointPos[0] - refPos[0]
    rpY = pointPos[1] - refPos[1]
    refOriRads = getAngRads(refOri)
    return rotate((rpX, rpY), -refOriRads)


