# contains the class of vacuum

# Imports
from node import Node

class Vacuum:
    map = [[0 for i in range(5)] for j in range(4)]
    startingLoc = [0,0]
    currentLoc = [0,0]  # [x-value, y-value]
    currentScore = 0.0
    stepCount = 0
    # currentNode

    def __init__(self, map, startingLoc, currentLoc, currentScore, stepCount, currentNode):
        self.map = map
        self.startingLoc = startingLoc
        self.currentLoc = currentLoc
        self.currentScore = currentScore
        self.stepCount = stepCount
        self.currentNode = currentNode
    
    def isDirty(self):
        x = self.currentLoc[0]
        y = self.currentLoc[1]

        if self.map[x][y] == 1:
            return True
        else:
            return False

    def moveRight(self):
        if self.currentLoc[0] == 4:
            return False
        else:
            self.currentLoc[0] += 1
            self.currentScore += 0.9
            self.stepCount += 1
            return True

    def moveLeft(self):
        if self.currentLoc[0] == 0:
            return False
        else:
            self.currentLoc[0] -= 1
            self.currentScore += 1.0
            self.stepCount += 1
            return True
        
    def moveUp(self):
        if self.currentLoc[1] == 0:
            return False
        else:
            self.currentLoc[1] -= 1
            self.currentScore += 0.8
            self.stepCount += 1
            return True

    def moveDown(self):
        if self.currentLoc[1] == 3:
            return False
        else:
            self.currentLoc[1] += 1
            self.currentScore += 0.7
            self.stepCount += 1
            return True

    def suck(self):
        x = self.currentLoc[0]
        y = self.currentLoc[1]

        self.currentScore += 0.6
        self.stepCount += 1
        self.map[x][y] = 0

    def getScore(self):
        return self.currentScore
    
    def setScore(self, score):
        self.currentScore = score

    def getStepCount(self):
        return self.stepCount

    def setStepCount(self, count):
        self.setStepCount = count

    def getStartingLoc(self):
        return self.startingLoc

    def setStartingLoc(self, loc):
        self.startingLoc = loc     

    def getCurrentLoc(self):
        return self.currentLoc

    def setCurrentLoc(self, loc):
        self.currentLoc = loc

    def setCurrentNode(self, node):
        self.currentNode = node