from datetime import datetime
import string
class File:
    def __init__(self,file: string) -> None:
        self.file = file
    def readFile(self: any) -> string:
        with open(self.file,'r',encoding="utf-8") as file_data:
            return file_data.read()
    def writeFile(self: any,app: string) -> any:
        time = datetime.now()
        object = f"{app}_{str(time)}\n_"
        with open(self.file, "a",encoding="utf-8") as fichier:
            return fichier.write(object)



