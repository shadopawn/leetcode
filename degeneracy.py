energyValueDict = {}

maxRange = 4
for x in range(1,maxRange+1):
    for y in range(1,maxRange+1):
        for z in range(1,maxRange+1):
            energyValue = x**2+y**2+z**2
            quantumNumTuples = []
            if energyValue in energyValueDict:
                quantumNumTuples = energyValueDict[energyValue]
            quantumNumTuples.append((x, y, z))
            energyValueDict[energyValue] = quantumNumTuples

for key, value in sorted(energyValueDict.items(), key=lambda item: item[0]):
    print(key, value)