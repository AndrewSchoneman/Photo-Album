'''

@author: Andy
'''
import unittest
from unittest import mock
from PhotoAlbum import Photo
from PhotoAlbum import check
from PhotoAlbum import jsonFileCheck
from PhotoAlbum import readFile
from PhotoAlbum import objectQuestion

class Test(unittest.TestCase):


    def testPhoto(self):
        photo = Photo(1, "a", "b", "c")
        self.assertEqual(photo, Photo(1, "a", "b", "c"), "Photo equality test")

    def testCheck(self):
        self.assertEqual(1, check("1", 10), "Check test")
        
    def testCheck1(self):
        self.assertNotEqual(2, check("1", 10), "Check unequal test")
    
    def testCheckNumTooLarge(self):
        userInput = "1"
        with mock.patch('builtins.input', side_effect=userInput):
            answer = check("1000",10)           
        self.assertEqual(1, answer)
    
    def testCheckNumZero(self):
        userInput = "1"
        with mock.patch('builtins.input', side_effect=userInput):
            answer = check("0",10)           
        self.assertEqual(1, answer)
    
    def testCheckRpeatedBadAnswers(self):
        userInput = ["pass", "na", "none", "1"]
        with mock.patch('builtins.input', side_effect=userInput):
            answer = check("0",10)           
        self.assertEqual(1, answer)

    def testJsonFileCheck(self):
        self.assertEqual([{'test': 'passed'}], jsonFileCheck("test.json"), ".json file check")

    def testInputCheck(self):        
        userInput = "1"
        with mock.patch('builtins.input', side_effect=userInput):
            answer = check("nonsense",10)           
        self.assertEqual(1, answer)
    
    def testInputCheckQuit(self):
        userInput = ["quit"]
        with mock.patch('builtins.input', side_effect=userInput):
            with self.assertRaises(SystemExit) as cm:
                check("badEntry", 10)
            self.assertEqual(cm.exception.code, 0)
    
    def testInputJsonFile(self):        
        userInput = ["test.json"]
        with mock.patch('builtins.input', side_effect=userInput):
            answer = jsonFileCheck("nonsense")           
        self.assertEqual([{"test": "passed"}], answer)
    
    def testJsonFileRepeatedBadInput(self):        
        userInput = ["na", "none", "nothing", "test.json"]
        with mock.patch('builtins.input', side_effect=userInput):
            answer = jsonFileCheck("nonsense")           
        self.assertEqual([{"test": "passed"}], answer)
    
    def testInputJsonFileQuit(self):        
        userInput = ["quit"]
        with mock.patch('builtins.input', side_effect=userInput):
            with self.assertRaises(SystemExit) as cm:
                jsonFileCheck("nonsense")           
            self.assertEqual(cm.exception.code, 0)   
        
    def testJsonFileRepeatedBadInputQuit(self):        
        userInput = ["na", "none", "nothing", "quit"]
        with mock.patch('builtins.input', side_effect=userInput):
            with self.assertRaises(SystemExit) as cm:
                jsonFileCheck("nonsense")           
            self.assertEqual(cm.exception.code, 0)
    
    def testObjectQuestionYes(self):
        userInput = ["a","b", "c", "yes"]
        with mock.patch('builtins.input', side_effect=userInput):
            answer = objectQuestion()
        self.assertEqual("yes", answer)
    
    def testObjectQuestionNo(self):
        userInput = ["a","b", "c", "no"]
        with mock.patch('builtins.input', side_effect=userInput):
            answer = objectQuestion()
        self.assertEqual("no", answer)
    
    def testObjectQuestionQuit(self):
        userInput = ["a","b", "c", "quit"]
        with mock.patch('builtins.input', side_effect=userInput):
            with self.assertRaises(SystemExit) as cm:
                objectQuestion()
        self.assertEqual(cm.exception.code, 0)        
            
    def testReadFile(self):
        parsedJson = {1: [[1, 'accusamus beatae ad facilis cum similique qui sunt', 'https://via.placeholder.com/600/92c952', 'https://via.placeholder.com/150/92c952']]}
        self.assertEqual(parsedJson, readFile(jsonFileCheck("test1.json")), "ReadFile check")
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    '''The buffer=True below supresses output to std out, if you want to see the error messages printed just remove it'''
    unittest.main()