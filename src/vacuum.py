# contains the class of vacuum

# Imports
from functions import distanceFromGoal
from node import Node
import numpy as np
from room import Room
from operator import attrgetter

class Vacuum:
    map = [[0 for i in range(5)] for j in range(4)]
    startingLoc = [0,0]
    # currentLoc = [0,0]  # [x-value, y-value]
    currentScore = 0.0
    stepCount = 0
    nodesExpanded = 0
    nodesGenerated = 0
    dirtyRooms = np.array([])
    # currentNode

    def __init__(self, map, startingLoc, currentLoc, currentScore, stepCount, currentNode):
        self.map = map
        self.startingLoc = startingLoc
        self.currentLoc = currentNode.value
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

    def findDirtyRooms(self):
        # dirtyRooms = np.array([])
        # if len(self.dirtyRooms) != 0:
        #     for i in range(len(self.dirtyRooms)):
        #         self.dirtyRooms = np.delete(self.dirtyRooms, i)

        for ir, row in enumerate(self.map):
            for ic, col in enumerate(row):
                if col == 1:
                    # distance = distanceFromGoal(self.currentLoc, [ir, ic])
                    self.dirtyRooms = np.append(self.dirtyRooms, Room([ir,ic], 1))
        
        # return dirtyRooms

    def findClosestRoom(self):
        if len(self.dirtyRooms) != 0:
            for room in self.dirtyRooms:
                room.setDistance(distanceFromGoal(self.currentLoc, room.location))

            sortedDirtyRooms = sorted(self.dirtyRooms, key=attrgetter('distance'))

            return sortedDirtyRooms[0]
        else:
            return None

    def deleteClosestDirtyRoom(self):
        if len(self.dirtyRooms) != 0:
            self.dirtyRooms = np.delete(self.dirtyRooms, 0)
            

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

    def getNodesExpanded(self):
        return self.nodesExpanded

    def setNodesExpanded(self, nodesExpanded):
        self.nodesExpanded = nodesExpanded

    def incrementNodesExpanded(self, value):
        self.nodesExpanded += value

    def getNodesGenerated(self):
        return self.nodesGenerated

    def setNodesGenerated(self, nodesGenerated):
        self.nodesGenerated = nodesGenerated

    def incrementNodesGenerated(self, value):
        self.nodesGenerated += value
