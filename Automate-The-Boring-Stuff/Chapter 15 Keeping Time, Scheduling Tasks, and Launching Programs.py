"""
Automate The Boring Stuff Chapter 15
Keeping Time, Scheduling Tasks, and Launching Programs
Github: MattDWe
"""

#Unix Epoch time seconds from 01-01-1970
import time
print(time.time())

def calcProd():
    #Calculate the product of the first 10000 numbers.
    product = 1
    for i in range(1, 10000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print("The result is %s digits long." % (len(str(prod))))
print("The program took %s seconds to run" % str(endTime - startTime))

#Pausing a program to x amount of seconds
for i in range(3):
    print("Tick")
    time.sleep(1)
    print("Tock")
    time.sleep(1)

now = time.time()
print(now)
print(round(now, 2))
print(round(now, 4))
print(round(now))

#Datetime based off system time

import datetime
print(datetime.datetime.now())

#Convert Unix epoch time to datetime
print(datetime.datetime.fromtimestamp(1000000))

#timedelta duration of time
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(str(delta))

"""
You can have a program pause until a certain date
import datetime
import time
halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2016:
    time.sleep(1)
"""

#Printing datetime more friendly
"""
%Y Year with century, as in '2014'
%y Year without century, '00' to '99' (1970 to 2069)
%m Month as a decimal number, '01' to '12'
%B Full month name, as in 'November'
%b Abbreviated month name, as in 'Nov'
%d Day of the month, '01' to '31'
%j Day of the year, '001' to '366'
%w Day of the week, '0' (Sunday) to '6' (Saturday)
%A Full weekday name, as in 'Monday'
%a Abreviated weekday name, as in 'Mon'
%H Hour (24-hour clock), '00' to '23'
%I Hour (12-hour clock), '01' to '12'
%M Minute, '00' to '59'
%S Second, '00' to '59'
%p 'AM' or 'PM'
%% Literal '%' character
"""

oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
print(oct21st.strftime("%Y/%m/%d %H:%M:%S"))

print(datetime.datetime.strptime("October 21, 2015", "%B %d, %Y"))

#Mulltithreading
import threading
print("Start of program.")

def takeANap():
    time.sleep(5)
    print("Wake up!")

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print("End of program.")

threadObj = threading.Thread(target=print, args=["Cats", "Dogs", "Frogs"], kwargs={"sep": " & "})
threadObj.start()

#Concurrency issues is when threads start to write over each other and can create bugs that are hard to debug

#Launching other programs from python

import subprocess
subprocess.Popen("C:\\Windows\\System32\\calc.exe")
print(calcProc.poll() == None)

#Passing Command Line Arguments to POpen()

#subprocess(["path of program to open", "file to be opened"])
#subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])

"""
Practice Questions
1. Way for computer to tell time by counting by seconds from Jan 1 1970
2. time.time()
3. time.sleep(5)
4. the rounded integer given
5. datetime object returns a specific moment in time timedelta returns durations
6. threadObj = threading.Thread(target=spam)
   threadObj.start()
7. Avoid using the same variables in different threads
8. subprocess.popen(["C:\\Windows\\System32", "calc.exe"])
"""

