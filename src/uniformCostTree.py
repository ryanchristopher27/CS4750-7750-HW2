# Contains Uniform Cost Tree Search Algorithm
from asyncio.windows_events import NULL
import sys
from turtle import ycor
import numpy as np
from vacuum import Vacuum

#iterates through the room and finds all the dirty rooms and put them in the dirty room. 
#array 2x the size of the amount of dirty rooms: x,y
def findDirtyRooms(map):
    dirtyRooms = np.array([])
    for ir, row in enumerate(map):
        for ic, col in enumerate(row):
            if col == 1:
                dirtyRooms = np.append(dirtyRooms, [ir, ic])
    return dirtyRooms

#Orders the dirty rooms from closest to furthest from currentLocaitions
#returns an updated dirtyRooms 
def orderClosestRoom(dirtyRooms, currentLocation):
    isComplete = 0
    currentValue = 0
    lowestValue = sys.maxsize
    currentXCordinate = 0
    currentYCordinate = 0
    xCordinate = 0  
    yCordinate = 0
    xPosition = 0   #the position in the array of the values to be deleted at the end
    yPosition = 0
    isX = True

    if(dirtyRooms.size):

        for position, value in enumerate(dirtyRooms):
            isComplete +=1
            if(isX):
                currentXCordinate = value
                currentValue += xDifference(currentLocation[0], value)
            else:
                currentYCordinate = value
                currentValue += yDifference(currentLocation[1], value)

            if isComplete % 2 == 0 :
                if currentValue < lowestValue:
                    lowestValue = currentValue
                    xCordinate = currentXCordinate
                    yCordinate = currentYCordinate
                    xPosition = position - 1
                    yPosition = position
                currentValue = 0
                isX = True
            else:
                isX = False
        
        #Test values 
        print(xCordinate, " ", yCordinate) 
        print("score = ", lowestValue)
        print(xPosition, " ", yPosition)

        xMove(currentLocation[0], xCordinate)
        yMove(currentLocation[1], yCordinate)
        dirtyRooms = np.delete(dirtyRooms, yPosition)
        dirtyRooms = np.delete(dirtyRooms, xPosition)

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
        score = 0.8*difference
    else:
        #movind down 
        score = 0.7*abs(int(difference))

    return score

def xMove(currentXLocation, desiredXLocations):
    difference = currentXLocation - desiredXLocations
    if(difference >= 0):
        for x in range(0, int(difference)):
            v.moveLeft()
    else:
        for x in range(0, abs(int(difference))):
            v.moveRight()

def yMove(currentYLocation, desiredYLocations):
    difference = currentYLocation - desiredYLocations
    if(difference >= 0):
        for x in range(0, int(difference)):
            v.moveUp()
    else:
        for x in range(0, abs(int(difference))):
            v.moveDown()
       

map = [[0 for i in range(5)] for j in range(4)]
v = Vacuum(map, [0,0], 0)

v.map[0][0] = 1
v.map[2][3] = 1
v.map[3][3] = 1
dirtyRooms = findDirtyRooms(v.map)
dirtyRooms = findClosestRoom(dirtyRooms, [0,0])
dirtyRooms = findClosestRoom(dirtyRooms, [2,3])