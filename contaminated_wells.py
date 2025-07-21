import random

wellList = []

for i in range(64):
    wellList.append(0)
    
for i in range(16):
    wellList.append(1)

def testWells():
    testedWells = []
    tempWellList = wellList[:]
    random.shuffle(tempWellList)
    for i in range(15):
        testedWells.append(tempWellList.pop())

    return testedWells

sampleSize = 10000
samplesWithThreeOrMoreContaminatedWells = 0

for i in range(sampleSize):
    testWellList = testWells()
    if sum(testWellList) >= 3:
        samplesWithThreeOrMoreContaminatedWells += 1

probability = samplesWithThreeOrMoreContaminatedWells/sampleSize
print(probability)