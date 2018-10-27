'''
Created on Oct 26, 2018

@author: Andy
'''
import unittest
from PhotoAlbum import Photo
from PhotoAlbum import check
from PhotoAlbum import jsonFileCheck
from PhotoAlbum import readFile

class Test(unittest.TestCase):


    def testPhoto(self):
        photo = Photo(1, "a", "b", "c")
        self.assertEqual(photo, Photo(1, "a", "b", "c"), "Photo equality test")

    def testCheck(self):
        self.assertEqual(1, check("1", 10), "Check test")
        
    def testCheck1(self):
        self.assertNotEqual(2, check("1", 10), "Check unequal test")
    

    def testJsonFileCheck(self):
        self.assertEqual([{'test': 'passed'}], jsonFileCheck("test.json"), ".json file check")
    
    def testReadFile(self):
        parsedJson = {1: [[1, 'accusamus beatae ad facilis cum similique qui sunt', 'https://via.placeholder.com/600/92c952', 'https://via.placeholder.com/150/92c952']]}
        self.assertEqual(parsedJson, readFile(jsonFileCheck("test1.json")), "ReadFile check")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()