from datetime import datetime

MAX_HISTORY = 10

COLUMN_1 = "COLUMN_1"
COLUMN_2 = "COLUMN_2"
HISTORY  = "HISTORY"
LEVEL    = "LEVEL"
DIRECTION= "DIRECTION"
LASTUPDATE = "UPDATED"
LEVEL2     = (COLUMN_1, COLUMN_2)
LEVEL3     = (LEVEL, DIRECTION)

_data = {COLUMN_1: {HISTORY: [],
                    LEVEL : -1,
                    DIRECTION : 0,
                    LASTUPDATE : datetime.now()
                    },
         COLUMN_2: {HISTORY: [],
                    LEVEL : -1,
                    DIRECTION : 0,
                    LASTUPDATE : datetime.now()
                    }
         }

def _addHistrory(lst, level):
    lst.append(level)
    if len(lst) > MAX_HISTORY:
       lst.remove(lst[0]) 

def addLevelDirection(column, level : int, direction: int):
    #print(column, level, direction)
    _addHistrory(_data[column][HISTORY], level)
    _data[column][LEVEL] = level
    _data[column][DIRECTION] = direction
    _data[column][LASTUPDATE] = datetime.now()

def addLevel(column, level : int):
    _addHistrory(_data[column][HISTORY], level)
    _data[column][LEVEL] = level
    _data[column][LASTUPDATE] = datetime.now()
    
def addDirection(column, direction: int):
    _data[column][DIRECTION] = direction
    _data[column][LASTUPDATE] = datetime.now()
    
def getData():
    return _data[COLUMN_1], _data[COLUMN_2]

def getLastUpdate():
    return max(_data[COLUMN_1][LASTUPDATE], _data[COLUMN_2][LASTUPDATE])

if __name__ == "__main__":
    print(getLastUpdate())
    addLevel(COLUMN_1, 10)
    addLevel(COLUMN_1, 11)
    addLevel(COLUMN_1, 12)
    addLevel(COLUMN_1, 13)
    print(getLastUpdate())
    print(getData())
    
    
    