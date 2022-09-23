# Contains Uniform Cost Graph Search Algorithm

# Imports
from asyncio.windows_events import NULL
from math import dist
from vacuum import Vacuum
import numpy as np
from functions import *
from node import Node
from operator import attrgetter

# fringe = priority queue
    # format: Dict = {'distance from goal': [x-value, y-value]}
def uniformCostGraphSearch(vac):
    # Make sure function does not continue to run after concurrency completes
    if len(vac.dirtyRooms) == 0:
        return None
    visited = np.array([[]])
    # visited = np.append(visited, vac.currentNode)
    # vac.findDirtyRooms()
    closestRoom = vac.findClosestRoom()
    goalLoc = NULL
    if closestRoom != NULL:
        goalLoc = closestRoom.location

    # Populate fringe with expanded nodes from current node and sort it
    fringe = vac.currentNode
    fringe = sorted(np.append(fringe, Expand(vac)), key=attrgetter('pathCost'))

    while(len(fringe) != 0):
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
                vac.setCurrentLoc(node.value)
                vac.setCurrentNode(node)
                vac.deleteClosestDirtyRoom()
                vac.setSequence()
                uniformCostGraphSearch(vac)
                break
        else:
        # if node not in visited:
            if visited.size != 0:
                for x in visited:
                    if x.value == node.value:
                        inVisited = True
            if not inVisited:
                print("\nAdded node to visited: ", node.value)
                visited = np.append(visited, node)
                vac.setCurrentNode(node)
                vac.setCurrentLoc(node.value)
                vac.incrementNodesGenerated(1)
                fringe = sorted(np.append(fringe, Expand(vac)), key=attrgetter('pathCost'))
    

# TESTING
def test1():
    testNode = Node([0,0], 0, 0, NULL)
    testVac = Vacuum([[0 for i in range(5)] for j in range(4)], [0,0], [0,0], 0, 0, testNode)
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

test1()