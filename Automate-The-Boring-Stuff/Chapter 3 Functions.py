#Chapter 3 of Automate the Boring Stuff notes and exercises

def hello():
    print("Hello")
    print("Howdy!")
    print("Como estas")

hello()

def hello(name):
    print("Hello " + name)

hello("Matt")

#Magic 8ball program
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "100% Positive"
    elif answerNumber == 2:
        return "Likely"
    elif answerNumber == 3:
        return "Maybe"
    elif answerNumber == 4:
        return "Cheesecake"
    elif answerNumber == 5:
        return "Ask more questions"
    elif answerNumber == 6:
        return "Nope"
    elif answerNumber == 7:
        return "Not possible"
    elif answerNumber == 8:
        return "Try again"


spam = print("Hello!")
None == spam #This comes out as true because Python puts return None after every nonspecified line

print("Hello", end=" ")
print("World") #The end removes the new line command python adds automatically

print("Dog","Cat","Cheese", sep=", ")
#This tells the print to seperate each string with a comma

try:
    def spam():
        eggs = 31337
    spam()
    print(eggs)
except:
    print("This functions gives an error because the eggs variable is local to the function")

def spam():
    print(eggs)
eggs = 42
spam()
print(eggs)

#While you are allowed to have a local variable be the same name as a global avoid if possible

def spam():
    eggs = "spam local"
    print(eggs)
def bacon():
    eggs = "bacon local"
    print(eggs)
    spam()
    print(eggs)
eggs = "global123"
bacon()
print(eggs)

def spam():
    global eggs #This tells python to use the global variable of eggs in this function so changing in here will change the global variable
    eggs = "spam"
    
eggs = "global"
spam()
print(eggs)

def spam():
    global eggs
    eggs = "spam" #This is global
def bacon():
    eggs = "bacon" #This is local
def ham():
    print(eggs) #This is global
eggs = 43 #This is global
spam()
print(eggs) #Prints spam because of the spam function was called replacing the global variable of eggs

#Use try and except to test something and throw it back if it failed
def divide(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error, can not divide by zero")
print(divide(2))
print(divide(43))
print(divide(0))
print(divide(2))

#Another methods using try is

def divide(divideBy):
    return 42 / divideBy
try:
    print(divide(2))
    print(divide(0))
    print(divide(23)) #This print never gets used because to goes to the except when an error occurs
except ZeroDivisionError:
    print("Error, cannot divide by zero")

#This is a program for a guess the number game

import random
secretNumber = random.randint(1,20)
print("I'm thinking about a number 1 through 20")

for guessesTaken in range(1,7):
    print("Take a guess")
    guess = input("Guess: ")
    try:
        int(guess) + 1
    except:
        print("Please enter an actual number. Now you just wasted a guess.\n")
        continue
    guess = int(guess)

    if guess < secretNumber:
        print("\nYour guess is too low")
    elif guess > secretNumber:
        print("\nYour guess is too high")
    elif guess == secretNumber:
        print("You got it! The Number was " + str(guess))
        break
    print(str(guessesTaken) + " Guesses made out of 6\n")

#Practice Questions
#1. Saves you from repeating code
#2. When the function is called
#3. def
#4. Function call is when a function is actually being called to use
#5. 1
#6. They no longer exist outside the local scope
#7. It returns a local value from a function
#8. Python automatically puts return None after so None
#9. global variableName
#10. NoneType data type
#11. It imports the module areallyourpetsnamederic
#12. spam.bacon()
#13. using try and except
#14. try is the code that is being tested except is the code that is ran if try fails
