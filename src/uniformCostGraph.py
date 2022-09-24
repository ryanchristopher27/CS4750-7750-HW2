# Contains Uniform Cost Graph Search Algorithm

# Imports
from asyncio.windows_events import NULL
from math import dist
from vacuum import Vacuum
import numpy as np
from functions import *
from node import Node
from operator import attrgetter

# Recursively goes through and finds best path from starting location to dirty rooms
# Pass in vacuum object
# Return nothing, all results are contained within vacuum object
def uniformCostGraphSearch(vac):
    for room in vac.dirtyRooms:
        print(room.location)
    # Make sure function does not continue to run after concurrency completes
    if len(vac.dirtyRooms) == 0:
        return None
    visited = np.array([[]])
    closestRoom = vac.findClosestRoom()
    goalLoc = NULL
    if closestRoom != NULL:
        goalLoc = closestRoom.location

    # Populate fringe with expanded nodes from current node and sort it
    fringe = vac.currentNode
    fringe = sorted(np.append(fringe, Expand(vac)), key=attrgetter('pathCost'))

    while(len(fringe) != 0):
        fringe = sorted(np.append(fringe, Expand(vac)), key=attrgetter('pathCost'))
        inVisited = False
        node = fringe[0]
        # node.setTotalPathCost()
        fringe = np.delete(fringe, 0)
        node.addSequenceMove()
        if node.value == goalLoc:
            print("\nFound Goal Node At: ", node.value)
            vac.map[node.value[0]][node.value[1]] = 0
            node.suck()

            # Implement Recursion
            # If there are still dirty rooms
            if closestRoom != NULL:
                vac.setStartingLoc(node.value)
                # vac.setCurrentLoc(node.value)
                vac.setCurrentNode(node)
                vac.deleteClosestDirtyRoom()
                vac.setSequence()
                uniformCostGraphSearch(vac)
                break
        else:
            if visited.size != 0:
                for x in visited:
                    if x.value == node.value:
                        inVisited = True
            if not inVisited:
                print("\nAdded node to visited: ", node.value)
                visited = np.append(visited, node)
                vac.setCurrentNode(node)
                # vac.setCurrentLoc(node.value)
                vac.incrementNodesGenerated(1)
                # fringe = sorted(np.append(fringe, Expand(vac)), key=attrgetter('pathCost'))
    

# TESTING

# Test performed from starting location [0, 0]
def test1():
    testNode = Node([0,0], 0, 0, NULL)
    testVac = Vacuum([[0 for i in range(5)] for j in range(4)], [0,0], 0, 0, testNode)
    testVac.map[3][3] = 1
    testVac.map[1][2] = 1
    testVac.map[0][3] = 1
    testVac.map[1][1] = 1
    testVac.map[0][0] = 1
    testVac.findDirtyRooms()
    uniformCostGraphSearch(testVac)

    finalNode = testVac.currentNode

    sequence = np.array([])

    while finalNode.parent != NULL:
        sequence = np.append(sequence, finalNode)
        finalNode = finalNode.parent

    for x in sequence:
        print(x.value, x.depth, x.pathCost, x.totalPathCost)

    print(testVac.sequence)
    print("\nNodes Expanded: ", testVac.nodesExpanded)
    print("Nodes Generated: ", testVac.nodesGenerated)

# Test performed from starting node [2, 2]
# Instance 1
def test2():
    testNode = Node([1,1], 0, 0, NULL)
    testVac = Vacuum([[0 for i in range(5)] for j in range(4)], [1,1], 0, 0, testNode)
    testVac.map[0][1] = 1
    testVac.map[1][3] = 1
    testVac.map[2][4] = 1
    print(testVac.map)
    testVac.findDirtyRooms()
    uniformCostGraphSearch(testVac)

    finalNode = testVac.currentNode

    sequence = np.array([])

    while finalNode.parent != NULL:
        sequence = np.append(sequence, finalNode)
        finalNode = finalNode.parent

    for x in sequence:
        print(x.value, x.depth, x.pathCost, x.totalPathCost)

    print(testVac.sequence)
    print("\nNodes Expanded: ", testVac.nodesExpanded)
    print("Nodes Generated: ", testVac.nodesGenerated)
    print(testVac.map)

test2()