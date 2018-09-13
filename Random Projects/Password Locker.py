"""
Password Locker Program
Project from Automate The Boring Stuff
Password storage program
"""
import pyperclip, sys

passwords = {"email": "DOYOUKNOW", "blog":"1234", "reddit":"10"}

if len(sys.argv) < 2:
       print("Usage: python pw.py [account] - copy account password")
       sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print("Passowrd for " + account + " copied to cliboard.")
else:
    print("There is no account named " + account + ".")

