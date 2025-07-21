from collections import defaultdict, namedtuple

LifeSpan = namedtuple("LifeSpan", "birthYear deathYear")

exampleLifeSpans = [
    LifeSpan(2000, 2010),
    LifeSpan(1975, 2005),
    LifeSpan(1975, 2003),
    LifeSpan(1803, 1809),
    LifeSpan(1750, 1869),
    LifeSpan(1840, 1935),
    LifeSpan(1803, 1921),
    LifeSpan(1894, 1921)
]

def highestPopulationYear(lifeSpans: list[tuple]) -> int:
    populationChangeForYear = defaultdict(lambda: 0)
    for lifeSpan in lifeSpans:
        populationChangeForYear[lifeSpan.birthYear] += 1
        populationChangeForYear[lifeSpan.deathYear+1] -= 1

    populationChangeForYear = dict(sorted(populationChangeForYear.items()))

    highestPopulationYear = 0
    currentPopulation = 0
    currentHighestPopulation = 0
    for year, populationChange in populationChangeForYear.items():
        currentPopulation += populationChange
        print(f"{year}: {populationChange:2} current population: {currentPopulation}")
        if currentPopulation > currentHighestPopulation:
            currentHighestPopulation = currentPopulation
            highestPopulationYear = year

    return highestPopulationYear

result = highestPopulationYear(exampleLifeSpans)
print(result)