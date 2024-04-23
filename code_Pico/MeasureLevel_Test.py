#list of dummy data
MAX_VALUE = 99
_dummyValues = list(range(1, MAX_VALUE + 1, 1))

_index1 = 0
def measureLevel1():
    global _index1
    _index1 += 1
    if _index1 >= len(_dummyValues):
        _index1 = 0
        _dummyValues.reverse()
    return _dummyValues[_index1]

def measureLevel2():
    return MAX_VALUE + 1 - _dummyValues[_index1]
 
 
calculateFunctions = (measureLevel1, measureLevel2)

#return level1, level2, direction1, direction2
def getWaterLevel():
    level = []
    for func in calculateFunctions:
        level.append(func())

    return level
           
if __name__ == "__main__":
    for x in range(300):
        result = getWaterLevel()
        print(result)



