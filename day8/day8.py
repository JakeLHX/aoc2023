import re

with open('day8/input.txt', 'r') as file:
    key = file.readline()
    file.readline()
    lines = file.readlines()

translation = key.maketrans('RL', '10', '\n')

pattern = list(key.translate(translation))

startPT1 = 'AAA'
endPT1 = 'ZZZ'

startPT2Letter = 'A'
startPT2List = []
endPT2Letter = 'Z'
endPT2 = []

mapDict = {}

for line in lines:
    matchPT1 = re.match(r'^(\w+)\s*=\s*\(([^)]+)\)\s*$', line)
    key = matchPT1.group(1)
    if key[2] == 'A':
        startPT2List.append(key)
    value = matchPT1.group(2).split(', ')
    mapDict[key]= value

#Pt1
def part1(pattern, next):
    count = 0
    for each in pattern:
        if next != 'ZZZ':
            next = mapDict[next][int(each)]
            count += 1
            pattern += each
        else:
            break
    return count

iteratedValues = {

}

#Pt2
def part2(pattern, startList, startLetter):
    count = 0
    loopList = startList
    print(startList)
    for each in pattern:
        setEndValues = set()
        for i in range (0,len(startList)):
            item = loopList[0]
            if iteratedValues.get(item) != None:
                iteratedValues[item].append(count)
            else:
                iteratedValues[item] = []
            loopList.remove(item)
            loopList.append(mapDict[item][int(each)])
            setEndValues.add(item[2])
        if list(setEndValues)[0] == 'Z' and len(setEndValues) == 1:
            break
        # print(loopList)
        count += 1
        if count%500 == 0:
            1+1
        pattern += each
    return count

# print(part1(pattern,startPT1))
print(part2(pattern,startPT2List,startPT2Letter))
    
