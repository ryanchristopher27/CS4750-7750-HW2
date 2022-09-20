# contains the class of vacuum
class Vacuum:
    map = [[0]*5]*4
    currentLoc = [0,0]  # [x-value, y-value]
    currentScore = 0.0
    stepCount = 0

    def __init__(self, map, currentLoc, currentScore):
        self.map = map
        self.currentLoc = currentLoc
        self.currentScore = currentScore
    
    def isDirty(vac):
        x = vac.currentLoc[0]
        y = vac.currentLoc[1]

        if vac.map[x][y] == 1:
            return True
        else:
            return False

    def moveRight(vac):
        if vac.currentLoc[0] == 4:
            return False
        else:
            vac.currentLoc[0] += 1
            vac.currentScore += 0.9
            vac.stepCount += 1
            return True

    def moveLeft(vac):
        if vac.currentLoc[0] == 0:
            return False
        else:
            vac.currentLoc[0] -= 1
            vac.currentScore += 1.0
            vac.stepCount += 1
            return True
        
    def moveUp(vac):
        if vac.currentLoc[1] == 0:
            return False
        else:
            vac.currentLoc[1] -= 1
            vac.currentScore += 0.8
            vac.stepCount += 1
            return True

    def moveDown(vac):
        if vac.currentLoc[1] == 3:
            return False
        else:
            vac.currentLoc[1] += 1
            vac.currentScore += 0.7
            vac.stepCount += 1
            return True

    def suck(vac):
        x = vac.currentLoc[0]
        y = vac.currentLoc[1]

        vac.currentScore += 0.6
        vac.stepCount += 1
        vac.map[x][y] = 0

    def getScore(vac):
        return vac.currentScore

    def getStepCount(vac):
        return vac.stepCount     