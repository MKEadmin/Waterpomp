import levelData

TOPIC_LEVEL     = "DZHF/COLUMN_{:d}/LEVEL"        # new
TOPIC_DIRECTION = "DZHF/COLUMN_{:d}/DIRECTION"    # new
dataTopic = {levelData.DIRECTION: TOPIC_DIRECTION,
             levelData.LEVEL_AVG: TOPIC_LEVEL
            }

def _getTopicData(bakID, key, data):
    return dataTopic[key].format(bakID), str(data)

#level1 = levelData.getData(data, levelData.TANK_R, levelData.LEVEL_AVG)
#level2 = levelData.getData(data, levelData.TANK_L, levelData.LEVEL_AVG)
def getTopicData(data : dict):
    topicData = []
    for keyId in data.keys():
        for topic in dataTopic.keys():
            value = levelData.getData(data, keyId, topic)
            if value != None:
                t, d = _getTopicData(keyId, topic, value)
                topicData.append((t,d))
    return topicData
    
if __name__ == "__main__":
    data = dict()
    levelSet = ((11, 89), (12, 88), (13, 87), (42, 58), (50,50), (8, 92), (50, 50), (10, 90))
    for l0,l1 in levelSet:
        print(20*"-", "NEW DATA", 20*"-")
        data = levelData._getDummyData(l0, l1)        
        topicData = getTopicData(data)
        for t,d in topicData:
            print("MQTT-Toptic >> ", t,'\t', d)
    