"""
Automate The Boring Stuff Chapter 18
Controlling The Keyboard And Mouse With GUI Automation
Github: MattDWe
"""

import pyautogui, time

#Controlling Mouse
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

print(pyautogui.size())
#Moving Mouse
for i in range(1): #Based on true position
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)

for i in range(1): #Based on mouse position
    pyautogui.moveRel(100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, -100, duration=0.25)

print(pyautogui.position())

#Click
pyautogui.click(10, 5) #Will click at this position

#Dragging mouse
time.sleep(5)
pyautogui.click()
distance = 200
while distance > 180:
    pyautogui.dragRel(distance, 0, duration=.2) #Move Right
    distance -= 5
    pyautogui.dragRel(0, distance, duration=.2) #Move Down
    pyautogui.dragRel(-distance, 0, duration=.2) #Move Left
    distance -= 5
    pyautogui.dragRel(0, -distance, duration=.2)#Move Up
    
#Scrolling
pyautogui.scroll(200)

time.sleep(5); pyautogui.scroll(100)

#Screenshot features that can create an image file based on current contents.
im = pyautogui.screenshot()
print(im.getpixel((0, 0)))
print(im.getpixel((50, 200)))
print(im.getpixel((50, 200)))
print(pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)))
print(pyautogui.pixelMatchesColor(50, 200, (255, 135, 144)))

#Controlling Keyboard
pyauto.click(100, 100); pyautogui.typewrite("Hello World!")

"""
Keyboard key string                                         Meaning

'a', 'b', 'c', 'A', 'B', 'C', '1', '2', '3', '!', '@', '#', and so on The keys for single characters
'enter' (or 'return' or '\n')                               The ENTER key
'esc'                                                       The ESC key
'shiftleft', 'shiftright'                                   The left and right SHIFT keys
'altleft', 'altright'                                       The left and right ALT keys
'ctrlleft', 'ctrlright'                                     The left and right CTRL keys
'tab' (or '\t')                                             The TAB key
'backspace', 'delete'                                       The BACKSPACE and DELETE keys
'pageup', 'pagedown'                                        The PAGE UP and PAGE DOWN keys
'home', 'end'                                               The HOME and END keys
'up', 'down', 'left', 'right'                               The up, down, left, and right arrow keys
'f1', 'f2', 'f3'                                            The F1 to F12 keys
'volumemute', 'volumedown', 'volumeup'                      The mute, volume down, and volume up keys (some keyboards do not have these keys, but your operating system will still be able to understand these simulated keypresses)
'pause'                                                     The PAUSE key
'capslock', 'numlock', 'scrolllock'                         The CAPS LOCK, NUM LOCK, and SCROLL LOCK keys
'insert'                                                    The INS or INSERT key
'printscreen'                                               The PRTSC or PRINT SCREEN key
'winleft', 'winright'                                       The left and right WIN keys (on Windows)
'command'                                                   The Command () key (on OS X) 'option' The OPTION key (on OS X)
"""

#Pressing and Releasing Keyboard
pyautogui.keyDown("shift"); pyauto.press("4"); pyautogui.keyUp("shift")

"""
Practice Questions:
1. Move mouse to top left or ctrl-c
2. pyautogui.size()
3. pyautogui.position()
4. moveTo is true position and moveRel is relative to mouse current position
5. .dragRel
6. .typewrite("Hello World")
7. See above
8. pyautogui.screenshot("screenshot.png")
9. pyautogui.PAUSE = 2
"""
