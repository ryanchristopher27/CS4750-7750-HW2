# Contains Uniform Cost Tree Search Algorithm
# from asyncio.windows_events import NULL
from operator import attrgetter
from random import uniform

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

def xDifference(currentXLocation, desiredXLocations):
    difference = currentXLocation - desiredXLocations
    if(difference >= 0):
        #moving left
        score = 1*difference
    else:
        #moving right
        score = 0.9*abs(int(difference))

    return score

def yDifference(currentYLocation, desiredYLocations):
    difference = currentYLocation - desiredYLocations
    if(difference >= 0):
        #moving up
        score = 0.8*int(difference)
    else:
        #movind down 
        score = 0.7*abs(int(difference))

    return score

def xMove(v : Vacuum, desiredXLocations):
    difference = v.currentLoc[0] - desiredXLocations
    if(difference >= 0):
        for x in range(0, int(difference)):
            v.moveLeft()
    else:
        for x in range(0, abs(int(difference))):
            v.moveRight()

def yMove(v : Vacuum, desiredYLocations):
    difference = v.currentLoc[1] - desiredYLocations
    if(difference >= 0):
        for x in range(0, int(difference)):
            v.moveUp()
    else:
        for x in range(0, abs(int(difference))):
            v.moveDown()

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
        elif y == 3:
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
    elif x == 4:
        if y == 0:        
            # Left
            # successors = np.append(successors, (x-1, y))
            successors = np.append(successors, Node([x-1,y], currentDepth+1, leftCost, v.currentNode))
            # Down
            # successors = np.append(successors, (x, y+1))
            successors = np.append(successors, Node([x,y+1], currentDepth+1, downCost, v.currentNode))
        elif y == 3:
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
        elif y == 3:
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
    
       
def uniformCostTree(v:Vacuum): 
    fringe = sorted(Expand(v, 0, v.currentNode.depth, v.currentLoc), key=attrgetter('pathCost'))

    #order dirtyrooms from closest to farthest based on score.
    v.dirtyRooms = orderRooms(findDirtyRooms(v), v.currentLoc)
    if(v.dirtyRooms == None):
        print("Algorithm done")
        return

    goalNode = v.dirtyRooms[0]

    while(len(fringe) != 0):
        node = fringe[0]
        fringe.pop(0)
        if(node.value == goalNode.value):
            #clean room 
            print("\nFound Goal Node At: ", node.value)
            xValue = v.dirtyRooms[0].getValue()[0]
            yValue = v.dirtyRooms[0].getValue()[1]
            v.dirtyRooms.pop(0)
            xMove(v, xValue)
            yMove(v, yValue)
            v.suck()
            uniformCostTree(v)
            return
        fringe = sorted(np.append(fringe, Expand(v, node.pathCost, node.depth, node.value)), key=attrgetter('pathCost'))
        v.incrementNodesGenerated(1)



#Test functions 
map = [[0 for i in range(5)] for j in range(4)]
testNode = Node([0, 0], 0, 0, None)
vTest = Vacuum(map, [0,0], [0,0], 0, 0, testNode)
print("----- Test Functions -----")
print("\n")

yMove(vTest, 3)
print("yMove Test")
print("current location:", vTest.currentLoc[1], "== 3")
print("current score:", vTest.currentScore, "== 2.1")
print("\n")

xMove(vTest, 2)
print("xMove Test")
print("current location:", vTest.currentLoc[0], "== 2")
print("current score:", vTest.currentScore, "== 3.9")
print("\n")

score = xDifference(3, 0)
print("xDifference Test")
print("score:", score, "== 3")
print("\n")

score = yDifference(3, 1)
print("yDifference Test")
print("score:", score, "== 1.6")
print("\n")

vTest.map[0][1] = 1
vTest.map[3][2] = 1
vTest.map[3][3] = 1

dirtyRoomsTest : Node = findDirtyRooms(vTest)
print("findDirtyRooms Test") 
print("dirtyRooms [0, 1] [3, 2] [3, 3] == ")
for p in dirtyRoomsTest :
    print(p.getValue())
print("\n")

orderedRooms = orderRooms(dirtyRoomsTest, vTest.currentLoc)
print("orderedRooms Test")
print("orderedRooms [3,3] [3, 2] [0, 1] ==")
for p in orderedRooms:
    print(p.getValue())
print("\n")

vTest.currentScore = 0
uniformCostTree(vTest)
print("uniformCostTree Test")
print("score", vTest.currentScore, "== 7.3")
print("currentLocation", vTest.currentLoc, "== [0, 1])")
print("nodes generated", vTest.nodesGenerated)
print("nodes expanded", vTest.nodesExpanded)
print("\n")