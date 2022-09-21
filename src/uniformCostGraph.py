# Contains Uniform Cost Graph Search Algorithm

# Imports
from math import dist
from vacuum import Vacuum

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
    successors = {}

    if vac.currentLoc[0] == 0:
        if vac.currentLoc[1] == 0:
            # Right or Down

        elif vac.currentLoc[1] == 3:
            # Right or Up

        else:
            # Right, Up, or Down
        

    elif vac.currentLoc[0] == 4:
        if vac.currentLoc[1] == 0:        
            # Left or Down

        elif vac.currentLoc[1] == 3:
            # Left or Up

        else:
            # Left, Up, or Down


    else:
        if vac.currentLoc[1] == 0:
            # Left, Right, or Down

        elif vac.currentLoc[1] == 3:
            # Left, Right, or Up
            
        else:
            # Left, Right, Up, or Down
    
