import sys, json
'''
@Author Andy Schoneman
A program to display the contents of a photo album as outlined in a .json file
 '''
# An object that is a storage class for a collection of photo objects. One thing that I did to make this 
# different than the non object storage method is that all of the photos are stored in a dictionary with keys
# corresponding to the photo id's. This has its pros and cons. We can get constant lookup time for photos and
# we can more easily edit their content, but there won't be any duplicates (or rather photos, even if they're 
# different but have the same photo id) which could be a pro or a con depending on what we're trying to do. 

class PhotoAlbumObj():
    def __init__(self, albumId):
        self.albumId = albumId
        self.photos = {}
    
    # method to add photos to the photo album and just checks to ensure that actual photo objects are added    
    def addPhoto(self, photo):
        if type(photo) == Photo:
            self.photos[photo.idNum] = photo
        else:
            raise ValueError("Only photos may be added to a photo Album")
    
    # Prints out the name of the photo album and all of the photos it contains
    def displayContents(self):
        print("\nPhoto Album {self.albumId} contains:\n".format(self=self))
        for photo in self.photos:
            self.photos[photo].idAndTitle() 
    
    # defines equality for photo albums. 
    def __eq__(self, other):
        if self is other:
            return True
        elif type(other) != PhotoAlbumObj:
            return False
        else:
            if self.albumId == other.albumId:
                for photo in self.photos:
                    if photo not in other.photos:
                        return False
                    elif self.photos[photo] != other.photos[photo]:
                        return False
                return True
            else:
                return False
    # The string representation of the photoAlbum object
    def __str__(self):
        return "Photo Album {self.albumId} containing {0} photos".format(len(self.photos), self=self)

# A photo class which creates a Photo object which stores all of the information 
# about the photo provided in the .json file
class Photo():
    def __init__(self, idNum, title, url, thumbnail):
        self.idNum = idNum
        self.title = title
        self.url = url
        self.thumbnail = thumbnail
        
        if type(idNum) != int:
            raise ValueError("PhotoAlbum Id must be an integer")
         
    # Prints off the photo Id and title
    def idAndTitle(self):
        print("[{self.idNum}] {self.title}".format(self=self))
    
    # Defines equality for photo objects 
    def __eq__(self, other):
        if self is other:
            return True
        elif type(other) != Photo:
            return False
        else:
            return self.idNum == other.idNum and self.title == other.title and self.url == other.url and self.thumbnail == other.thumbnail
    
    def __str__(self):
        return "Id: {self.idNum} \nTitle: {self.title} \nURL {self.url} \nThumbnail {self.thumbnail}".format(self=self)

# Creates a dictionary of PhotoAlbum objects filled with photos that have the same photo album id
# the keys to the dictionary are the photo album id's
def createObjects(file):
    photoAlbum = {}
    for entry in file:
        if int(entry['albumId']) not in photoAlbum:
            photoAlbum[int(entry["albumId"])] = PhotoAlbumObj((int(entry['albumId'])))
            photoAlbum[int(entry['albumId'])].addPhoto( Photo(int(entry['id'] ), entry["title"], entry['url'], entry['thumbnailUrl']))
        else:
            photoAlbum[int(entry["albumId"])].addPhoto(  Photo(int(entry['id']) , entry["title"], entry['url'], entry['thumbnailUrl']))  
    return photoAlbum

# Asks the user if they'd like to create objects. Loops infinitely until it gets a valid
# answer. Upon getting one it returns either a string or quits out of the program
def objectQuestion():
    while True:
        userInput = input("Would you like to create objects? Type yes for yes, no for no, or quit to quit: ")
        try:
            if userInput.strip(" !@#$%^&*()\"\'\?/-+,.:;`~").lower() == "yes":
                return "yes"
            elif  userInput.strip(" !@#$%^&*()\"\'\?/-+,.:;`~").lower() == "no":
                return "no"
            elif  userInput.strip(" !@#$%^&*()\"\'\?/-+,.:;`~").lower() == "quit":
                sys.exit(0)
            else:
                raise ValueError
        except ValueError:
            print("Command {} not recognized".format(userInput))
            
# Reads the contents of the .json file provided and then returns a dictonary that has keys corresponding to
# to the photo album id's in the file and those keys are to a list of lists which contains the information
# about the various photos in the album                                                                                  
def readFile(file):
    photoAlbum = {}
    for entry in file:
        if int(entry['albumId']) not in photoAlbum:
            photoAlbum[int(entry["albumId"])] = [ [entry['id'] , entry["title"], entry['url'], entry['thumbnailUrl']] ]
        else:
            photoAlbum[int(entry["albumId"])].append(  [entry['id'] , entry["title"], entry['url'], entry['thumbnailUrl']]  )
    return photoAlbum

# prints the contents of the read file. The photo album is the dict returned by read file and the num is 
# the photo album that we want to view the contents of
def printFile(photoAlbum, num):
    print("\nPhoto Album {} contains:\n".format(num))
    for entry in photoAlbum[num]:
        print("[" + str(entry[0]) + "] " + entry[1])

