import time
import pygetwindow as gw

while True:
    time.sleep(5)
    print(gw.getActiveWindow().title)
    