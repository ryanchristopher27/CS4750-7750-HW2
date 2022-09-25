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
                dirtyRooms.append(Node([ir,ic],0, 0, 0))
    return dirtyRooms

#Orders the dirty rooms from closest to furthest from currentLocaitions
#returns an updated dirtyRooms 
def orderRooms(dirtyRooms, currentLocation):
    if(dirtyRooms != []):
        #buble sort extreamly
        for value in dirtyRooms:
            value.setPathCost(0)
            value.setPathCost(value.getPathCost() + xDifference(currentLocation[0], value.getValue()[0]))
            value.setPathCost(value.getPathCost() + yDifference(currentLocation[1], value.getValue()[1]))
        orderedRooms = sorted(dirtyRooms, key=Node.getPathCost)
        return orderedRooms
    return None

def yDifference(currentXLocation, desiredXLocations):
    difference = currentXLocation - desiredXLocations
    if(difference >= 0):
        #moving left
        score = 1*difference
    else:
        #moving right
        score = 0.9*abs(int(difference))

    return score

def xDifference(currentYLocation, desiredYLocations):
    difference = currentYLocation - desiredYLocations
    if(difference >= 0):
        #moving up
        score = 0.8*int(difference)
    else:
        #movind down 
        score = 0.7*abs(int(difference))

    return score

def yMove(v : Vacuum, desiredXLocations, solution):
    difference = v.currentLoc[0] - desiredXLocations
    if(difference >= 0):
        for x in range(0, int(difference)):
            v.moveLeft()
            solution.append(["Left", 1])
    else:
        for x in range(0, abs(int(difference))):
            v.moveRight()
            solution.append(["Right", 0.9])

def xMove(v : Vacuum, desiredYLocations, solution):
    difference = v.currentLoc[1] - desiredYLocations
    if(difference >= 0):
        for x in range(0, int(difference)):
            v.moveUp()
            solution.append(["Up", 0.8])
    else:
        for x in range(0, abs(int(difference))):
            v.moveDown()
            solution.append(["Down", 0.7])

