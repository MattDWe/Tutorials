"""
Chapter 7 from Automate The Boring Stuff
"""

def isPhoneNumber(text): #Program to check if inputed text is a phone number
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print("415-555-4242 is a phone number")
print(isPhoneNumber("415-555-4242"))
print("Moshi moshi is a phone number")
print(isPhoneNumber("Moshi moshi"))
phoneNumber = str(input("Please enter a phone number\nEX. ###-###-####\n"))
print("Is " + phoneNumber + " a phone number?\n" + str(isPhoneNumber(phoneNumber)))

message = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office."
for i in range(len(message)):
    chunk = message[i:i+12] #Checks parts of string and runs through function
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
print("Done")
        
import re #Used for shortening the phone number function

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d") #Lists the format for the string to search for
mo = phoneNumRegex.search("My number is 415-555-4242.") #Searches the string for the given format
print("Phone number found: " + mo.group()) #Displays the whole group that was found

"""
Steps for using the regex module
1. Import Regex import re
2. Create a regex object with re.compile()
3. Pass the string through the object with the seach() method which returns a matched object
4. Call the match object group() to return the matched text
"""

phoneNumRegex = re.compile(r"(\d\d\d)-(\d\d\d-\d\d\d\d)") #Use parentheses to seperate groups
mo = phoneNumRegex.search("My number is 415-555-4242")

print(mo.group(1))
print(mo.group(2))
print(mo.group())

areaCode, mainNumber = mo.groups() #Using groups() you can call all groups at once
print(areaCode)
print(mainNumber)

phoneNumRegex = re.compile(r"(\(\d\d\d\)) (\d\d\d-\d\d\d\d)")
mo = phoneNumRegex.search("My phone number is (415) 555-4242.")
print(mo.group(1))
print(mo.group(2))

heroRegex = re.compile(r"Batman|Tina Fey")
mo1 = heroRegex.search("Batman and Tina Fey.")
print(mo1.group())

mo2 = heroRegex.search("Tina Fey and Batman.")
print(mo2.group())

#You can use | to seperate possible outcomes to search for

batRegex = re.compile(r"Bat(man|mobile|copter|bat)")
mo = batRegex.search("Batmobile lost a wheel")
print(mo.group())
print(mo.group(1))

#A ? can be used to match optional part of the pattern

batRegex = re.compile(r"Bat(wo)?man")
mo1 = batRegex.search("The adventures of Batman")
mo2 = batRegex.search("The adventures of Batwoman")
print(mo1.group())
print(mo2.group())

phoneRegex = re.compile(r"(\d\d\d-)?\d\d\d-\d\d\d\d")
mo1 = phoneRegex.search("My number is 415-555-4242")
mo2 = phoneRegex.search("My number is 555-4242")
print(mo1.group())
print(mo2.group())

#You can think of the ? as saying, “Match zero or one of the group preceding this question mark.”

#The asterisk is like the ? but instead of once it can be repeated any number of times

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search("The Adventures of Batman")
mo2 = batRegex.search("The Adventures of Batwoman")
mo3 = batRegex.search("The Adventures of Batwowowowoman")
print(mo1.group())
print(mo2.group())
print(mo3.group())

#The plus sign means match one or more

batRegex = re.compile(r"Bat(wo)+man")
mo1 = batRegex.search("The Adventures of Batwoman")
mo2 = batRegex.search("The Adventures of Batwowowowowowoman")
mo3 = batRegex.search("The Adventures of Batman")
print(mo1.group())
print(mo2.group())
print(mo3 == None)

#You can use curly brackets to show repitition

haRegex = re.compile(r"(Ha){3}")
mo1 = haRegex.search("HaHaHa")
mo2 = haRegex.search("Ha")
print(mo1.group())
print(mo2 == None)

#When given a range to search for it will always give the longest string

greedyHaRegex = re.compile(r"(Ha){3,5}")
mo1 = greedyHaRegex.search("HaHaHaHaHa")
print(mo1.group())

nongreedyHaRegex = re.compile(r"(Ha){3,5}?") #Using a ? takes the shortest string
mo2 = nongreedyHaRegex.search("HaHaHaHaHa")
print(mo2.group())

"""
Search() is limited to the first found object
finall() will list every string that follows the format
"""

phoneNumRegex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phoneNumRegex.findall("Cell: 456-456-4565 Work: 789-789-7898")
print(mo)

"""
Possible Character Classes For Compiler
\d 0-9
\D Any character that is not a numeric digit
\w Any letter, numeric digit, or the underscore character
\W any character that is not a letter, numeric digit, or the underscore character
\s Any space, tab, or newline character
\S Any chracter that is not a space, tab, or newline
"""

