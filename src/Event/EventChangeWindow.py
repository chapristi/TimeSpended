from array import array
import string
import time
import pygetwindow as gw
from src.Service.File import File
class EventSubscriberChangeWindow:
    def __init__(self) -> None:
        self.file = File("../../infos.txt")
    #i'm looking for a way to get event et delete this time.sleep 😭
    def whatWindow() -> string:
        return gw.getActiveWindow().title
    def SplitedElements (self) -> array:
        ok = self.file.readFile()
        return ok.split("_")
    def Event (self):
        while True:
            time.sleep(5)
            page = self.whatWindow()
            t = self.SplitedElements()
            if page != t[len(t)-2]:
                self.file.writeFile(self.whatWindow())
                
        

    