#Chapter 5 of dictionaries and structuring data
#Book Automate the boring stuff

#Dictionaries work with key-value pairs

myCat = {"size": "fat", "color": "gray", "disposition": "loud"}

print(myCat["size"])
print("My cat has " + myCat["color"] + " fur.")

spam = {12345: "Password", 42: "Meaning of life"} #You can use integers as the key
print("What does the number 42 mean? " + spam[42])

#Different from lists and dictionaries are they are unordered

spam = ["cats", "dogs", "moose"]
bacon = ["dogs", "cats", "moose"]
print(spam == bacon) #Prints false

age = {"Matt": 18, "Joe": 32, "Jon": 22,}
spaceMan = {"Joe": 32, "Jon": 22, "Matt": 18}
print(age == spaceMan) #Prints True

#If a key does not exist but is called it will return a KeyError

#Example program for assigning birthdays to names
birthdays = {"Matt": "Jan 1", "Austin": "Aug 9"}
while True:
    name = input("Enter a name: (Press enter to quit) ")
    if name == "":
        break
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print(name + " is not registered in our logs")
        birthday = input("What is there birthday? ")
        birthdays[name] = birthday
        print(name + "'s birthday on " + birthday + " was added.")

spam = {"color": "blue", "age": 18}
print(spam.values()) #Prints values
print(spam.keys()) #Prints keys
print(spam.items()) #Prints both keys and values

#Using multiple assignment trick you can do this

spam = {"color": "blue", "age": 18}
for x, y in spam.items():
    print("Key: " + str(x) + " Value: " + str(y))

#You can check if a key or value is in a dictionary using this

spam = {"color": "blue", "age": 18}

print("color" in spam.keys()) #True
print("Matt" in spam.keys()) #False
print("blue" in spam.values()) #True

#An alternative is to use dictionary.get(key,fall back value)
print("My favorite color is " + str(spam.get("color","Rainbow!")))
print("Please grab " + str(spam.get("apples",0)) + " apples.")
                    
#You can shorten the following code using setdefault() method
spam = {"color": "blue", "age": 18} #Long version
if "glue" not in spam:
    spam["glue"] = "Don't eat glue"

spam = {"color": "blue", "age": 18} #Short version
spam.setdefault("glue", "Don't eat glue") #If the key already exists it will return the existing matching value

#Program to count the number of eat character in a sentence
message = str(input("Please enter a string: "))
count = {}

for character in message:
    count.setdefault(character, 0) #Checks if character is in message if it not it sets it to 0
    count[character] = count[character] + 1 #Adds 1 to the characters value
print(count)

#To print dictionaries in a more pretty way you import pprint for pprint() pformat()
import pprint
message = str(input("Please enter a string: "))
count = {}

for character in message:
    count.setdefault(character, 0) #Checks if character is in message if it not it sets it to 0
    count[character] = count[character] + 1 #Adds 1 to the characters value
pprint.pprint(count)

#Sometimes you need to have a dictionary in a dictionary
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
        return numBrought

print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))

#Practice questions
#1. emptyDictionary = {}
#2. dictionary = {"foo": 42}
#3. Dictionaries have a key matched with a value
#4. KeyError
#5. "cat" in spam checks all keys and values spam.keys() will only check keys
#6. "cat" in spam checks all keys and values spam.values() will only check values
#7. spam.setdefault("color","black")
#8. import pprint and pprint.pprint()
