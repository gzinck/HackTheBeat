"""

Created on 15 Sept 2018.
This holds the results of the data, which will be pulled into the GUI.

@author: Graeme Zinck

"""

class DataResults:
    def __init__(self, graphImg, percentMatch, beatType):
        self.graphImg = graphImg
        self.percentMatch = percentMatch
        self.beatType = beatType
    def getImage(self):
        return self.graphImg
    def getPercent(self):
        return self.percentMatch
    def getBeatType(self):
        return self.beatType