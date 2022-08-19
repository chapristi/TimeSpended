from datetime import datetime
import string
"""
This class manage what is related to file (write,read) and manage his complexity 
"""
class File:
    def __init__(self) -> None:
        self.file = "infos.txt"
    def readFile(self: any) -> string:
        with open(self.file,'r',encoding="utf-8") as file_data:
            return file_data.read()
    def writeFile(self: any,app: string) -> any:
        time = datetime.now()
        object = f"{app}_{str(time)}\n_"
        with open(self.file, "a",encoding="utf-8") as fichier:
            return fichier.write(object)



