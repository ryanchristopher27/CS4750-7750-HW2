# Contains Uniform Cost Graph Search Algorithm

# Imports
from math import dist
from vacuum import Vacuum
import numpy as np

# fringe = priority queue
    # format: Dict = {'distance from goal': [x-value, y-value]}
def uniformCostGraphSearch(vac, fringe):
    visited = {}
    
    count = 0

    # Populate fringe

    #while(fringe):
    


# Input: current location and goal location
# Output: distance between 2 locations
def distanceFromGoal(currentLoc, goalLoc):
    xDist = abs(goalLoc[0] - currentLoc[0])
    yDist = abs(goalLoc[1] - currentLoc[1])

    return xDist + yDist


# Expand Function
def Expand(vac):
    successors = np.array([])
    x = vac.currentLoc[0]
    y = vac.currentLoc[1]

    # Check for edge cases
    # Add set of tuples which each contain x and y coordinates for expanded node
    if x == 0:
        if y == 0:
            # Right or Down
            successors = np.append(successors, [x+1, y])
            successors = np.append(successors, [x, y+1])
        elif y == 3:
            # Right or Up
            successors.add((x+1, y), (x, y-1))
        else:
            # Right, Up, or Down
            successors.add((x+1, y), (x, y+1), (x, y-1))

    elif x == 4:
        if y == 0:        
            # Left or Down
            successors.add((x-1, y), (x, y+1))
        elif y == 3:
            # Left or Up
            successors.add((x-1, y), (x, y-1))
        else:
            # Left, Up, or Down
            successors.add((x-1, y), (x, y+1), (x, y-1))

    else:
        if y == 0:
            # Left, Right, or Down
            successors.add((x+1, y), (x-1, y), (x, y+1))
        elif y == 3:
            # Left, Right, or Up
            successors.add((x+1, y), (x-1, y), (x, y-1))
        else:
            # Left, Right, Up, or Down
            successors.add((x+1, y), (x-1, y), (x, y+1), (x, y-1))
    
    return successors


# def InsertAll(successors, fringe):
    
map = [[0 for i in range(5)] for j in range(4)]
startingLoc = [0,0]
currentLoc = [0,0]  # [x-value, y-value]
currentScore = 0.0
stepCount = 0
vac = Vacuum(map, startingLoc, currentLoc, currentScore, stepCount)
successors = Expand(vac)

print(vac)
print(successors)