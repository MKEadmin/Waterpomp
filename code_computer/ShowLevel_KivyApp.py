#install kivy and KivyMD
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.widget import MDWidget
from kivy.clock import Clock
from kivy.properties import *
from kivy.lang import Builder
from kivy.config import Config

from datetime import datetime
import columnData

import LevelSubscriber_mock as dataSource
#import LevelSubscriber as dataSource


ALARM_TOP    = 20
ALARM_BOTTUM = 80
WARNING_TOP  = 30
WARNING_BOTTUM = 70

Builder.load_file("ShowLevel.kv")
class PrullenbakWidget(MDBoxLayout):

    # This is the kv id of the Label I would like to update
    lbl_column_1 = StringProperty('??')
    lbl_column_2 = StringProperty('??')
    h1 = NumericProperty(100)
    h2 = NumericProperty(0)
    color1 = ColorProperty("#ffff00")
    color2 = ColorProperty("#ff00ff")
    #default text set

    # This is the action I would like to happen when the button is pressed
    def button_pressed(self):
        self.updateData()
    
    def colorForLevel(self, level):
        if level < ALARM_TOP or level > ALARM_BOTTUM:
            return "#ff0000"
        if level < WARNING_TOP or level > WARNING_BOTTUM:
            return "#ff8500"
        return "#00ff00"

    def updateColumnHeight(self, data):
        self.h1 = data[0][columnData.LEVEL]
        self.h2 = data[1][columnData.LEVEL]
        self.color1 = self.colorForLevel(self.h1)
        self.color2 = self.colorForLevel(self.h2)
        self.ids.lbl_column_1.text = f"{self.h1}"
        self.ids.lbl_column_2.text = f"{self.h2}"
        
    def updateData(self):
        #dataSource.updateData()
        data = columnData.getData()        
        self.updateColumnHeight(data)
        self.ids.lbl_lastUpdate.text = columnData.getLastUpdate().strftime("%d/%m/%Y, %H:%M:%S")
        
class MainApp(MDApp):
    def build(self):        
        Clock.schedule_interval(self.timer, 1)
        self.widget = PrullenbakWidget()
        return self.widget
    
    def timer(self, dt):
        self.widget.button_pressed()
            

if __name__ == '__main__':
    MainApp().run()
