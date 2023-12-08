from Symbol import Symbol
from Number import Number
with open('day3/input.txt', 'r') as file:
    data = file.read().split()

# # Convert each row into a list of characters
# matrix = [list(row) for row in data]

def get_surrounding_coords(coord):
    x, y = coord
    surrounding_coords = [
        [x - 1, y - 1],
        [x - 1, y],
        [x - 1, y + 1],
        [x, y - 1],
        [x, y + 1],
        [x + 1, y - 1],
        [x + 1, y],
        [x + 1, y + 1]
    ]
    return surrounding_coords


#My idea is to find all the symbols coordinates and store them in a list

symbols = []
numbers=[]
partNumbers = set()
line = 0
for eachLine in data:
    charLoc= 0
    for char in eachLine:
        if (char.isalnum() == 0 and char != '.'):
            sym = Symbol(char, [line, charLoc])
            symbols.append(sym)
        charLoc = charLoc+1
    line = line+1
        
# print(symbols)

#matrix[0][0] is 4

line = 0
#Then store all the numbers in a NumCoordList with the coordinates of each digit
for eachLine in data:
    eachLine = eachLine+'.'
    start = None
    for i, char in enumerate(eachLine):
        if char.isdigit():
            if start is None:
                start = i
        elif start is not None:
            end = i
            number = int(eachLine[start:end])
            positions = [[line, pos] for pos in range(start, end)]
            num = Number(number, positions)
            numbers.append(num)
            start = None
    line = line+1

# print(numbers)

#Then loop through the symbolList and look in each of the 8 surrounding coords for a number
for number in numbers:
    for symbol in symbols:
        symCoord = symbol.coords
        surrounds = get_surrounding_coords(symCoord)
        for each in surrounds:
            if(number.isInCoords(each)):
                partNumbers.add(number)

# print(partNumbers)

total = 0

for partNumber in partNumbers:
    total = total + partNumber.num

print(total)


#Once a number has been found and added to the partnum list, it needs to be removed from the NumCoordList because it cant be added twice. 

sumRatios = 0

for symbol in symbols:
    if symbol.isAsterix:
        gearRats = set()
        symCoord = symbol.coords
        surrounds = get_surrounding_coords(symCoord)
        for number in numbers:
            for coord in surrounds:
                if number.isInCoords(coord):
                    gearRats.add(number)
        if len(gearRats) > 1:
            gearRatsList = list(gearRats)
            ratio = gearRatsList[0].num * gearRatsList[1].num
            sumRatios = sumRatios+ratio

print(sumRatios)




    