import random

def randomPressure():
    return 1.5 + (random.random() / 5)

measureFunctions = (randomPressure, randomPressure)

#return level1, level2, direction1, direction2
def getPressure():
    level = []
    for func in measureFunctions:
        level.append(func())
    return level
        
if __name__ == "__main__":
    for x in range(300):
        result = getPressure()
        print(result)




