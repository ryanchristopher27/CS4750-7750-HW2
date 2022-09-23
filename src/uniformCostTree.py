# Contains Uniform Cost Tree Search Algorithm
from vacuum import Vacuum
from node import Node
import math

#iterates through the room and finds all the dirty rooms and put them in the dirty room. 
#array 2x the size of the amount of dirty rooms: x,y
def findDirtyRooms(v: Vacuum):
    dirtyRooms = []
    for ir, row in enumerate(v.map):
        for ic, col in enumerate(row):
            if col == 1:
                dirtyRooms.append(Node([ir,ic], 0))
    return dirtyRooms

#Orders the dirty rooms from closest to furthest from currentLocaitions
#returns an updated dirtyRooms 
def orderRooms(dirtyRooms, currentLocation):
    if(dirtyRooms != []):
        #buble sort extreamly
        for value in dirtyRooms:
            value.setScore(0)
            value.addToScore(xDifference(currentLocation[0], value.getXValue()))
            value.addToScore(yDifference(currentLocation[1], value.getYValue()))
        orderedRooms = sorted(dirtyRooms, key=Node.getScore)
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
       
def uniformCostTree(fringe, v:Vacuum): 
    if(fringe == []):
        return None
    
    orderedFringe: Node = orderRooms(fringe, v.currentLoc)
 
    xValue = orderedFringe[0].getXValue()
    yValue = orderedFringe[0].getYValue()
    orderedFringe.pop(0)
    xMove(v, xValue)
    yMove(v, yValue)

    if(v.isDirty()):
        #a goal node reached
        uniformCostTree(orderedFringe, v)
        
#Test functions 
map = [[0 for i in range(5)] for j in range(4)]
vTest = Vacuum(map, [0,0], 0)
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
uniformCostTree(orderedRooms, vTest)
print("uniformCostTree Test")
print("score", vTest.currentScore, "== 5.5")
print("currentLocation", vTest.currentLoc, "== [0, 1])")
print("\n")