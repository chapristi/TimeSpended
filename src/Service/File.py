import json 

class File:
    def __init__(self,file) -> None:
        self.file = file
    def readFile():
        with open('../infos.json') as json_data:
            return json.load(json_data)
    