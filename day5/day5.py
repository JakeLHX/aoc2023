from RangeToMap import RangeToMap

with open('day5/input.txt', 'r') as file:
    input_str = file.read()

    sections = input_str.split('\n\n')

    arrayDict = {}

    for section in sections:

        current_key = None
        current_array = []
        section = section.split('\n')

        for line in section:
            if line.startswith('seeds:'):
                current_key = 'seedArray'
                current_array = list(map(int, line.split(':')[1].split()))
            elif line.startswith('seed-to-soil map:'):
                current_key = 'seedToSoilArray'
                current_array = []
            elif line.startswith('soil-to-fertilizer map:'):
                current_key = 'soilToFertilizerArray'
                current_array = []
            elif line.startswith('fertilizer-to-water map:'):
                current_key = 'fertilizerToWaterArray'
                current_array = []
            elif line.startswith('water-to-light map:'):
                current_key = 'waterToLightArray'
                current_array = []
            elif line.startswith('light-to-temperature map:'):
                current_key = 'lightToTemperatureArray'
                current_array = []
            elif line.startswith('temperature-to-humidity map:'):
                current_key = 'temperatureToHumidityArray'
                current_array = []
            elif line.startswith('humidity-to-location map:'):
                current_key = 'humidityToLocationArray'
                current_array = []
            else:
                values = list(map(int, line.strip().split()))
                if values:
                    current_array.append(values)

            if current_key and current_array:
                arrayDict[current_key] = current_array

def RangeToMapFunc(arrayName, map):
    for c in arrayDict[arrayName]:
        r = RangeToMap(c)
        map.update(r.getMap())

locations = set()

# Group the numbers into pairs
split_pairs = [(arrayDict['seedArray'][i], arrayDict['seedArray'][i + 1]) for i in range(0, len(arrayDict['seedArray']), 2)]

seeds = []

for pair in split_pairs:
    seeds.append(pair[0])
    seeds.append(pair[0] + pair[1])
    # for each in range(pair[0], pair[0] + pair[1]):
    for each in range(pair[0] + pair[1] - 1000000, pair[0] + pair[1]):
        seeds.append(each)

def getLightFromSeed(arrayDict, seed):
    soil = seed

    for eachArray in arrayDict['seedToSoilArray']:
        seedRange = RangeToMap(eachArray, seed)
        if seedRange.isQueryValInRange():
            soil = seedRange.returnMappedNumber()

    fertilizer = soil

    for eachArray in arrayDict['soilToFertilizerArray']:
        seedRange = RangeToMap(eachArray, soil)
        if seedRange.isQueryValInRange():
            fertilizer = seedRange.returnMappedNumber()

    water = fertilizer

    for eachArray in arrayDict['fertilizerToWaterArray']:
        seedRange = RangeToMap(eachArray, fertilizer)
        if seedRange.isQueryValInRange():
            water = seedRange.returnMappedNumber()

    light = water

    for eachArray in arrayDict['waterToLightArray']:
        seedRange = RangeToMap(eachArray, water)
        if seedRange.isQueryValInRange():
            light = seedRange.returnMappedNumber()

    temperature = light

    for eachArray in arrayDict['lightToTemperatureArray']:
        seedRange = RangeToMap(eachArray, light)
        if seedRange.isQueryValInRange():
            temperature = seedRange.returnMappedNumber()

    humidity = temperature

    for eachArray in arrayDict['temperatureToHumidityArray']:
        seedRange = RangeToMap(eachArray, temperature)
        if seedRange.isQueryValInRange():
            humidity = seedRange.returnMappedNumber()

    location = humidity

    for eachArray in arrayDict['humidityToLocationArray']:
        seedRange = RangeToMap(eachArray, humidity)
        if seedRange.isQueryValInRange():
            location = seedRange.returnMappedNumber()
    return location

for seed in seeds:
    
    location = getLightFromSeed(arrayDict, seed)

    locations.add(location)
    # print(seed, 'is at location', location)


print(min(locations))
# print(s2s.getMap())