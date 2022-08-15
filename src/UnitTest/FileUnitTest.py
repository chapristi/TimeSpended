import unittest

class FileUnitTest(unittest.TestCase):
    def testFileExist(self):
        fr = open('../infos.json','r')
        self.assertIsNotNone(fr.read())
        

