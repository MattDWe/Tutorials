"""
This program reads inputted passwords and gives results on the strength of that password.
Project is from Automate The Boring Stuff Chapter 7
"""
import re

password = input("""Please enter a password and we will return the strength.
Tips for a strong password:
    More than 8 digits long (Longer the better)
    Contains both uppercase and lowercase characters.
    Has at least one digit.

Password: """)

passwordStrengthRating = 0

if len(password) >= 8:                                      #Password Length Check
    passwordStrengthRating += 1
else:
    passwordStrengthRating -= 1

caseRegex = re.compile(r"([A-Z]+)([a-z]+)")                 #Password Upper and Lower Case Check
mo = caseRegex.search(password)
try:
    upperCaseAmount = len(mo.group(1))
except:
    upperCaseAmount = 0
try:
    lowerCaseAmount = len(mo.group(2))
except:
    lowerCaseAmount = 0
try:
    letterAmount = len(mo.group())
except:
    letterAmount = 0
if upperCaseAmount == letterAmount:
    passwordStrengthRating -= 1
elif lowerCaseAmount == letterAmount:
    passwordStrengthRating -= 1
else:
    passwordStrengthRating += 1
    
digitRegex = re.compile(r"\d+")                             #Contains at least one digit check
numberOfDigits = len(digitRegex.findall(password))
if numberOfDigits == 0:
    passwordStrengthRating -= 1
elif numberOfDigits == len(password):
    passwordStrengthRating -= 1
elif numberOfDigits >= 1:
    passwordStrengthRating += 1

print("Your strength rating is " + str(passwordStrengthRating) + " (-3 to 3)")
