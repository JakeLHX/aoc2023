class Symbol:
    def __init__(self, char, coords):
        self.char = char
        self.coords = coords

    def isAsterix(self):
        if self.char == '*':
            return 1