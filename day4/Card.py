class Card:

    def __init__(self, game, winningNums, cardNums):
        self.game = game
        self.winningNums = winningNums
        self.cardNums = cardNums
        self.winCount = len(self.getWins())

    def getWins(self):
        wins = []
        for each in self.cardNums:
            if each in self.winningNums:
                wins.append(each)
        return wins