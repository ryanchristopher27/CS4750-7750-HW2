# Contains Uniform Cost Tree Search Algorithm
from operator import attrgetter
from random import uniform
import time

import numpy as np
from vacuum import Vacuum
from node import Node

#iterates through the room and finds all the dirty rooms and put them in the dirty room. 
#array 2x the size of the amount of dirty rooms: x,y
def findDirtyRooms(v: Vacuum):
    dirtyRooms = []
    for ir, row in enumerate(v.map):
        for ic, col in enumerate(row):
            if col == 1:
                dirtyRooms.append(Node([ir,ic],0, 0, None))
    return dirtyRooms

#Orders the dirty rooms from closest to furthest from currentLocaitions
#returns an updated dirtyRooms 
def orderRooms(dirtyRooms, currentLocation):
    if(dirtyRooms != []):
        #buble sort
        for value in dirtyRooms:
            value.setPathCost(0)
            value.setPathCost(value.getPathCost() + rowDifference(currentLocation[0], value.getValue()[0]))
            value.setPathCost(value.getPathCost() + colDifference(currentLocation[1], value.getValue()[1]))
        orderedRooms = sorted(dirtyRooms, key=Node.getPathCost)
        return orderedRooms
    return None

def colDifference(currentColLocation, desiredColLocations):
    difference = currentColLocation - desiredColLocations
    if(difference >= 0):
        #moving left
        score = 1*difference
    else:
        #moving right
        score = 0.9*abs(int(difference))

    return score

def rowDifference(currentRowLocation, desiredRowLocations):
    difference = currentRowLocation - desiredRowLocations
    if(difference >= 0):
        #moving up
        score = 0.8*int(difference)
    else:
        #movind down 
        score = 0.7*abs(int(difference))

    return score

def colMove(v : Vacuum, desiredColLocations, solution):
    difference = v.currentNode.value[1] - desiredColLocations
    if(difference >= 0):
        for x in range(0, int(difference)):
            v.moveLeft()
            solution.append(["Left", 1])
    else:
        for x in range(0, abs(int(difference))):
            v.moveRight()
            solution.append(["Right", 0.9])

def rowMove(v : Vacuum, desiredRowLocations, solution):
    difference = v.currentNode.value[0] - desiredRowLocations
    if(difference >= 0):
        for x in range(0, int(difference)):
            v.moveUp()
            solution.append(["Up", 0.8])
    else:
        for x in range(0, abs(int(difference))):
            v.moveDown()
            solution.append(["Down", 0.7])

def expand(v: Vacuum, currentCost, currentDepth, value):
    successors = np.array([])
    row = value[0]
    col = value[1]
    leftCost = 1.0 + currentCost
    rightCost = 0.9 + currentCost
    upCost = 0.8 + currentCost
    downCost = 0.7 + currentCost

    if row == 0:
        if col == 0:
            # Right
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, v.currentNode))
            # Down
            successors = np.append(successors, Node([row,col+1], currentDepth+1, downCost, v.currentNode))
        elif col == 4:
            # Right
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, v.currentNode))
            # Up
            successors = np.append(successors, Node([row,col-1], currentDepth+1, upCost, v.currentNode))
        else:
            # Right
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, v.currentNode))
            # Up
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, v.currentNode))
            # Down
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, v.currentNode))
    elif row == 3:
        if col == 0:        
            # Left
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, v.currentNode))
            # Down
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, v.currentNode))
        elif col == 4:
            # Left
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, v.currentNode))
            # Up
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, v.currentNode))
        else:
            # Left
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, v.currentNode))
            # Up
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, v.currentNode))
            # Down
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, v.currentNode))
    else:
        if col == 0:
            # Right
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, v.currentNode))
            # Left
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, v.currentNode))
            # Down
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, v.currentNode))
        elif col == 4:
            # Right
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, v.currentNode))
            # Left
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, v.currentNode))
            # Up
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, v.currentNode))
        else:
            # Right
            successors = np.append(successors, Node([row+1,col], currentDepth+1, downCost, v.currentNode))
            # Left
            successors = np.append(successors, Node([row-1,col], currentDepth+1, upCost, v.currentNode))
            # Down
            successors = np.append(successors, Node([row,col+1], currentDepth+1, rightCost, v.currentNode))
            # Up
            successors = np.append(successors, Node([row,col-1], currentDepth+1, leftCost, v.currentNode))

    v.currentNode.setChildren(successors)
    v.incrementNodesGenerated(len(successors))

    return successors
    
       