def Expand(v: Vacuum, currentCost, currentDepth, value):
    successors = np.array([])
    x = value[0]
    y = value[1]
    leftCost = 1.0 + currentCost
    rightCost = 0.9 + currentCost
    upCost = 0.8 + currentCost
    downCost = 0.7 + currentCost

    if x == 0:
        if y == 0:
            # Right
            # successors = np.append(successors, [x+1, y])
            successors = np.append(successors, Node([x+1,y], currentDepth+1, rightCost, v.currentNode))
            # Down
            # successors = np.append(successors, [x, y+1])
            successors = np.append(successors, Node([x,y+1], currentDepth+1, downCost, v.currentNode))
        elif y == 4:
            # Right
            # successors = np.append(successors, (x+1, y))
            successors = np.append(successors, Node([x+1,y], currentDepth+1, rightCost, v.currentNode))
            # Up
            # successors = np.append(successors, (x, y-1))
            successors = np.append(successors, Node([x,y-1], currentDepth+1, upCost, v.currentNode))
        else:
            # Right
            # successors = np.append(successors, (x+1, y))
            successors = np.append(successors, Node([x+1,y], currentDepth+1, rightCost, v.currentNode))
            # Up
            # successors = np.append(successors, (x, y+1))
            successors = np.append(successors, Node([x,y-1], currentDepth+1, upCost, v.currentNode))
            # Down
            # successors = np.append(successors, (x, y-1))
            successors = np.append(successors, Node([x,y+1], currentDepth+1, downCost, v.currentNode))
    elif x == 3:
        if y == 0:        
            # Left
            # successors = np.append(successors, (x-1, y))
            successors = np.append(successors, Node([x-1,y], currentDepth+1, leftCost, v.currentNode))
            # Down
            # successors = np.append(successors, (x, y+1))
            successors = np.append(successors, Node([x,y+1], currentDepth+1, downCost, v.currentNode))
        elif y == 4:
            # Left
            # successors = np.append(successors, (x-1, y))
            successors = np.append(successors, Node([x-1,y], currentDepth+1, leftCost, v.currentNode))
            # Up
            # successors = np.append(successors, (x, y-1))
            successors = np.append(successors, Node([x,y-1], currentDepth+1, upCost, v.currentNode))
        else:
            # Left
            # successors = np.append(successors, (x-1, y))
            successors = np.append(successors, Node([x-1,y], currentDepth+1, leftCost, v.currentNode))
            # Up
            # successors = np.append(successors, (x, y+1))
            successors = np.append(successors, Node([x,y-1], currentDepth+1, upCost, v.currentNode))
            # Down
            # successors = np.append(successors, (x, y-1))
            successors = np.append(successors, Node([x,y+1], currentDepth+1, downCost, v.currentNode))
    else:
        if y == 0:
            # Right
            # successors = np.append(successors, (x+1, y))
            successors = np.append(successors, Node([x+1,y], currentDepth+1, rightCost, v.currentNode))
            # Left
            # successors = np.append(successors, (x-1, y))
            successors = np.append(successors, Node([x-1,y], currentDepth+1, leftCost, v.currentNode))
            # Down
            # successors = np.append(successors, (x, y+1))
            successors = np.append(successors, Node([x,y+1], currentDepth+1, downCost, v.currentNode))
        elif y == 4:
            # Right
            # successors = np.append(successors, (x+1, y))
            successors = np.append(successors, Node([x+1,y], currentDepth+1, rightCost, v.currentNode))
            # Left
            # successors = np.append(successors, (x-1, y))
            successors = np.append(successors, Node([x-1,y], currentDepth+1, leftCost, v.currentNode))
            # Up
            # successors = np.append(successors, (x, y-1))
            successors = np.append(successors, Node([x,y-1], currentDepth+1, upCost, v.currentNode))
        else:
            # Right
            # successors = np.append(successors, (x+1, y))
            successors = np.append(successors, Node([x+1,y], currentDepth+1, rightCost, v.currentNode))
            # Left
            # successors = np.append(successors, (x-1, y))
            successors = np.append(successors, Node([x-1,y], currentDepth+1, leftCost, v.currentNode))
            # Down
            # successors = np.append(successors, (x, y+1))
            successors = np.append(successors, Node([x,y+1], currentDepth+1, downCost, v.currentNode))
            # Up
            # successors = np.append(successors, (x, y-1))
            successors = np.append(successors, Node([x,y-1], currentDepth+1, upCost, v.currentNode))

    v.currentNode.setChildren(successors)
    v.incrementNodesExpanded(len(successors))

    return successors
    
       
def uniformCostTree(v:Vacuum, solution): 
    fringe = sorted(Expand(v, 0, v.currentNode.depth, v.currentLoc), key=attrgetter('pathCost'))

    #order dirtyyrooms from closest to farthest based on score.
    v.dirtyRooms = orderRooms(findDirtyRooms(v), v.currentLoc)
    if(v.dirtyRooms == None):
        print("Algorithm done")
        return

    goalNode = v.dirtyRooms[0]

    while(len(fringe) != 0 or v.dirtyRooms == None):
        node = fringe[0]
        fringe.pop(0)
       
        if(node.value == goalNode.value):
            #clean room 
            print("\nFound Goal Node At: ", node.value)
            xValue = v.dirtyRooms[0].getValue()[0]
            yValue = v.dirtyRooms[0].getValue()[1]
            v.dirtyRooms.pop(0)

            xMove(v, xValue, solution)
            yMove(v, yValue, solution)
            v.suck()
            solution.append(["Suck", 0.6])
            v.map[xValue][yValue] = 0

            uniformCostTree(v, solution)

            return
        fringe = sorted(np.append(fringe, Expand(v, node.pathCost, node.depth, node.value)), key=attrgetter('pathCost'))
        v.incrementNodesGenerated(1)



#Test functions 
# solution = []
# map = [[0 for i in range(5)] for j in range(4)]
# testNode = Node([0, 0], 0, 0, None)
# vTest = Vacuum(map, [0,0], [0,0], 0, 0, testNode)
# print("----- Test Functions -----")
# print("\n")

