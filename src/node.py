# contains the class of node

# Imports
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

    def __init__(self, value, depth, pathCost, parent):
        self.value = value
        self.depth = depth
        self.pathCost = pathCost
        self.parent = parent

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

    def getChildrenValues(self):
        childrenValues = np.array([])
        for x in self.children:
            childrenValues = np.append(childrenValues, x.value)

        return childrenValues


    # Methods
        # Expand: return all the successors of current node
        