def uniformCostTree(v:Vacuum, solution): 
    fringe = sorted(expand(v, 0, v.currentNode.depth, v.currentNode.value), key=attrgetter('pathCost'))
    v.incrementNodesExpanded(1)

    #order dirty rooms from closest to farthest based on score.
    v.dirtyRooms = orderRooms(findDirtyRooms(v), v.currentNode.value)
    if(v.dirtyRooms == None):
        return

    goalNode = v.dirtyRooms[0]

    while(len(fringe) != 0 or v.dirtyRooms == None):
        node = fringe[0]
        fringe.pop(0)
       
        if(node.value == goalNode.value):
            #clean room 
            rowValue = v.dirtyRooms[0].getValue()[0]
            colValue = v.dirtyRooms[0].getValue()[1]
            v.dirtyRooms.pop(0)
            rowMove(v, rowValue, solution)
            colMove(v, colValue, solution)
            v.suck()
            solution.append(["Suck", 0.6])
            v.map[rowValue][colValue] = 0
            uniformCostTree(v, solution)
            return

        fringe = sorted(np.append(fringe, expand(v, node.pathCost, node.depth, node.value)), key=attrgetter('pathCost'))
        v.incrementNodesExpanded(1)

def UniformCostTreeOutputs():

    solution1 = []
    mapInstance1 = [[0 for i in range(5)] for j in range(4)]
    node1 = Node([1, 1], 0, 0, None)
    v1 = Vacuum(mapInstance1, [0,0], 0, 0, node1)

    v1.map[0][1] = 1
    v1.map[1][3] = 1
    v1.map[2][4] = 1

    v1.currentScore = 0
    st = time.process_time()
    uniformCostTree(v1, solution1)
    et = time.process_time()

    print("\n\nUNIFORM COST TREE SEARCH")

    #Instance #1: Initial agent location: (2,2). Dirty squares: (1,2), (2,4), (3,5). 
    print("Instance #1: Initial agent location: (1,1). Dirty squares: (0,1), (1,3), (2,4).")
    print("Total Cost:", "{:.1f}".format(v1.currentScore))
    print("Run Time:", "{:.3f}".format(et - st), "seconds")
    print("Nodes Generated", v1.nodesGenerated)
    print("Nodes Expanded", v1.nodesExpanded)
    print("Total Nodes", len(solution1))
    print(solution1)
    print("\n")


    solution2 = []
    mapInstance2 = [[0 for i in range(5)] for j in range(4)]
    node2 = Node([2, 1], 0, 0, None)
    v2 = Vacuum(mapInstance2, [0,0], 0, 0, node2)

    v2.map[0][1] = 1
    v2.map[1][0] = 1
    v2.map[1][3] = 1
    v2.map[2][2] = 1

    v2.currentScore = 0
    st = time.process_time()
    uniformCostTree(v2, solution2)
    et = time.process_time()

    #Instance #2: Initial agent location: (3,2). Dirty squares: (1,2), (2,1), (2,4), (3,3). 
    print("Instance #2: Initial agent location: (3,2). Dirty squares: (1,2), (2,1), (2,4), (3,3).")
    print("Total Cost:", "{:.1f}".format(v2.currentScore))
    print("Run Time:", "{:.3f}".format(et - st), "seconds")
    print("Nodes generated", v2.nodesGenerated)
    print("Nodes expanded", v2.nodesExpanded)
    print("Total nodes", len(solution2))
    print(solution2)
    print("\n")


