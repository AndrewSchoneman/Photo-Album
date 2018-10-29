'''
@author: Andy
'''
import unittest
import io
from unittest import mock
from PhotoAlbum import Photo
from PhotoAlbum import check
from PhotoAlbum import jsonFileCheck
from PhotoAlbum import readFile
from PhotoAlbum import objectQuestion
from PhotoAlbum import PhotoAlbumObj
from PhotoAlbum import printFile
from PhotoAlbum import createObjects
from PhotoAlbum import main


class Test(unittest.TestCase):

    # Test that the photo object quality function works correctly
    def tes_tPhoto(self):
        photo = Photo(1, "a", "b", "c")
        self.assertEqual(photo, Photo(1, "a", "b", "c"), "Photo equality test")
   
    # Test that a value error is thrown if someone tries to create a photo with a non integer
    # id value as its first argument
    def testPhoto_Equals(self):
        self.assertRaises(ValueError, Photo, "1", "a", "b", "c")
    
    # Test that we can only add photos to a photo album
    def test_AddPhoto_To_PhotoAlbumObj(self):
        album  = PhotoAlbumObj(1)
        self.assertRaises(ValueError, album.addPhoto, "not a photo")
    
    # Test that the check function returns a number as expected. In this example 1 is less than 10 and 
    # is a number so the input is valid
    def test_Check(self):
        self.assertEqual(1, check("1", 10), "Check test")
    
    # Test to make sure that if check is given an invalid size type a value error is thrown
    def test_Check_Size(self):
        self.assertRaises(ValueError, check, 1, "badInput")
       
    # Test to see if a number which is too large is not accepted by the check function. In this case
    # 1000 is greater than so it shouldn't be accepted. Then a valid input is given and we make sure 
    # that the value returned is correct.
    def test_Check_NumToo_Large(self):
        userInput = "1"
        with mock.patch('builtins.input', side_effect=userInput):
            answer = check("1000",10)           
        self.assertEqual(int(userInput), answer)
    
    # Test to see if check will reject zero since there is no photo album 0. Then ensure that it returns
    # a valid answer after getting valid user input.
    def testCheck_NumZero(self):
        userInput = "1"
        with mock.patch('builtins.input', side_effect=userInput):
            answer = check("0",10)           
        self.assertEqual(int(userInput), answer)
        
    # Test checker to see if check when given a bad input and then a good input will return the good input
    def testInput_Check(self):        
        userInput = "1"
        with mock.patch('builtins.input', side_effect=userInput):
            answer = check("nonsense",10)           
        self.assertEqual(1, answer)
    
    # Test to see if the check function will take repeated bad inputs until getting a valid input
    # and then return that input
    def testCheck_Repeated_Bad_Answers_Check(self):
        userInput = ["pass", "na", "none", "1"]
        with mock.patch('builtins.input', side_effect=userInput):
            answer = check("0",10)           
        self.assertEqual(1, answer)        
    
    # Test to see if the check function will take repeated bad inputs until getting a valid input
    # and then return that input
    def test_Input_Check_Quit(self):
        userInput = ["quit"]
        with mock.patch('builtins.input', side_effect=userInput):
            with self.assertRaises(SystemExit) as cm:
                check("badEntry", 10)
            self.assertEqual(cm.exception.code, 0)
    
    # Test to see if the check function will take repeated bad inputs until getting a quit input
    # and then exit the program
    def test_Repeated_Bad_Input_Check_Quit(self):
        userInput = ["a", "b", "c","quit"]
        with mock.patch('builtins.input', side_effect=userInput):
            with self.assertRaises(SystemExit) as cm:
                check("badEntry", 10)
            self.assertEqual(cm.exception.code, 0)    
    
        
    # Test if the .json reader will behave as expected when given a valid .json file. The info
    # comes from the test.json file which just contains {["test" : "passed"]}
    def testJsonFileCheck(self):
        self.assertEqual([{'test': 'passed'}], jsonFileCheck("test.json"), ".json file check")
    
    # Test to see if the json file reader will take a bunch of bad inputs and then read the file
    # as expected when given a valid json file. The info comes from the .json file test.json which
    # just contains a single json object with {["test" : "passed"]}
    def testJson_File_Repeated_Bad_Input(self):        
        userInput = ["na", "none", "nothing", "test.json"]
        with mock.patch('builtins.input', side_effect=userInput):
            answer = jsonFileCheck("nonsense")           
        self.assertEqual([{"test": "passed"}], answer)
    
    # Test to see if the json reader funtiton will quit as expected when given the quit command
    def test_Input_JsonFile_Quit(self):        
        userInput = ["quit"]
        with mock.patch('builtins.input', side_effect=userInput):
            with self.assertRaises(SystemExit) as cm:
                jsonFileCheck("nonsense")           
            self.assertEqual(cm.exception.code, 0)   
        
    # Test to see if the json file reader will take a bunch of bad inputs and then quit as expected when given
    # the quit command
    def test_JsonFile_Repeated_BadInput_Quit(self):        
        userInput = ["na", "none", "nothing", "quit"]
        with mock.patch('builtins.input', side_effect=userInput):
            with self.assertRaises(SystemExit) as cm:
                jsonFileCheck("nonsense")           
            self.assertEqual(cm.exception.code, 0)
    
    # A check to see if the create object question works correctly. We feed the function a series 
    # of bad inputs until we hit quit and then see if the program returned "yes" as expected.       
    def test_objectQuestion_Yes(self):
        userInput = ["foo","bar", "baz", "yes"]
        with mock.patch('builtins.input', side_effect=userInput):
            answer = objectQuestion()
        self.assertEqual("yes", answer)

    # A check to see if the create object question works correctly. We feed the function a series 
    # of bad inputs until we hit quit and then see if the program returned "no" as expected.    
    def test_bjectQuestion_No(self):
        userInput = ["a","b", "c", "no"]
        with mock.patch('builtins.input', side_effect=userInput):
            answer = objectQuestion()
        self.assertEqual("no", answer)
    
    # A check to see if the create object question works correctly. We feed the function a series 
    # of bad inputs until we hit quit and then see if the program exited as expected. 
    def test_objectQuestion_Quit(self):
        userInput = ["a","b", "c", "quit"]
        with mock.patch('builtins.input', side_effect=userInput):
            with self.assertRaises(SystemExit) as cm:
                objectQuestion()
        self.assertEqual(cm.exception.code, 0)        
        
    # Test to see if what is returned by the read file function is what is expected. It is just a dict with one entry
    # containing the info from the test1.json file which just has the first json object from photos.json
    def test_ReadFile(self):
        parsedJson = {1: [[1, 'accusamus beatae ad facilis cum similique qui sunt', 'https://via.placeholder.com/600/92c952', 'https://via.placeholder.com/150/92c952']]}
        self.assertEqual(parsedJson, readFile(jsonFileCheck("test1.json")), "ReadFile check")
        
    
    # Test to see if what is printed to standard output by the dict of photo albums (non object) matches what we expect
    # The information in the file comes from test1.json which just contains the first json object from the
    # larger file and nothing else
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_StandardOutput_Non_Object(self, mock_stdout):
        file = readFile(jsonFileCheck("test1.json"))
        printFile(file, 1)
        excpectedOut = '\nPhoto Album 1 contains:\n\n[1] accusamus beatae ad facilis cum similique qui sunt\n'
        self.assertEqual(mock_stdout.getvalue(), excpectedOut)
    
    # Test to see if what is printed to standard output by the dict of photo album objects matches what we expect
    # The information in the file comes from test1.json which just contains the first json object from the
    # larger file and nothing else
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_StandardOutput_Object(self, mock_stdout):
        photoAlbums = createObjects(jsonFileCheck("test1.json"))
        photoAlbums[1].displayContents()
        excpectedOut = '\nPhoto Album 1 contains:\n\n[1] accusamus beatae ad facilis cum similique qui sunt\n'
        self.assertEqual(mock_stdout.getvalue(), excpectedOut)
   
    # Test of the main function to see if the output is what is expected when the program is given two correct
    # arguments. Information comes from test1.json. This tests the object version. 
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_Object_Both_Args(self, mock_stdout):
        userInput = ["yes"]
        with mock.patch('builtins.input', side_effect=userInput):
            main(["test1.json", "1"])
            excpectedOut = '\nPhoto Album 1 contains:\n\n[1] accusamus beatae ad facilis cum similique qui sunt\n'
            self.assertEqual(mock_stdout.getvalue(), excpectedOut)
    
    # Test of the main function to see if the output is what is expected when the program is given only one correct
    # argument. Information comes from test1.json. This tests the object version.    
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_Object_One_Arg(self, mock_stdout):
        userInput = ["1","yes"]
        with mock.patch('builtins.input', side_effect=userInput):
            main(["test1.json"])
            excpectedOut = '\nPhoto Album 1 contains:\n\n[1] accusamus beatae ad facilis cum similique qui sunt\n'
            self.assertEqual(mock_stdout.getvalue(), excpectedOut)    

    # Test of the main function to see if the output is what is expected when the program is given only no
    # arguments. Information comes from test1.json. This tests the object version.
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_Object_Empty_Arg(self, mock_stdout):
        userInput = ["test1.json", "1","yes"]
        with mock.patch('builtins.input', side_effect=userInput):
            main([])
            excpectedOut = '\nPhoto Album 1 contains:\n\n[1] accusamus beatae ad facilis cum similique qui sunt\n'
            self.assertEqual(mock_stdout.getvalue(), excpectedOut) 

    # Test of the main function to see if the output is what is expected when the program is given only two correct
    # arguments. Information comes from test1.json. This tests the non object version.             
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_Non_Object(self, mock_stdout):
        userInput = ["no"]
        with mock.patch('builtins.input', side_effect=userInput):
            main(["test1.json", "1"])
            excpectedOut = '\nPhoto Album 1 contains:\n\n[1] accusamus beatae ad facilis cum similique qui sunt\n'
            self.assertEqual(mock_stdout.getvalue(), excpectedOut)

    # Test of the main function to see if the output is what is expected when the program is given only one correct
    # argument. Information comes from test1.json. This tests the non object version.     
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_Non_Object_One_Arg(self, mock_stdout):
        userInput = ["1", "no"]
        with mock.patch('builtins.input', side_effect=userInput):
            main(["test1.json"])
            excpectedOut = '\nPhoto Album 1 contains:\n\n[1] accusamus beatae ad facilis cum similique qui sunt\n'
            self.assertEqual(mock_stdout.getvalue(), excpectedOut)

    # Test of the main function to see if the output is what is expected when the program is given only no
    # arguments. Information comes from test1.json. This tests the object version. 
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_Non_Object_Empty_Args(self, mock_stdout):
        userInput = ["test1.json","1", "no"]
        with mock.patch('builtins.input', side_effect=userInput):
            main([])
            excpectedOut = '\nPhoto Album 1 contains:\n\n[1] accusamus beatae ad facilis cum similique qui sunt\n'
            self.assertEqual(mock_stdout.getvalue(), excpectedOut)

            
if __name__ == "__main__":
    '''The buffer=True below suppresses output to standard output, if you want to see the error messages printed just remove it'''
    unittest.main(buffer=True)