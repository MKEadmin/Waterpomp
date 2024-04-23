#No enum supported in micropython
#so this workaround
def enum(**enums: int):
    return type('Enum', (), enums)
directionEnum = enum(UP=1, DOWN=2, SAME=3)
directionNames = {directionEnum.UP: "UP",
                  directionEnum.DOWN: "DOWN",
                  directionEnum.SAME: "SAME",
                  }

#class to determine the direction te flow goes...
class flowDirection:
    def __init__(self, marge = 0, maxSameCounter = 3):
        if maxSameCounter <= 1:
            maxSameCounter = 1
        if marge < 0:
            marge = 0
        self._marge = marge
        self._currentDirection = directionEnum.SAME
        self._maxSameCounter = maxSameCounter
        self._sameCounter = maxSameCounter
        self._queue = []
        #self._queue.clear()
        print(f">> Init >> marge = {marge}, maxSameCounter = {maxSameCounter}")
        
    def debug(self, key = "?"):
        name = self.getDirectionName()
        txt = "{:4s} ->dir={:4s} counter=[{:3d}/{:2d}] lastSame={:4s} lst={}".format(str(key), name, self._sameCounter, self._maxSameCounter, str(self._lastSameValue), self._queue)
        print(txt)
        
    def getDirection(self):
        return self._currentDirection
    
    def getDirectionName(self):
        return directionNames[self._currentDirection]
    
    def reset(self, value = None):
        self._currentDirection = directionEnum.SAME
        self._sameCounter      = self._maxSameCounter
        self._lastSameValue    = value
        
    def _withinMarge(self, value, oldValue):
        if oldValue == None:
            return False
        
        return value >= (oldValue - self._marge) and value <= (oldValue + self._marge)
    
    #keeps a queue of max _maxSameCounter length
    def _updateQueue(self, value):
        self._queue.append(value)
        if len(self._queue) > self._maxSameCounter:
            self._queue.pop(0)
            
    def _getLastValue(self):
        index = len(self._queue)
        if index == 0:
            return None
        return self._queue[index-1]
    
    def _getPrevValue(self):
        index = len(self._queue)
        if index < 2:
            return None
        return self._queue[index-2]
    
    def addValue(self, value):
        if value != None:
            self._updateQueue(value)
        self._calcDirection()
        
    #when sameCounter <= 0 measurements within marge will return same    
    #called from addValue
    _lastSameValue = None
    def _calcDirection(self):
        prev = self._getPrevValue()
        last = self._getLastValue()
        if prev == None or len(self._queue) <= 1 or self._lastSameValue == None:
            self.reset(last)
            return self._currentDirection
        
        lastDir = self._currentDirection        
        isSame  = self._withinMarge(last, self._lastSameValue)
        
        if isSame:
            if last == self._lastSameValue and lastDir == directionEnum.SAME:
                self._sameCounter = self._maxSameCounter
            else:
                self._sameCounter -= 1
            if self._sameCounter <= 0:
                self._lastSameValue = last
                self._currentDirection = directionEnum.SAME
            return self._currentDirection
        
        if last > prev or (last == prev and self._currentDirection == directionEnum.UP):
            self._currentDirection = directionEnum.UP
        else:
            self._currentDirection = directionEnum.DOWN
        
        if lastDir != self._currentDirection:
            self._sameCounter = self._maxSameCounter
            self._lastSameValue = last
        return self._currentDirection