# This is a check to ensure that the user has entered a valid photo album in either the command line or as 
# user input. If an invalid input is found the program loops forever until it gets a valid response or quits.
def check(album, size):
    # check to see if we got a valid input form the user or command line. If we strip away all non number
    # characters and are left with nothing then we know the entry is invalid
    if len(album.lower().strip("abcdefghijklmopqrstuvwxyz!@#$%^&*()\"\'\?/+,.:;`~").split() ) >= 1:      
        try:
            # If something remains try and convert it to an int. If more than one number is entered then
            # we only grab the last one
            index = int(album.lower().strip("abcdefghijklmopqrstuvwxyz!@#$%^&*()\"\'\?/+,.:;`~").split()[-1])
            # check that the int not zero or negative and not greater than the number of photo albums
            if index > size or index < 1:
                raise ValueError
        except ValueError:
            # found a bad photo album number so we need to warn the user and ask for a correct one
            print("Photo Album {} not recognized. Please enter a valid photo album ex Photo Album 2".format(album))
            while True:
                try:
                    userInput = input("Please enter a valid Photo Album number or type quit to quit: ")
                    # if the user wants to quit we quit else we perform similar logic as we did previously
                    if userInput.strip(" !@#$%^&*()\"\'\?/-+,.:;`~").lower()  == "quit":
                        sys.exit(0)  
                    elif len(userInput.lower().strip("abcdefghijklmopqrstuvwxyz!@#$%^&*()\"\'\?/+,.:;`~").split() ) >= 1:
                        index  = int(userInput.lower().strip("abcdefghijklmopqrstuvwxyz!@#$%^&*()\"\'\?/+,.:;`~").split()[-1])
                        if index > size or index < 1:
                            raise ValueError
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Photo Album {} not recognized".format(userInput))
    else:
        # We already know the user input/command line argument is bad so we ask for a correct argument
        print("Photo Album {} not recognized. Please enter a valid photo album ex Photo Album 2".format(album))
        while True:
            try:            
                userInput = input("Please enter a valid Photo Album number or type quit to quit: ")
                if userInput.strip(" !@#$%^&*()\"\'\?/-+,.:;`~").lower()  == "quit":
                    sys.exit(0)                
                elif len(userInput.lower().strip("abcdefghijklmopqrstuvwxyz!@#$%^&*()\"\'\?/-+,.:;`~").split() ) >= 1:
                    index  = int(userInput.lower().strip("abcdefghijklmopqrstuvwxyz!@#$%^&*()\"\'\?/+,.:;`~").split()[-1])
                    if index > size or index < 1:
                        raise ValueError
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Photo Album {} not recognized. Please enter a valid photo album ex Photo Album 2".format(userInput))
                continue
        
    return index

# A function to try and see if the user or command line .json file is entered correctly. If not it will
# as the user for a valid .json file or give them an option to quit. After it gets a valid .json file
# it will return the information. 
def jsonFileCheck(file):
    json_data = ""
    noSuchFile = False
    while True:
        try:
            # check to see if what was entered ends with .json
            if file.endswith(".json") and not noSuchFile:
                # if so try and open the file and read its contents
                with open(file) as f:
                    json_data =  json.load(f)
            else:
                # else we know that the whatever is entered cannot be correct so we ask for the file again
                file = input("{0} is not a valid .json file. Please enter a valid .json file or type quit to quit: ".format(file))
                with open(file) as f:
                    json_data =  json.load(f)
            break
        except IOError:
            noSuchFile = True
            # check to see if the user asks to quit and if so quit
            if file.strip(" !@#$%^&*()\"\'\?/-+,.:;`~").lower() == "quit":
                sys.exit(0)
    return json_data
    

def main(argv):
    photoAlbumFile = ""
    albumToView = ""
    # if no commandLine args are given then we ask the user for the file and 
    # the photo album to view
    if len(argv) == 0:
        photoAlbumFile = input("Please enter the name of the .json file ")
        albumToView = input("Please enter the photo album to view ex \"Photo Album 2\" ")
    # If one argument is present then we make the assumption they entered the file name since
    # that's supposed to be the filename anyway then ask the user for the photo album
    elif len(argv) == 1 :
        photoAlbumFile = argv[0]
        albumToView = input("Please enter the photo album to view ex \"Photo Album 2\" ") 
    # Else if there is more than one argument given we treat the first arg as the filename and the 
    # rest as the album to look at since the user can type something like "photo album 2" all we really care
    # is that it contains a number
    else:
        photoAlbumFile = argv[0]
        for val in argv[1:]:
            albumToView += " " + val
    # Ask if the user wants to create objects or just print the file
    answer  = objectQuestion()
    if answer == "no":
        album = readFile( jsonFileCheck(photoAlbumFile))    
        printFile(album, check(albumToView, len(album)))
    elif answer == "yes":
        photoAlbums = createObjects(jsonFileCheck(photoAlbumFile))
        photoAlbums[check(albumToView, len(photoAlbums))].displayContents()
                    
# calls main to get the program started. The args are the command line args provided by the user. 
if __name__ == "__main__":
    main(sys.argv[1:])
