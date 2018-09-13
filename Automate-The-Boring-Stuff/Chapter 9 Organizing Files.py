"""
Automate The Boring Stuff Chapter 9
Organizing Files
Github: MattDWe
"""

#Shutil Module copies, moves, renames, and deltes files in Python programs.

#Copying uses shutil
#Calling shutil.copy(source, destination) copies file at source and pastes it at destination.

#Shutil.copy( , ) will only copy a single file.
#Shutil.copytree( , ) will copy an entire folder and every folder and files contained in it.

#Moving and Renaming uses shutil
#shutil.move(source, destination) will move the file or folder at the path source to the destination.
    #This will overwrite a file automatically if it is already existing in that folder.
    #To rename and move shutil.move("C:\\bacon.txt", "C:\\eggs\\new_bacon.txt")
        #This will move the file to eggs folder and rename it to new_bacon.
    #if there is no folder that was described it will rename that source to the destination.

#Deleting uses os and shutil
#Below requires importing os
#Calling os.unlink(path) will delete the file at path.
#Calling os.rmdir(path) will delete the folder at path (This folder must be empty of any files or folders).
#Calling shutil.rmtree(path) will remove the folder at path and all files and folders contianed.

#Using import send2trash is a safe method of deleting.
#send2trash.send2trash(path) will send it to the trash bin instead of permanetly deleting.

#Renaming uses os
#Using os.walk() can be used to rename multiple folders.
#Below is an example using walk to walk through the multiple folders and files in a directory.
"""
import os

for folderName, subfolders, filenames in os.walk("C:\\delicous"):
    print("The current folder is " + folderName)

    for subfolder in subfolders:
        print(Subfolder of " + folderName + ": " + subfolder)
    for filename in filenames:
        print("File inside " + folderName + ": " + filename)
"""

"""
Using a for loop with os.walk() will walk through the directory tree.
os.walk() will return 3 values:
1. A string of the current folders's name.
2. A list of a strings of the folders in the current folder.
3. A list of string of the files in the current folders.
"""

#Compressing Files uses zipfile
#Zip files work like text files that are opened and closed.
#zipfile.ZipFile("name") Will create a zip file with the given name.
#nameOfZipFile.namelist() will return a list of the contained files and folders.
"""
Example of compressing a zipfile
exampleZip = zipfile.ZipFile("example.zip")
exampleZip.namelist()
exampleZip.close()
"""

#Extracting from zipfiles uses zipfile
#extractall() method for zipfile extracts all files and folders from the zip into the current directory.
"""
Example of extracting a zipfile
exampleZip = zipfile.ZipFile("example.zip")
exampleZip.extractall()
exampleZip.close()
"""
#extract() method will extract a single file from the ZIP.
"""
exampleZip.extract("spam.txt")
exampleZip.extract("spam.txt", "C:\\some\\new\\folders")
exampleZip.close()
"""

#Creating and adding to Zip Files using zipfile.
#Like text files using "w" will create a new zipfile and add the listed files.
"""
import zipfile
newZip = zipfile.ZipFile("new.zip", "w")
newZip.write("spam.txt", "compress_type=file.ZIP_DEFLATED)
newZip.close()
"""

"""
Practice Questions
1. shutil.copy() will copy one file/folder(Folder must be empty) copytree() will copy the whole folder and it's contents.
2. shutil.move("C:\\File to rename", "C:\\New Name")
3. send2trash is the safe method and shutil method permanetely deletes.
4. zipfile.ZipFile() first argument is the filename and second is the mode to open the zipfile in(read, write, or append).
"""
