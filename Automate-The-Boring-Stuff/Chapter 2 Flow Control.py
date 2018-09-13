# Operator Meanings
# == Equal to
# != Not equal to
# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or equal to

# Remember == is equal to and = assigns a value to something

# and or and not
# if elif and else
# while
# for

while True: 
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue #Will continue back to the start if Joe is not entered
    print('Hello, Joe. What is the password?')
    password = input()
    if password == 'swordfish':
        break #Breaks out of loop if password is entered
print('Access granted.')

print('My name is') # Will print Matt five times
for x in range(5):
    print('Matt')

for x in range(0, 10, 2):
    print(x) #Will print 0 2 4 6 8 Counts in intervals of 2

for x in range(5, 0 , -1): #Counts backwards
    print(x)

import random #importing to get the .randint command

for x in range(5):
    print(random.randint(1, 10))

import sys #importing to get the .exit command

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        #sys.exit()
        break

#Questions
#1. True and False capital letters
#2. and or not
#3. and - true true = true, true false = false, false false = false
#   or  - true false = true, true true = true, false false = false
#   not - true = false, false = true
#4. False, False, True, False, False, True
#5. != not equal to > greater < lower <= less or equal >= greater or equal == equal
#6. == checks if it is equal = assigns a value
#7. if blank is true then run code elif if blank is true than run code else run this for everything else
#8. sets spam = 0 checks if spam equals 10 which is false so exits and goes to print spam
#9.
spam = input('Enter 1, 2, or anything else')
if spam == 1:
    print('Hello!')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

#10. Ctrl-C
#11. Break breaks you out of a loop continue resets the loop
#12. range(10) will do something 10 times range(0,10) will count through 0 through 10 range(0, 10, 1) will count in 1 intervals from 0 till 10
#13.
for x in range(1, 10):
    print(x)
    
i = 0
while True:
    print(i)
    i = i + 1
    if i > 10:
        break
#14 spam.bacon()
    
