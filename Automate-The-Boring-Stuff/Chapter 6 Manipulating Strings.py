#Chapter 6 of Automate The Boring Stuff notes and examples

#Escape Characters:
    # \' Single Quote
    # \" Double Quote
    # \t Tab
    # \n Newline
    # \\ Backslash
    # r" Raw String

print("Hello there! \nHow are you? \nI\'m doing fine.")

#You can use r to make a raw string that ignores all escape characters
print(r"That is Carol\'s cat.")

#You can also use indentation to format strings by using ''' or """
print("""Dear Matt,

I am pretty sure you might be the best person in the whole world!

Love,
Matt""")

"""
I wish I knew this method of writing comments before
It would have been pretty helpful when my comments got a little long
"""

#Strings are like lists in how it is indexed

spam = "Hello World!"
for letters in spam:
    print(letters)

print(spam[0:5])

"""
Functions for formatting Strings:
    upper() Makes uppercase
    lower() Makes lowercase
    isupper() Gives true or false
    islower() Gives true or false
"""
print(spam.upper())
print(spam.lower())

#upper and lower are helpful when looking for an exact string

"""
More isX string methods:
    isalpha() Gives true or false if consists only of letters and is not blank.
    isalnum() Gives true or false if consists of letters and numbers and is not blank.
    isdecimal() Gives true or false if only consists of numeric characters and is not blank.
    isspace() Gives true or false if consists of tabs, spaces, and new lines and is not blank.
    istitle() Gives true or false if formatted by Uppercase letter then lower case for the rest
            Example Uppercase Words
Helpful for verifiying users entries
"""

while True:
    age = input("Enter your age: ")
    if age.isdecimal():
        break
    print("Not a valid age.")
    
while True:
    password = input("Please type in a password only using letters and numbers: ")
    if password.isalnum():
        break
    print("Only can include numbers and letters.")

#startswith() and endswith() returns true or false if string ends or begins with given string

#join() and split() used to join or split a string

string = ", ".join(["Blarg", "Nope", "Yes"])
print(string)
string = "ABD".join(["My", "Name", "Is", "Simon"])
print(string)

string = "My name is Matt".split()
print(string)
string = "MyABCnameABCisABCMatt".split("ABC")
print(string)

"""
Justifying Text
    rjust()
    ljust()
    center()
"""

print("Hello".rjust(30))
print("Hello".rjust(20,"-"))
print("Hello".center(20, "-"))

def printPicnic(itemDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, "-"))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth, ".") + str(v).rjust(rightWidth))

picnicItems = {"Waffles": 10, "Cheese": 4, "Apples": 234}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

"""
Removing white space
    strip() Strips white space on both sides of strings
    rstrip() Strips white space from the right side of the string
    lstrip() Strips the white space from the left side of the string
"""

string = "       Hello World        "
print(string.strip())
print(string.lstrip())
print(string.rstrip())

#Can also specify what to remove instead of whitespace

import pyperclip #That was annoying to install
pyperclip.copy("Hello World")
print(pyperclip.paste())

"""
1. Escape Characters:
     \' Single Quote
     \" Double Quote
     \t Tab
     \n Newline
     \\ Backslash
     r" Raw String
2. new line and tab
3. \\
4. Because using double quotes
5. You can format the string with the print using \"""
6. e, Hello, Hello, o world!
7. HELLO, True, False
8. ["Remember,", "remember," "the fifth of November."]
    "There-Can-be-only-one"
9. Justifying Text
    rjust()
    ljust()
    center()
10. Removing white space
    strip() Strips white space on both sides of strings
    rstrip() Strips white space from the right side of the string
    lstrip() Strips the white space from the left side of the string
"""
