from Card import Card

def returnCardsToDuplicate(card):
    cardNumsToClone = []
    for i in range(1, len(card.getWins())+1):
        cardNumsToClone.append(card.game + i)
    return cardNumsToClone

sumX = 0

cards = []
finalCards = 0

cardDict = {

}

with open('day4/input.txt', 'r') as file:
    for line in file:
        split_data = line.split('|')
        # Extract the card number
        card_number = int(split_data[0].split(':')[0].split()[-1])

        # Extract the numbers after the "|" symbol and convert them to integers
        card = Card(card_number, list(map(int, split_data[0].split(':')[1].split())), list(map(int, split_data[1].split())))

        if card.getWins() != []:
            cardVal = 1 * 2 ** (len(card.getWins())-1)
            sumX = sumX + cardVal

        cards.append(card)
        finalCards += 1
        finalCards += card.winCount
        cardDict[card.game] = 1
        
# for card in cards:
#     cloneCards = returnCardsToDuplicate(card) #This returns a list of the card numbers to be cloned (if 1 has 4 winners it returns [2,3,4,5])
#     if cloneCards != [] :
#         for card in cloneCards:
#             cards.append(cards[card-1])
#             finalCards += cards[card-1].winCount

for card in cards:
    for i in range(len(card.getWins())):
        cardDict[card.game + (i + 1)] += (1 * cardDict[card.game])  # Multiply 1 by the number of times the card would add
            
print(sumX)
print(sum(cardDict.values()))

#5095824