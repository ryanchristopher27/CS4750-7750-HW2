# This file contains the functions used 

# Imports
import numpy as np
from node import Node

# Distance from current location to goal location
# Pass in current location and goal location
# Return integer distance
def distanceFromGoal(currentLoc, goalLoc):
    xDist = abs(goalLoc[0] - currentLoc[0])
    yDist = abs(goalLoc[1] - currentLoc[1])

    return xDist + yDist


# Takes in the current location and expands it in every direction possible
# Pass in vacuum object containing current location
# Return array of all successor nodes
def Expand(vac):
    successors = np.array([])
    row = vac.currentNode.value[0]
    col = vac.currentNode.value[1]
    currentDepth = vac.currentNode.depth
    leftCost = 1.0
    rightCost = 0.9
    upCost = 0.8
    downCost = 0.7

    # Check for edge cases
    # Add set of tuples which each contain x and y coordinates for expanded node
    if row == 0:
        if col == 0:
            # Right
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, vac.currentNode))
            # Down
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, vac.currentNode))
        elif col == 4:
            # Left
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, vac.currentNode))
            # Down
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, vac.currentNode))
        else:
            # Right
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, vac.currentNode))
            # Left
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, vac.currentNode))
            # Down
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, vac.currentNode))
    elif row == 3:
        if col == 0:        
             # Right
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, vac.currentNode))
            # Up
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, vac.currentNode))
        elif col == 4:
            # Left
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, vac.currentNode))
            # Up
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, vac.currentNode))
        else:
            # Left
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, vac.currentNode))
            # Up
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, vac.currentNode))
            # Right
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, vac.currentNode))
    else:
        if col == 0:
            # Right
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, vac.currentNode))
            # Up
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, vac.currentNode))
            # Down
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, vac.currentNode))
        elif col == 4:
            # Down
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, vac.currentNode))
            # Left
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, vac.currentNode))
            # Up
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, vac.currentNode))
        else:
            # Right
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, vac.currentNode))
            # Left
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, vac.currentNode))
            # Down
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, vac.currentNode))
            # Up
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, vac.currentNode))
    
    vac.currentNode.setChildren(successors)
    vac.incrementNodesExpanded(1)
    vac.incrementNodesGenerated(len(successors))

    return successors

# iterates through the room and finds all the dirty rooms and put them in the dirty room. 
# array 2x the size of the amount of dirty rooms: x,y
# Pass in map from vacuum object
# Return array of dirty rooms in map
def findDirtyRooms(map):
    dirtyRooms = np.array([])
    for ir, row in enumerate(map):
        for ic, col in enumerate(row):
            if col == 1:
                dirtyRooms = np.append(dirtyRooms, [ir, ic])
    return dirtyRooms