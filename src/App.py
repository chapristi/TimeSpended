from array import array
from tkinter import *
import sys
import tkinter
sys.path.append('src/Service')
from src.Event.EventChangeWindow import EventChangeWindow
"""
    this class manage what is about the application to visualise datas
"""
class App:
    """
        this function split the file in a array 2 by 2
    """
    def list(self: any) -> array:
        ev = EventChangeWindow()
        test_list = ev.SplitedElements()
        final_list = lambda test_list, x: [test_list[i:i+x] for i in range(0, len(test_list), x)]
        return final_list(test_list, 2)
    """
        manages the display of the tktiner board
    """
    def __init__(self: any, root: tkinter) -> None:
        lst = self.list()
        total_rows = len(lst)
        total_columns = len(lst[0])

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=100, fg='blue',
                               font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])



