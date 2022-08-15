import time
import pygetwindow as gw
class EventSubscriberChangeWindow:
    #i'm looking for a way to get event et delete this time.sleep
    def whatWindow():
        while True:
            time.sleep(5)
            print(gw.getActiveWindow().title)
    