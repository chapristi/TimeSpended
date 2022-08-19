import unittest
TESTDATA_FILENAME = "infos.txt"
"""
    class to test the code in src/Service/File.py 
"""
class FileUnitTest(unittest.TestCase):
   """
    test to open the file
   """
   def testRead(self):
       self.testfile = open(TESTDATA_FILENAME)
       self.testdata = self.testfile.read()
   def tearDown(self):
       self.testfile.close()

        

