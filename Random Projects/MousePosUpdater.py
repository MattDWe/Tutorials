"""
Project From Automate The Boring Stuff Chapter 18
Project: Where Is The Mouse Right Now?
Program is to constantly update when the mouse moves and display the current position.
Github: MattDWe
"""

import pyautogui

print("Ctrl-C to quit.")

try:
    while True:
        #Get and print the mouse coordinates
        x, y = pyautogui.position()
        positionStr = "X: " + str(x).rjust(4) + " Y " + str(y).rjust(4)
        print(positionStr, end="")
        print("\b" * len(positionStr), flush=True)
except KeyboardInterrupt:
    print("Done.")
