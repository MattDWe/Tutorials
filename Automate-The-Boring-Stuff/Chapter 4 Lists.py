#Chapter 4 of Automate the Boring Stuff Lists

spam = ["Cat","Bat", "Rat", "Elephant"] #You can use lists to save multiple values to a varibale

print(spam)
print(spam[2])

#["Cat","Bat", "Rat", "Elephant"] Is in the form of [ 0, 1, 2, 3]

print("Hello " + spam[0])

try:
    print(spam[1000])
except:
    print("Spam[1000] is not in the list so it is passed as an error")

#Lists can contain other lists and accessed by stacking the brackets

spam = [["cat", "bat"], [10, 20, 30 ,40 ,50]]

print(spam[0][1])
print(spam[1][2])

#You can use negative numbers to call from the back of the list

spam = [1, 2, 3, 4, 5, 6, 7, 8]

print(spam[-1]) #Will take the first value from the back being 8

#A slice is getting multiple values from a list [ : ]

print(spam[1:3]) #Prints 2 and 3

print(len(spam)) #Gets length of the list and prints number of variables in the list being 8

#You can also change a certain value in the list

spam[1] = 4 #Replaces value in slot 1, being 2, to 4
print(spam[1])

#You can combine lists using + or duplicate a list using *
combineLists = ["A", "B", "C"] + [1, 2, 3]
duplicateLists = [1, 2, 3] * 3

print(combineLists)
print(duplicateLists)

#Using del statement you can remove a value from a list

spam = ["cat", "bat", "rat", "elephant"]

print(spam)
del spam[2]
print(spam)

#Program to record cat names and place into a list
catNames = []

while True:
    name = input("Enter the name of cat " + str(len(catNames) +1) + " (Or press enter to exit): ")
    if name == "":
        break
    elif name in catNames:
        print("You entered that name already")
        continue
    elif name not in catNames: #Use in and not in to check for duplicates
        catNames = catNames + [name]

if len(catNames) > 4:
    print("You have a lot of cats")
    
print("Your listed cat names are: ")

for name in catNames:
    print("   " + name)

for i in range(4): #This is a demonstration to show this creates something like a list
    print(i)

for i in [0, 1, 2, 3]:
    print(i)

#There are two ways to assign values to a list
#The second way is more prefered

cat = ["fat", "orange", "loud"]
print(cat)

size = cat[0]
color = cat[1]
disposition = cat[2]
print(size)
print(color)
print(disposition)

#Better method in one line

cat = ["fat", "orange", "loud"]
print(cat)

size, color, disposition = cat
print(size)
print(color)
print(disposition)

#Required that the number of variables matches the exact length of the list in order to do the one line method

#This method can also be used to switch two values

a, b = "Alice", "Bob"
a, b = b, a
print(a)
print(b)

#Shortcut for assigning variables using operations
spam = 42
print(spam)
spam = spam + 1
print(spam)

spam = 42
print(spam)
spam += 1
print(spam)
#Adding an = to the end of the operation assigns the new value to the variable name
#This can also be used to string multiplication and combination

spam = "Hello"
spam += " world!"
print(spam)

bacon = ["Zophie"]
bacon *= 3
print(bacon)

#Methods index() append() insert() remove() sort()
spam = ["hello", "hi", "howdy", "heyas"]
print(spam.index("hello")) #Index gives the position of the value
print(spam.index("howdy"))

#If there is a duplicate value in a list it will give the position of the first one listed in the list

spam = ["cat","dog","bat"]
spam.append("moose")
print(spam) #Append adds a value to the list at the end

spam = ["cat", "dog", "bat"]
spam.insert(1, "chicken")
print(spam) #Insert inserts a value to a specific position of the list

spam = ["cat", "bat", "rat", "elephant"]
spam.remove("bat")
print(spam) #Remove removes a specific string

spam = ["cat", "bat", "rat", "elephant"]
del spam[2]
print(spam) #del can be used when you know the exact position

spam = ["cat", "bat", "rat", "elephant"]
print(spam)
spam.sort() #ASCIIbetical order meaning smaller value goes first A B C a b c
print(spam)

spam = [3, 54, -1, 2]
print(spam)
spam.sort() #Smaller to bigger
print(spam)

spam = ["A", "B", "C", "D"]
print(spam)
spam.sort(reverse=True) #Using reverse=True it reverses the order
print(spam)

#For sort to work it has to have one type of value

#Magic 8ball program using lists
import random

messages = ["It is certain",
            "Definetely",
            "Maybe",
            "Ask again",
            "Probably",
            "Nope"]
print(messages[random.randint(0, len(messages) - 1)])

name = "Matt" #Strings are a lot like lists in you can call each letter by position
for letter in name:
    print("***" + letter + "***")

#Strings can not be changed like lists but you can use specific parts of a string
name = "Matt a person"
newName = name[0:5] + "the" + name[6:]
print(newName)

#Tuple is like a list but uses ( ) instead of [ ]

eggs = ("Hello", 42, .5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

#Like strings tuples can not have their values modified
#If you want to have a tuple with one value add a comma or python thinks it's just a normal value
#Use tuples if you have a list of values that you don't want changed

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = "Hello!"
print(spam)
print(cheese) #This is an example showing how when you assign a variable to another
              #string it uses that string as a reference calling back to it

#To avoid errors with referencing you use import copy and .copy
import copy
spam = [1, 2, 3]
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)

#Practice Questions
#1. Brackets that are used for a list
#2. Using spam = [2, 4, 6, 8, 10] spam[2] = "hello"
#3.  33/11=3 so spam[3] = 8
#4. 10
#5. 2, 4
#6. 1
#7. [3.14, 'cat', 11, 'cat', True, 99]
#8. [3.14, 11, 'cat', True, 99]
#9. list = [whatever] * 3 list = "whatever,Whatever" + "More stuff"
#10. Append adds to the end of the list. Insert inserts something at a specified point
#11. .remove() and del list[value]
#12. numbered like 0,1,2,3 for a word like bat and ["one","two","three","four"]
#    can be changed
#13. lists can be changed and tuples are permanent
#14. tuple = (42,)
#15. tuple = ([list,list,list]) list = ((list, list, list))
#16. They reference back to the original list that it was assigned to
#17. Copy copies the list and deepcopy copies a list that has lists inside of it


