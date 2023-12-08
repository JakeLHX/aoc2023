class Number:
    def __init__(self, num, coords):
        self.num = num
        self.coords = coords


    def isInCoords(self, coord):
        if coord in self.coords:
            return 1