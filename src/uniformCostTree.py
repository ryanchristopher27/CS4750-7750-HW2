# Contains Uniform Cost Tree Search Algorithm
from gc import unfreeze
import numpy as np
from vacuum import Vacuum

#iterates through the room and finds all the dirty rooms and put them in the dirty room. 
#array 2x the size of the amount of dirty rooms: x,y
def findDirtyRooms(v: Vacuum):
    dirtyRooms: int = np.array([])
    for ir, row in enumerate(v.map):
        for ic, col in enumerate(row):
            if col == 1:
                dirtyRooms = np.append(dirtyRooms, [int(ir), int(ic)])
    return dirtyRooms

#Orders the dirty rooms from closest to furthest from currentLocaitions
#returns an updated dirtyRooms 
def orderRooms(dirtyRooms, currentLocation):
    isComplete = 0
    currentValue = 0
    recentValue = 0
    # currentXCordinate = 0
    # currentYCordinate = 0
    # xCordinate = 0  
    # yCordinate = 0
    # xPosition = 0   #the position in the array of the values to be deleted at the end
    # yPosition = 0
    isX = True

    if(dirtyRooms.size):
        #buble sort extreamly
        for position, value in enumerate(dirtyRooms):
            for position2, value2 in enumerate(dirtyRooms):
                isComplete +=1
                if(isX):
                    currentXCordinate = value2
                    currentValue += xDifference(currentLocation[0], value2)
                else:
                    currentYCordinate = value2
                    currentValue += yDifference(currentLocation[1], value2)

                if isComplete % 2 == 0 :
                    # print("current Value", currentValue)
                    # print("recent Value", recentValue)

                    if recentValue > currentValue:
                        # xCordinate = currentXCordinate
                        # yCordinate = currentYCordinate
                        # xPosition = position - 1
                        # yPosition = position
                        # print("dirtyRooms[position2-3] ", dirtyRooms[position2-3], "dirtyRooms[position2-1]", dirtyRooms[position2-1])
                        # print("[position2-3] ", position2-3, "[position2-1]", position2-1)

                        dirtyRooms[position2-3], dirtyRooms[position2-1] = dirtyRooms[position2-1], dirtyRooms[position2-3]
                        dirtyRooms[position2-2], dirtyRooms[position2] = dirtyRooms[position2], dirtyRooms[position2-2]
                    recentValue = currentValue
                    currentValue = 0
                    isX = True
                else:
                    isX = False
        # print(dirtyRooms)

        #Test values 
        # print(xCordinate, " ", yCordinate) 
        # print("score = ", recentValue)
        # print(xPosition, " ", yPosition)

        # xMove(currentLocation[0], xCordinate)
        # yMove(currentLocation[1], yCordinate)
        # dirtyRooms = np.delete(dirtyRooms, yPosition)
        # dirtyRooms = np.delete(dirtyRooms, xPosition)

        return dirtyRooms
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
    if(fringe.size):        
        orderedFringe = orderRooms(fringe, v.currentLoc)
        print("currentlocation", v.currentLoc)
        print(orderedFringe)
        xValue = orderedFringe[0]
        yValue = orderedFringe[1]
        # print(orderedFringe, "ordered fringe")

        orderedFringe = np.delete(orderedFringe, 1)
        orderedFringe = np.delete(orderedFringe, 0)
        xMove(v, xValue)
        yMove(v, yValue)
        # print(v.currentScore)
        if(v.isDirty()):
            #a goal node reached
            uniformCostTree(orderedFringe, v)
    else:
        return None
        
        


map = [[0 for i in range(5)] for j in range(4)]
vac = Vacuum(map, [0,0], 0)

# v.map[0][0] = 1
# vac.map[2][2] = 1
# vac.map[3][3] = 1
# vac.map[1][1] = 1
# dirtyRooms = findDirtyRooms(vac)
# uniformCostTree(dirtyRooms, vac)
# print(vac.currentScore)
# print(vac.currentLoc)
# dirtyRooms = orderRooms(dirtyRooms, [2,3])


#Test functions 
map = [[0 for i in range(5)] for j in range(4)]
vTest = Vacuum(map, [0,0], 0)
print("\n")

yMove(vTest, 3)
# print("yMove Test")
# print("current location:", vTest.currentLoc[1], "== 3")
# print("current score:", vTest.currentScore, "== 2.1")
# print("\n")

xMove(vTest, 2)
# print("xMove Test")
# print("current location:", vTest.currentLoc[0], "== 2")
# print("current score:", vTest.currentScore, "== 3.9")
# print("\n")

score = xDifference(3, 0)
# print("xDifference Test")
# print("score:", score, "== 3")
# print("\n")

score = yDifference(3, 1)
# print("yDifference Test")
# print("score:", score, "== 1.6")
# print("\n")

vTest.map[0][1] = 1
vTest.map[3][2] = 1
vTest.map[3][3] = 1


dirtyRoomsTest = findDirtyRooms(vTest)
# print("findDirtyRooms Test") 
# print("dirtyRooms [x][y][x][y]...", dirtyRoomsTest, "== [0. 1. 3. 2. 3. 3.]")
# print("\n")

orderedRooms = orderRooms(dirtyRoomsTest, vTest.currentLoc)
# print("orderedRooms Test")
# print("orderedRooms", orderedRooms, "== [3. 3. 3. 2. 0. 1.]")
# print("\n")

print("current location before" ,vTest.currentLoc)
uniformCostTree(dirtyRoomsTest, vTest)
# print("uniformCostTree Test")
# print("score", vTest.currentScore)
# print("currentLocation", vTest.currentLoc, "== [0, 1])")
# print("\n")