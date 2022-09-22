# contains the class of node
class Node:
    # Attributes
        # Value: contains x and y coordinates to describe current node
        # Heuristic: contains distance from current node to goal node
        # Neighbors: contains list of all nodes connected to current node
        # Parent: contains the parent node of the current node
    value = (0, 0)
    heuristic = 0
    neighbors = {}

    # Methods
        # Expand: return all the successors of current node
        