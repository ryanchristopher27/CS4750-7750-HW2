class Node(object):

    def __init__(self, value, score):
        self.value = value
        self.score = score

    def getXValue(self):
        return self.value[0]

    def getYValue(self):
        return self.value[1]

    def getValue(self):
        return self.value
    
    def setValue(self, value):
        self.value = value

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def addToScore(self, score):
        self.score += score
    



