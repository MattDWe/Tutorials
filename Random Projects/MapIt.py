"""
Project from Automate The Boring Stuff Chapter 11
MapIt With The Webbrowser Module
Github: MattDWe
Program is to take address from clipboard and map it
"""

import webbrowser, pyperclip

#Get address from clipboard
address = pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/" + address)