if __name__ == "__main__":
    direction = dict()
    direction[1] = flowDirection(1, 2)
    direction[2] = flowDirection(1, 2)
    direction[3] = flowDirection(1, 3)
    
    direction[1].addValue(1)
    direction[1].debug(1)
    direction[1].addValue(2)
    direction[1].debug(1)
    direction[1].addValue(3)
    direction[1].debug(1)
    direction[1].addValue(4)
    direction[1].debug(1)
   #print(directionEnum)
   #print(directionEnum.UP) # printing enum member as string
   #print(directionEnum.UP.name)# printing name of enum member using "name" keyword    
   #print(directionEnum.UP.value) # printing value of enum member using "value" keyword    
   #print(type(directionEnum.UP))  # printing the type of enum member using type()
   #print(repr(directionEnum.UP))  # printing enum member as repr    
   #print(list(directionEnum)) # printing all enum member using "list" keyword
    
    def test(direction, key, value, expected):
        flow = direction[key]
        flow.addValue(value)
        calc = flow.getDirection()
        if calc != expected:
            print("ER > ", end = "")
        else:
            print("   > ", end = "")
        dir2 = "{0:5}".format(directionNames[expected])
        
        print(dir2," --> ", end=" ")
        flow.debug(key)
        
    
    #no change after init
    test(direction, 2, None, directionEnum.SAME)
    test(direction, 2, 10, directionEnum.SAME)
    test(direction, 2, 10, directionEnum.SAME)
    # --- Big change UP
    test(direction, 2, 20, directionEnum.UP)
    test(direction, 2, 20, directionEnum.UP)
    test(direction, 2, 20, directionEnum.SAME)
    # --- Big change DOWN
    test(direction, 2, 15, directionEnum.DOWN)
    test(direction, 2, 15, directionEnum.DOWN)
    test(direction, 2, 15, directionEnum.SAME)
    # --- MOVE UP
    test(direction, 2, 19, directionEnum.UP)
    # --- MOVE SLOWLY DOWN
    test(direction, 2, 18, directionEnum.UP)
    test(direction, 2, 17, directionEnum.DOWN)
    test(direction, 2, 16, directionEnum.DOWN)
    test(direction, 2, 16, directionEnum.SAME)
    test(direction, 2, 16, directionEnum.SAME)
    test(direction, 2, 17, directionEnum.SAME)
    test(direction, 2, 18, directionEnum.UP)
    test(direction, 2, 19, directionEnum.UP)
    test(direction, 2, 20, directionEnum.UP)
    test(direction, 2, 21, directionEnum.UP)
    test(direction, 2, 22, directionEnum.UP)
    test(direction, 2, 22, directionEnum.UP)
    test(direction, 2, 22, directionEnum.UP)
    
    
    
    #no change after init
    test(direction, 3, None, directionEnum.SAME)
    test(direction, 3, 10, directionEnum.SAME)
    test(direction, 3, 10, directionEnum.SAME)
    # --- Big change UP
    test(direction, 3, 20, directionEnum.UP)
    test(direction, 3, 20, directionEnum.UP)
    test(direction, 3, 20, directionEnum.UP)
    test(direction, 3, 20, directionEnum.SAME)
    # --- Big change DOWN
    test(direction, 3, 15, directionEnum.DOWN)
    test(direction, 3, 15, directionEnum.DOWN)
    test(direction, 3, 15, directionEnum.DOWN)
    test(direction, 3, 15, directionEnum.SAME)
    # --- MOVE UP
    test(direction, 3, 19, directionEnum.UP)
    # --- MOVE SLOWLY DOWN
    test(direction, 3, 18, directionEnum.UP)
    test(direction, 3, 17, directionEnum.DOWN)
    test(direction, 3, 16, directionEnum.DOWN)
    test(direction, 3, 16, directionEnum.DOWN)
    test(direction, 3, 16, directionEnum.SAME)
    test(direction, 3, 16, directionEnum.SAME)
    test(direction, 3, 17, directionEnum.SAME)
    test(direction, 3, 18, directionEnum.UP)
    test(direction, 3, 19, directionEnum.UP)
    test(direction, 3, 20, directionEnum.UP)
    test(direction, 3, 21, directionEnum.UP)
    test(direction, 3, 22, directionEnum.UP)
    test(direction, 3, 22, directionEnum.UP)
    test(direction, 3, 22, directionEnum.UP)