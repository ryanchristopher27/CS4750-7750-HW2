# Contains the class of room

# Imports


class Room(object):
    # Attributes
        # Location: contains location of room in map [row, col]
        # State: Dirty = 1, Clean = 0
        # Distance: Distance from current node
        distance = 0

        def __init__(self, loc, state):
            self.location = loc
            self.state = state

        def setLocation(self, loc):
            self.location = loc

        def getLocation(self):
            return self.location

        def setState(self, state):
            self.state = state

        def getState(self):
            return self.state

        def setDistance(self, dist):
            self.distance = dist

        def getDistance(self):
            return self.distance