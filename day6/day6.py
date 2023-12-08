from functools import reduce

with open('day6/input2.txt', 'r') as file:
    lines = file.readlines()

    # Extracting time and distance values
    time_values = list(map(int, lines[0].split()[1:]))
    distance_values = list(map(int, lines[1].split()[1:]))

iter = 0

waysToWin = {}

while iter < len(time_values):
    currentRec = distance_values[iter]
    timeForRace = time_values[iter]
    waysToWin[timeForRace] = 0
    for secondsHeld in range(0, timeForRace+1):
        if secondsHeld == timeForRace:
            1+1

        remainingSecs = timeForRace-secondsHeld
        
        if (secondsHeld*remainingSecs) > currentRec:
            waysToWin[timeForRace] += 1

    iter +=1

print(waysToWin)
print(reduce((lambda x, y: x * y), waysToWin.values()))