xmasRegex = re.compile(r"\d+\s\w+")
print(xmasRegex.findall("12 Drummers, 12, pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge"))

#Using [ ] you can make a more specific character class

vowelRegex = re.compile(r"[aeiouAEIOU]")
print(vowelRegex.findall("Robocop eats baby food. BABY FOOD."))

"""
A ^ can be used to signal the match must occur at the start of the searched text
A $ is for the end of the searched text
"""

beginsWithHello = re.compile(r"^Hello")
print(beginsWithHello.search("Hello World!"))

endsWithNumber = re.compile(r"\d$")
print(endsWithNumber.search("Your number is 42"))

#The . is a wildcard for matching

atRegex = re.compile(r".at")
print(atRegex.findall("The cat and bat and mat and flat and pat"))

#You can use .* combo to include everything

nameRegex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = nameRegex.search("First Name: Al Last Name: Sweigart")
print(mo.group())
print(mo.group(1))
print(mo.group(2))

#To have a nongreedy method add a ? and it will return shortest match

nongreedyRegex = re.compile(r"<.*?>")
mo = nongreedyRegex.search("<To serve man> for dinner.>")
print(mo.group())

#Using re.compile(".*", re.DOTALL) It will grab everything even newlines

noNewLineRegex = re.compile(".*")
print(noNewLineRegex.search("Serve the public trust.\nProtect the innocent.\nUphold the law.").group())
print()
newLineRegex = re.compile(".*", re.DOTALL)
print(newLineRegex.search("Serve the public trust.\nProtect the innocent.\nUphold the law.").group())

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Regex Symbols~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
? Matches zero or one of preceding group
* Matches zero or more of the preceding group
+ Matches one or more of the preceding group
{n} matches exactly n of the preceding group
{n, } matches n or more of the preceding group
{,m} matches 0 to m of the preceding group
{n,m}? or *? or +? performs a nongreedy match of the preceding group
^spam means the string must begin with spam
spam$ means the string must end with spam
. matches any character, except newline characters (Unless re.DOTALL is included)
\d \w \s match a digit, word, or space character, respectively
\D \W \S mach anything except a digit, word, or space character, respectively
[abc] matches any character between the brackets (a, b, or c will be returned)
[^abc} matches any character that isn't between the brackets
"""

#Matching text regardless of uppercase or lowercase using re.IGNORECASE or re.I

robocop = re.compile(r"robocop", re.IGNORECASE)
mo1 = robocop.search("Robocop is part man, part machine, all cop.")
print(mo1.group())
mo2 = robocop.search("ROBocop is part man, part machine, all cop.")
print(mo2.group())
mo3 = robocop.search("RoboCop is part man, part machine, all cop.")
print(mo3.group())

#You can also substitute strings using sub()

namesRegex = re.compile(r"Agent \w+")
mo = namesRegex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob.")
print(mo)

#Using \1 will replace that spot with the the first letter of the matched string

agentNamesRegex = re.compile(r"Agent (\w)\w*")
mo = agentNamesRegex.sub(r"\1****", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.")
print(mo)

#Using re.VERBOST you can tell the compiler to ignore whitespace and comments inside the string
#Instead of this
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')

#You can do this
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)


#Since re.compile can only have one extra argument you can use | to seperate it
someRegexValue = re.compile("foo", re.IGNORECASE | re.DOTALL)

"""
Pratice Questions
1. re.compile()
2. r is used so it ignores \
3. search() returns a matched object
4. group()
5. group 0 will print both groups group 1 will be the first 3 digits and group 2 is the rest of the digits
6. Add a backslash before the paraenthesis or periods
7. List if there is no groups tuple if there are
8. it is a pipe and it means either or
9. Means zero or one
10. + means one or more and * is zero or more
11. {3} will take first 3 characters exactly {3,5} will take 3rd place to the 5th place
12. \d is any digit \w is any word and \s is any space character 
13. \D is anything but a digit \W is anything but a word \S is anything but a space character
14. re.IGNORECASE
15. Characters and ignores newlines if re.DOTALL is included it will include newlines
16. .* will return greedy match and will take as much as possible .*? will return nongreedy and the shortest match
17. [a-z0-9]
18.  It will replace any digit with the letter X
19. It will ignore newlines and allow you to make comments
20. commaRegex = re.compile(r"^\d{1,3}(,\d{3})*$")
21. lastNameRegex = re.compile(r"[A-Z]{1}[a-z]* (Nakamoto)$")
22. sentanceRegex = re.compile(r"(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.", re.IGNORECASE)
"""
