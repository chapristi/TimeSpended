from array import array
import string
import time
import pygetwindow as gw
import sys
sys.path.append('src/Service')
from src.Service.File import File
#i'm looking for a way to get event et delete this time.sleep 😭
"""
This class manage what is related to the user's activity
"""
class EventChangeWindow:
    def __init__(self: any) -> None:
        self.file = File()
    """
     this function returns the page the user is on
    """    
    def whatWindow(self: any) -> string:
        return gw.getActiveWindow().title
    """
     this function split elements to get array output
    """
    def SplitedElements(self: any) -> array:
        ok = self.file.readFile()
        return ok.split("_")
    """
     this function write on file the user activity if the last is not the same that now
    """
    def Event (self: any):
        while True:
            time.sleep(5)
            page = self.whatWindow()
            t = self.SplitedElements()
            if page != t[len(t)-3]:
                self.file.writeFile(self.whatWindow())
                
        

    