from array import array
import string
import time
import pygetwindow as gw
import sys
sys.path.append('src/Service')
from src.Service.File import File

class EventChangeWindow:
    def __init__(self: any) -> None:
        self.file = File("infos.txt")
        #print(self.file.readFile())
    #i'm looking for a way to get event et delete this time.sleep 😭
    def whatWindow(self) -> string:
        return gw.getActiveWindow().title
    def SplitedElements(self: any) -> array:
        ok = self.file.readFile()
        return ok.split("_")
    def Event (self: any):
        while True:
            time.sleep(5)
            page = self.whatWindow()
            t = self.SplitedElements()
            print(t)
            print(page)
            print(t[len(t)-3])
            if page != t[len(t)-3]:
                self.file.writeFile(self.whatWindow())
                
        

    