class RangeToMap:
    def __init__(self, rangeArray, queryVal):
        self.rangeArray = rangeArray
        self.queryVal = queryVal

    def getMap(self):
        returnDict = {
        }

        returnDict[self.rangeArray[1]] = self.rangeArray[0]

        i = self.rangeArray[2]
        iter = 0

        while i != 0 :
            returnDict[self.rangeArray[1]+iter] = self.rangeArray[0]+iter
            i -= 1
            iter += 1


        return returnDict
    
    def isQueryValInRange(self):
        if self.queryVal in range(self.rangeArray[1], self.rangeArray[1] + self.rangeArray[2]):
            return 1
    
    def returnMappedNumber(self):
        return self.queryVal + (self.rangeArray[0]-self.rangeArray[1])