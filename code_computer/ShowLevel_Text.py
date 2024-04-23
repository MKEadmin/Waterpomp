#pip install timeloop
import columnData
from timeloop import Timeloop
from datetime import timedelta
import LevelSubscriber_mock as dataSource   #create the data

tl = Timeloop()
   
@tl.job(interval=timedelta(seconds=3))
def inspectData():
    data = columnData.getData()
    print(">>>> ", data[0]['UPDATED'], data[0]["LEVEL"], data[1]["LEVEL"])
    
tl.start(block=True)
