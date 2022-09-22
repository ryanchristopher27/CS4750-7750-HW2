# This file contains the functions used 

# Imports
import numpy as np

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
            successors = np.append(successors, (x+1, y))
            successors = np.append(successors, (x, y-1))
        else:
            # Right, Up, or Down
            successors = np.append(successors, (x+1, y))
            successors = np.append(successors, (x, y+1))
            successors = np.append(successors, (x, y-1))
    elif x == 4:
        if y == 0:        
            # Left or Down
            successors = np.append(successors, (x-1, y))
            successors = np.append(successors, (x, y+1))
        elif y == 3:
            # Left or Up
            successors = np.append(successors, (x-1, y))
            successors = np.append(successors, (x, y-1))
        else:
            # Left, Up, or Down
            successors = np.append(successors, (x-1, y))
            successors = np.append(successors, (x, y+1))
            successors = np.append(successors, (x, y-1))
    else:
        if y == 0:
            # Left, Right, or Down
            successors = np.append(successors, (x+1, y))
            successors = np.append(successors, (x-1, y))
            successors = np.append(successors, (x, y+1))
        elif y == 3:
            # Left, Right, or Up
            successors = np.append(successors, (x+1, y))
            successors = np.append(successors, (x-1, y))
            successors = np.append(successors, (x, y-1))
        else:
            # Left, Right, Up, or Down
            successors = np.append(successors, (x+1, y))
            successors = np.append(successors, (x-1, y))
            successors = np.append(successors, (x, y+1))
            successors = np.append(successors, (x, y-1))
    
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