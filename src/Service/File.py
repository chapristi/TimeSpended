from datetime import datetime
import string
class File:
    def __init__(self,file: string) -> None:
        self.file = file
    def readFile(self):
        with open('../../infos.txt','r') as file_data:
            return file_data.read()
    def writeFile(self,app: string):
        time = datetime.now()
        object = f"{app}_{str(time)}\n_"
        with open(self.file, "a") as fichier:
            return fichier.write(object)



