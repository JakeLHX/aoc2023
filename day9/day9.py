with open('day9/input.txt', 'r') as file:
    lines = []
    for each in file:
        lines.append(each.split())

total = 0
pt2Total = 0

for line in lines:
    pyramid = []
    origLine = [] + line
    pyramid.append(line)
    diffList = []
    while len(set(pyramid[-1])) > 1:
        for i in reversed(range(1, len(pyramid[-1]))):
            diff = int(pyramid[-1][i]) - int(pyramid[-1][i-1])
            diffList.insert(0,diff)
        pyramid.append(diffList)
        diffList = []
    diffNumEnd = pyramid[-1][0]
    diffNumStart = pyramid[-1][0]
    while len(pyramid[0]) != len(origLine)+2:
        pyramid.pop(-1)
        pyramid[-1].append(diffNumEnd+int(pyramid[-1][-1]))
        pyramid[-1].insert(0, int(pyramid[-1][0])-diffNumStart)
        diffNumEnd = int(pyramid[-1][-1])
        diffNumStart = int(pyramid[-1][0])
    total += pyramid[0][-1]
    pt2Total += pyramid[0][0]

print(total)
print(pt2Total)