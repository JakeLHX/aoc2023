import re;
from functools import reduce;
from operator import mul;

games = []

with open('day2/input.txt', 'r') as file:
    for line in file: 
        # Extract game number and groups using regular expressions
        matches = re.match(r'Game (\d+):(.+)', line)
        game_number = matches.group(1)
        groups_str = matches.group(2)

        # Split groups based on ';'
        groups = groups_str.split(';')

        # Create the final array of arrays
        result = [game_number] + [group.strip() for group in groups]

        games.append(result)

# print(games)

ruleDict = {
    "red": 12,
    "green": 13,
    "blue": 14
}

gameIDs = set()
invalidGames = set()

for game in games:
    id = int(game[0])
    gameIDs.add(id)
    rounds = game[1::]
    for round in rounds:
        draws = round.split(', ')
        for draw in draws :
            quantity, color = draw.split()
            if (int(ruleDict[color]) < int(quantity)) :
                invalidGames.add(id)

validGames = gameIDs - invalidGames

print(sum(validGames))

powers = []

for game in games:
    rounds = game[1::]

    maxDict = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    for round in rounds:
        draws = round.split(', ')
        for draw in draws :
            quantity, color = draw.split()
            if(maxDict[color] == 0 or int(maxDict[color]) < int(quantity)) :
                maxDict[color] = int(quantity)

    result = reduce(mul, maxDict.values(), 1)
    powers.append(result)

print(sum(powers))


