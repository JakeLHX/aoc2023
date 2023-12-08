import re;

with open('day1/input.txt', 'r') as file:
    data = file.read().split()
    
# print(data)

english_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def convertTextToInt(line) :
    returnStr = line
    for each in english_dict :
        returnStr = returnStr.replace(each, each+str(english_dict[each]) + each)
    return returnStr

#Strip non-integers function
def stripAlpha(line) :
    return re.sub(r'[^0-9]', '', line)

#Do stuff if with lengths
def process(input):
    if (len(input) == 1) :
        return input[0]*2
    elif (len(input) == 2) :
        return input
    else :
        return input[0] + input[-1]

total = 0

for each in data:
    firstPass = convertTextToInt(each)
    secondPass = stripAlpha(firstPass)
    processedLine = process(secondPass)
    total = total + int(processedLine)

print(total)
