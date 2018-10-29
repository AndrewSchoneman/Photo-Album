Photo Album

This project is an application to display the contents of a photo album which is provided by a .json file.
Specifically this code will take a .json file and a photo album and display the Id's and titles of all of
the photos contained in the album.

Getting Started

  In order to run this code you just need to provide command line arguments to the program in the form of
filename.json photo album num (with num being an actual integer). It is important that there be a number somewhere
in the arguments after the filename (note if multiple numbers are entered only the last one will be used). The
program will then prompt you if you want to create objects and you can specify yes or no or quit by typing quit.
If any of the arguments are incorrect (i.e. the file can't be opened or the photo album number doesn't exist) then
the program will prompt the user for a valid json file and photo album. It will not stop asking for valid input until
valid input is entered or the user types quit.

  If no command line arguments are provided then the program will prompt you for a filename and then a photo album. It will
perform the same checking to look for valid inputs and if none are found it will keeps asking for them forever until they
are provided or you quit typing quit.

After getting valid inputs you will see the contents of the photo album printed out the standard output.


Running the tests

The tests can by run in the PhotoAlbumTest.py file. All you need to do is run that file and you'll see the test outputs. There are 25 
tests and they test all aspects of the program. 

They build up from the more basic functions all way to the most complicated ones which are the drivers of the program. For example there 
is an important function in the program which checks to make sure that the user has input a valid photo album to view. The tests check 
to see what happens when the checker gets bad inputs until it gets a good input as well as if it exits the program correctly given the quit command.


Authors
Andrew Schoneman

License
Freeware
