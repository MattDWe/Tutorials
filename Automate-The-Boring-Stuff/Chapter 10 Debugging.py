"""
Chapter 10 of Automate The Boring Stuff
Debugging
Github: MattDWe
"""

"""
Exceptions are raised with a raise statement. This consists of three things.
The raise keyword
Exception() function
A string inside the exception() function

Example:
raise Exception("This is the error message.")
"""

#An example of using raise Exception()
def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    if height <= 2:
        raise Exception("Height must be greater than 2.")
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (" " * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (("*", 4, 4), ("0", 20, 5), ("x", 1, 3), ("ZZ", 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print("An exception happened: " + str(err))

"""
This is an example of a normal python errors traceback.
def spam():
    bacon()
def bacon():
    raise Exception('This is the error message.')

spam()
When you run errorExample.py, the output will look like this:


Traceback (most recent call last):
  File "errorExample.py", line 7, in <module>
    spam()
  File "errorExample.py", line 2, in spam
    bacon()
  File "errorExample.py", line 5, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message.
"""

#You can also import traceback to log an error and keep running the program

import traceback
try:
    raise Exception("This is the error message.")
except:
    errorFile = open("..\\Automate The Boring Stuff\\Chapter 10\\errorInfo.txt", "w")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written to errorInfo.txt.")

"""
Assertions are a sanity check to check if your program is doing something wrong. Using assert
statements it will reply an AssertionError if it fails.
Included:
Assert Keyword
A condition that will return True or False
A comma
A string to display when the condition is False
"""

#An example of using assert
podBayDoorStatus = "open"
assert podBayDoorStatus == "open", "The pod bay doors need to be \"open\"."
print("This passed")
#podBayDoorStatus = "I'm sorry, Dave. I'm afraid I can't do that."
#assert podBayDoorStatus == "open", "The pod bay doors need to be \"open\"."
#print("This does not pass")

market_2nd = {"ns": "green", "ew": "red"}
mission_a6th = {"ns": "red", "ew": "green"}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == "green":
            stoplight[key] = "yellow"
        elif stoplight[key] == "yellow":
            stoplight[key] = "red"
        elif stoplight[key] == "red":
            stoplight[key] = "green"
        assert "red" in stoplight.values(), "Neither light is red! " + str(stoplight)

#switchLights(market_2nd)
#This program triggers the assert function and passes an error

#To run a program skipping assertions you can use the -0 option.
    #Check Appendix B for how to do that

#Logging is to understand what is happening in your code.
#Like when when using print() to show a variable mid way through.

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

#Using logging.debug to show log information. Use this instead of print().
logging.debug("Message for logs")

"""
Debug - logging.debug() = Lowest level. Used for small details.
Info - logging.info() = Record information on general events to confirm things are working.
Warning - logging.warning() = Used to indicate a potential program that doesn't prevent the program from working but may in the future.
Error - logging.error() = Used to record an error that caused the program to fail to do something.
Critical - logging.critical() The highest level. Used to indicate a fatal eror.
"""
logging.debug("Debug Message")
logging.info("Info Message")
logging.warning("Warning Message")
logging.error("Error Message")
logging.critical("Critical Message")

#To disable logging after a you debugged a program you can use logging.disable()

#You can set the logging to save to a file
logging.basicConfig(filename="..\\Automate The Boring Stuff\\Chapter 10\\myProgramLog.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Test")

#IDLE's debugger allows you to execute your program one line at a time.
"""
To use the debugger you Debug -> Debugger
Tick stack, locals, source, and globals.
It will display line of code, list of local variables, and global variables.
Go - will cause the program to execute normally.
Step - Will cause the program to execute the next line of code.
Over - Will execute the next line of code like step. However if the next line is a function it will skip it.
Out - Will cause the program to continue until it exits the current function.
Quit - Will quit.
"""

#Breakpoints can be used to pause the debugger when it hits it. Right click set breakpoint.

"""
Practice Questions
1. assert spam >= 10, "AssertionError"
2. assert eggs.lower() != bacon.lower(), "AssertionError" or assert eggs.upper() != bacon.upper(), "AssertionError"
3. assert False, "AssertionError"
4. import logging and
    logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
5. import logging and
    logging.basicConfig(filename="..\\Automate The Boring Stuff\\Chapter 10\\myProgramLog.txt", level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
6. debug, info, warning, error, critcal
7. logging.disable()
8. Because it's not for the user to see
9. step goes to next line over will go over functions out will continue until exits function
10. At the end of the program or at a breakpoint
11. A point to pause the debugger
12. Right click breakpoint
"""
