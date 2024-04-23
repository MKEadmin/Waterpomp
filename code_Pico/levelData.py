from flowDirection import directionEnum
from flowDirection import flowDirection

TANK_R          = 1
TANK_L          = 2

LEVEL_AVG       = "L_AVERAGE"
LEVEL_ULTRASOON = "L_ULTRASOON"
LEVEL_SWITCH    = "L_SWITCH"
LEVEL_PRESSURE  = "L_PRESSURE"
DIRECTION       = "W_DIRECTION"
PRESSURE			= "PRESSURE"
levelMeasurements = (LEVEL_ULTRASOON, LEVEL_SWITCH, LEVEL_PRESSURE )

def addData(data : dict, bakId : int, key : str, value):
    if bakId not in data:
        data[bakId] = dict()
    data[bakId][key] = value

def getData(data: dict, bakId : int, key : str):
    if bakId not in data:
        return None
    if key not in data[bakId]:
        return None
    return data[bakId][key] 

def calculateAverageLevel(data: dict):
    for key in data.keys():
        counter = 0
        avg = 0
        for lm in levelMeasurements:
            value = getData(data, key, lm)
            if value != None:
                avg += value
                counter += 1
        if counter > 0:
            avg /= counter
            addData(data, key, LEVEL_AVG, avg)

#pre : calculateAverageLevel called
_directions = dict()
def calculateDirections(data: dict):
    for key in data.keys():
        if key not in _directions:
            _directions[key] = flowDirection(marge = 1, maxSameCounter = 2)
        value = data[key][LEVEL_AVG]
        flow = _directions[key]
        flow.addValue(value)
        flow.debug(str(key))
        addData(data, key, DIRECTION, flow.getDirection())

#levels is tutle of levels (42, 50, 8, 50, 8, 8, 8, 8, 9, 10, 11, 12, 13)
def _getDummyData(levelR, levelL):
    data = dict()
    addData(data, TANK_R, LEVEL_ULTRASOON, levelR)
    addData(data, TANK_L, LEVEL_ULTRASOON, levelL)
    calculateAverageLevel(data)
    calculateDirections(data)
    return data

if __name__ == "__main__":
    data = _getDummyData(13, 87)
    print(">> ", data)
    _directions[TANK_R].debug(str(TANK_R))
    _directions[TANK_L].debug(str(TANK_L))
    
    data = _getDummyData(14, 86)
    print(">> ", data)
    data = _getDummyData(15, 85)
    print(">> ", data)
    data = _getDummyData(16, 84)
    print(">> ", data)
    
#     print("----------------------") 
#     TOPIC_LEVEL     = "DZHF/COLUMN_{:d}/LEVEL"        # new
#     TOPIC_DIRECTION = "DZHF/COLUMN_{:d}/DIRECTION"    # new
#     dataTopic = {DIRECTION      : "Hoi",
#                  LEVEL_ULTRASOON: "Dag",
#                  LEVEL_AVG      : "HJH"
#                 }
#     for key in data.keys():
#         for topic in dataTopic.keys():
#             value = getData(data, key, topic)
#             print(key, topic, value)
#     
