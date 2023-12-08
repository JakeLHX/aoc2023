cardValuesPt1 = {
    '2' : 1,
    '3' : 2,
    '4' : 3,
    '5' : 4,
    '6' : 5,
    '7' : 6,
    '8' : 7,
    '9' : 8,
    'T' : 9,
    'J' : 10,
    'Q' : 11,
    'K' : 12,
    'A' : 13
}

cardValuesPt2 = {
    'J' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    'T' : 10,
    'Q' : 11,
    'K' : 12,
    'A' : 13
}

handScores = {
    'fiveOfKind' : 7,
    'fourOfKind' : 6, 
    'fullHouse' : 5,
    'threeOfKind' : 4,
    'twoPair' : 3,
    'onePair' : 2,
    'highCard' : 1
}

def evaluateHandPt1(hand):
    handMetrics = []
    handMetrics.append('highCard')
    handMetrics.append('')

    for card in hand:
        count = hand.count(card)

        if handMetrics[0] == 'threeOfKind' and count == 2 and handMetrics[1] != card:
            handMetrics[0] = ('fullHouse')
        elif handMetrics[0] == 'onePair' and count == 3 and handMetrics[1] != card:
            handMetrics[0] = ('fullHouse')
        elif handMetrics[0] == 'onePair' and count == 2 and handMetrics[1] != card:
            handMetrics[0] = ('twoPair')
        elif count == 5:
            handMetrics[0] = ('fiveOfKind')
            handMetrics[1] = card
        elif count == 4:
            handMetrics[0] = ('fourOfKind')
            handMetrics[1] = card
        elif count == 3 and handMetrics[0] == 'highCard':
            handMetrics[0] = ('threeOfKind')
            handMetrics[1] = card
        elif count == 2 and handMetrics[0] == 'highCard':
            handMetrics[0] = ('onePair')
            handMetrics[1] = card

    score = handScores[handMetrics[0]]
    return score

def evaluateHandPt2(hand):
    handMetrics = []
    handMetrics.append('highCard')
    handMetrics.append('')

    for card in hand:
        count = hand.count(card) + hand.count('J')
        handMetrics[1] = card
        if handScores[handMetrics[0]] <= handScores['threeOfKind'] and count == 2 and handMetrics[1] != card:
            handMetrics[0] = ('fullHouse')
        elif handScores[handMetrics[0]] <= handScores['onePair'] and count == 3 and handMetrics[1] != card:
            handMetrics[0] = ('fullHouse')
        elif handScores[handMetrics[0]] <= handScores['onePair'] and count == 2 and handMetrics[1] != card:
            handMetrics[0] = ('twoPair')
        elif count >= 5:
            handMetrics[0] = ('fiveOfKind')
            handMetrics[1] = card
        elif count == 4:
            handMetrics[0] = ('fourOfKind')
            handMetrics[1] = card
        elif count == 3 and handScores[handMetrics[0]] <= handScores['threeOfKind']:
            handMetrics[0] = ('threeOfKind')
            handMetrics[1] = card
        elif count == 2 and handScores[handMetrics[0]] <= handScores['onePair']:
            handMetrics[0] = ('onePair')
            handMetrics[1] = card

    score = handScores[handMetrics[0]]
    return score

with open('day7/input.txt', 'r') as file:
    lines = file.readlines()

handsWithScores = []

for line in lines:
    game = line.split()
    gameArray = []
    for each in game[0]:
        gameArray.append(cardValuesPt1[each])
    handsWithScores.append([game[1], evaluateHandPt1(game[0]), gameArray])

handsWithScores.sort(key=lambda handsWithScores: (handsWithScores[1], handsWithScores[2][0], handsWithScores[2][1], handsWithScores[2][2], handsWithScores[2][3], handsWithScores[2][4]))

winnings = 0

for c in range(0, len(handsWithScores)):
    bid = handsWithScores[c][0]
    handWinning = int(bid) * (c+1)
    winnings += handWinning

print('Pt1',winnings)

handsWithScores = []

for line in lines:
    game = line.split()
    gameArray = []
    for each in game[0]:
        gameArray.append(cardValuesPt2[each])
    handsWithScores.append([game[1], evaluateHandPt2(game[0]), gameArray])

handsWithScores.sort(key=lambda handsWithScores: (handsWithScores[1], handsWithScores[2][0], handsWithScores[2][1], handsWithScores[2][2], handsWithScores[2][3], handsWithScores[2][4]))

winnings = 0

for c in range(0, len(handsWithScores)):
    bid = handsWithScores[c][0]
    handWinning = int(bid) * (c+1)
    winnings += handWinning
    print('Game', c, 'Bid', bid, 'Wins', handWinning, 'With', handsWithScores[c][2] )

print('Pt2',winnings)