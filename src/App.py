from tkinter import *
import sys
sys.path.append('src/Service')
from src.Service.File import File
class App:

    def list(self):
        file = File("infos.txt")
        test_list = file.readFile().split("_")
        final_list= lambda test_list, x: [test_list[i:i+x] for i in range(0, len(test_list), x)]
        return final_list(test_list, 2)
  
    def __init__(self,root):
        lst = self.list()
        total_rows = len(lst)
        total_columns = len(lst[0])

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=100, fg='blue',
                               font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])



