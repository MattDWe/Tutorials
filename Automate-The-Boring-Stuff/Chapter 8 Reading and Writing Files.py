"""
Chapter 8 of Automate The Boring Stuff
Reading and Writing Files
Github: MattDWe
"""

#If you want to save variables even after the program has ended you need to write it to a file

import os

print(os.path.join("usr", "bin", "spam")) #Using join is useful to make a string of filenames

myFiles = ["accounts.txt", "details.csv", "invite.docx"]
for filename in myFiles:
    print(os.path.join("C:\\Users\\asweigart", filename))

print(os.getcwd())
os.chdir("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Automate The Boring Stuff")
print(os.getcwd())

"""
Dots can be used to specify easier ways to write paths
single period means "this directory"
two periods mean the parent folder
"""

try:
    os.makedirs("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Chapter 8")
except:
    print("File has already been created")

"""
os.path.abspath(path) will return a string of the absolute path
os.path.isabs(path) will return True or False based on if the string is absolute
os.path.relpath(path, start) will return a relative path from start path to path.

os.pathsplit() will give a tuple with the directory and the base name
same as using os.path.dirname() and os.path.basename()

to get a list of each folder would be calcFilePath.split(os.path.sep)
"""

print(os.path.getsize("C:\\Users\\Jon\\Documents\\For Fun\\Python")) #Will return size in bytes of the file

print(os.listdir("C:\\Users\\Jon\\Documents\\For Fun\\Python")) #Returns list of folders in path

totalSize = 0
for filename in os.listdir("C:\Windows\\System32"):
    totalSize = totalSize + os.path.getsize(os.path.join("C:\\Windows\\System32", filename))

print(totalSize)

"""
To ensure that a path exists so you do not crash the program use
os.path.exists(path) will return True if file or folder exists
os.path.isfile(path) will return True if path exists
os.path.isdir(path) will return True if the path argument exists and is a folder
"""

print(os.path.exists("D:\\")) #Checks if flash drive is plugged in

"""
Three steps of reading or writing files in python
1. open()
2. read()/write()
3. close()
"""
helloFile = open("C:\\Users\\Jon\\Documents\\For Fun\\Python\\Chapter 8\\hello.txt")
helloContent = helloFile.read()
print(helloContent)

sonnetFile = open("..\\Chapter 8\\sonnet29.txt")
print(sonnetFile.readlines())

baconFile = open("..\\Chapter 8\\bacon.txt", "w") #This file does not exist at first so it will create it
baconFile.write("Hello World!\n")
baconFile.close()

baconFile = open("..\\Chapter 8\\bacon.txt", "a") #a means append
baconFile.write("Bacon is not a vegetable.")

baconFile.close()
baconFile = open("..\\Chapter 8\\bacon.txt")
content = baconFile.read()
baconFile.close()
print(content)

#You can save variables in binary shelf files using shelve import

import shelve
shelfFile = shelve.open("..\\Chapter 8\\mydata")
cats = ["Zophie", "Pooka", "Simon"]
shelfFile["cats"] = cats
shelfFile.close()

shelfFile = shelve.open("..\\Chapter 8\\mydata")
print(type(shelfFile))
print(shelfFile["cats"])
shelfFile.close()

#You can also save variable susing pprint

import pprint
cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]
pprint.pformat(cats)

fileObj = open("myCats.py", "w")
fileObj.write("cats = " + pprint.pformat(cats) + "\n")
fileObj.close()

import myCats
print(myCats.cats)

"""
Practice Questions
1. relative path is relative to your current directory
2. An absolute path starts with C:\\
3. os.getcwd() will get the current directory and os.chdir() will change the current directory
4. . current folder and .. is parent folder
5. C:\bacon\eggs is the dir name and spam.txt is the base name
6. r for read w for write and a for append
7. It will overwrite the contents
8. read() will read everything on a single line readlines takes in \n
9. It resembles a dictionary with keys and values
"""