# # yMove(vTest, 3)
# # print("yMove Test")
# # print("current location:", vTest.currentLoc[1], "== 3")
# # print("current score:", vTest.currentScore, "== 2.1")
# # print("\n")

# # xMove(vTest, 2)
# # print("xMove Test")
# # print("current location:", vTest.currentLoc[0], "== 2")
# # print("current score:", vTest.currentScore, "== 3.9")
# # print("\n")

# score = xDifference(3, 0)
# print("xDifference Test")
# print("score:", score, "== 3")
# print("\n")

# score = yDifference(3, 1)
# print("yDifference Test")
# print("score:", score, "== 1.6")
# print("\n")

# vTest.setCurrentLoc([2,3])
# vTest.map[0][1] = 1
# vTest.map[3][2] = 1
# vTest.map[3][3] = 1

# dirtyRoomsTest : Node = findDirtyRooms(vTest)
# print("findDirtyRooms Test") 
# print("dirtyRooms [0, 1] [3, 2] [3, 3] == ")
# for p in dirtyRoomsTest :
#     print(p.getValue())
# print("\n")

# orderedRooms = orderRooms(dirtyRoomsTest, vTest.currentLoc)
# print("orderedRooms Test")
# print("orderedRooms [3,3] [3, 2] [0, 1] ==")
# for p in orderedRooms:
#     print(p.getValue())
# print("\n")

# vTest.currentScore = 0
# st = time.process_time()
# uniformCostTree(vTest, solution)
# et = time.process_time()

# print("uniformCostTree Test")
# print("score", vTest.currentScore, "== 7.3")
# print("currentLocation", vTest.currentLoc, "== [0, 1])")

# print("\n\n")
# print("CPU Time", et - st)
# print("score", vTest.currentScore)
# print("currentLocation", vTest.currentLoc)
# print("nodes generated", vTest.nodesGenerated)
# print("nodes expanded", vTest.nodesExpanded)
# print("total nodes", len(solution))
# print(solution)
# print("\n")

solution1 = []
mapInstance1 = [[0 for i in range(5)] for j in range(4)]
node1 = Node([0, 0], 0, 0, None)
v1 = Vacuum(mapInstance1, [0,0], [0,0], 0, 0, node1)

v1.setCurrentLoc([1,1])
v1.map[0][1] = 1
v1.map[1][3] = 1
v1.map[2][4] = 1

v1.currentScore = 0
st = time.process_time()
uniformCostTree(v1, solution1)
et = time.process_time()

#Instance #1: Initial agent location: (2,2). Dirty squares: (1,2), (2,4), (3,5). 
print("\n\n")
print("Instance #1: Initial agent location: (1,1). Dirty squares: (0,1), (1,3), (2,4).")
print("CPU Time", et - st)
print("score", v1.currentScore)
print("nodes generated", v1.nodesGenerated)
print("nodes expanded", v1.nodesExpanded)
print("total nodes", len(solution1))
print(solution1)
print("\n")


solution2 = []
mapInstance2 = [[0 for i in range(5)] for j in range(4)]
node2 = Node([0, 0], 0, 0, None)
v2 = Vacuum(mapInstance2, [0,0], [0,0], 0, 0, node2)

v2.setCurrentLoc([2,1])
v2.map[0][1] = 1
v2.map[1][0] = 1
v2.map[1][3] = 1
v2.map[2][2] = 1

v2.currentScore = 0
st = time.process_time()
uniformCostTree(v2, solution2)
et = time.process_time()

#Instance #2: Initial agent location: (3,2). Dirty squares: (1,2), (2,1), (2,4), (3,3). 
print("\n\n")
print("Instance #2: Initial agent location: (3,2). Dirty squares: (1,2), (2,1), (2,4), (3,3).")
print("CPU Time", et - st)
print("score", v2.currentScore)
print("nodes generated", v2.nodesGenerated)
print("nodes expanded", v2.nodesExpanded)
print("total nodes", len(solution2))
print(solution2)
print("\n")



