"""
This program is created to automate finding phone numbers and email addresses in a long document.
This will take from your current clipboard and replace it with phone numbers and email addresses.
This project is from Automate The Boring Stuff Chapter 7
"""

import pyperclip, re

phoneRegex = re.compile(r"""(
    (\d{3}|\(\d{3}\))?                  #Area Code
    (\s|-|\.)?                          #Seperator
    (\d{3})                             #First 3 digits
    (\s|-|\.)                           #Seperator
    (\d{4})                             #Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2, 5}))?     #Extension
    )""", re.VERBOSE)

emailRegex = re.compile(r"""(
    [a-zA-Z0-9._%+-]+                   #Username
    @                                   #@
    [a-zA-Z0-9.-]+                      #Domain name
    (\.[a-zA-Z]{2,4})                   #Top-level domain
    )""", re.VERBOSE)

#Find matches from clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum += " x" + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copies to clipboard
if len(matches) > 0:
    pyperclip.copy("\n".join(matches))
    print("Copied to clipboard:")
    print("\n".join(matches))
else:
    print("No phone numbers or email addresses found.")
    
