# contains the class of node

# Imports
from asyncio.windows_events import NULL
from importlib.resources import path
import numpy as np
from tkinter.tix import CheckList


class Node(object):
    # Attributes
        # Value: contains x and y coordinates to describe current node
        # Depth: number of layers to current node
        # PathCost: contains cost to get to node
        # Children: contains list of all nodes connected to current node
        # Parent: contains the parent node of the current node
    # value = [0, 0] 
    # pathCost = 0
    children = {}
    # totalPathCost = 0
    # moveSequence = np.array([])

    def __init__(self, value, depth, pathCost, parent):
        self.value = value
        self.depth = depth
        self.pathCost = pathCost
        self.parent = parent

        # if parent != NULL:
        #     totalPathCost = parent.totalPathCost + self.pathCost
        # else:
        #     totalPathCost = 0
        self.setMoveSequence()
        self.setTotalPathCost()

    # Getters and Setters
    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setDepth(self, depth):
        self.depth = depth

    def getDepth(self):
        return self.depth

    def setPathCost(self, pathCost):
        self.pathCost = pathCost

    def getPathCost(self):
        return self.pathCost

    def setChildren(self, children):
        self.children = children

    def getChildren(self):
        return self.children

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def setTotalPathCost(self):
        if self.parent != NULL:
            self.totalPathCost = self.parent.totalPathCost + self.pathCost
        else:
            self.totalPathCost = 0

    def setMoveSequence(self):
        if self.parent != NULL:
            self.moveSequence = self.parent.moveSequence
        else:
            self.moveSequence = np.array([])


    def increaseTotalPathCost(self, addedPathCost):
        self.totalPathCost = self.totalPathCost + addedPathCost

    def addNewMove(self, moveString):
        self.moveSequence = np.append(self.moveSequence, moveString)

    def getChildrenValues(self):
        childrenValues = np.array([])
        for x in self.children:
            childrenValues = np.append(childrenValues, x.value)

        return childrenValues

    def suck(self):
        self.addNewMove("Suck")
        self.increaseTotalPathCost(0.6)

    def appendSequence(self, move):
        self.moveSequence = np.append(self.moveSequence, move)

    def addSequenceMove(self):
        cost = self.pathCost
        # Add Left Move
        if cost == 1.0:
            self.appendSequence("Left")
        elif cost == 0.9:
            self.appendSequence("Right")
        elif cost == 0.8:
            self.appendSequence("Up")
        elif cost == 0.7:
            self.appendSequence("Down")
