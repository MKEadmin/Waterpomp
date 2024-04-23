#pip install timeloop
import columnData
from timeloop import Timeloop
from datetime import timedelta
import LevelSubscriber_mock as dataSource   #create the data

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

tl = Timeloop()

@tl.job(interval=timedelta(seconds=2))
def newData():
    data1 = measureLevel1()
    data2 = measureLevel2()
    if _dummyValues[0] > _dummyValues[1]:
        dir1 = 1
        dir2 = 2
    else:
        dir1 = 2
        dir2 = 1
    columnData.addLevelDirection(columnData.COLUMN_1, data1, dir1)
    columnData.addLevelDirection(columnData.COLUMN_2, data2, dir2)
    
tl.start(block=False)

if __name__ == "__main__":
    lastUpdate = None
    while True:
        update = columnData.getLastUpdate()
        if lastUpdate != update:
            data = columnData.getData()
            print(">>>> ", update, data[0]["LEVEL"], data[1]["LEVEL"])
            lastUpdate = update
    
    