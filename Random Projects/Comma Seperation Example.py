#This is a program project from Automate The Boring Stuff Ch 4
#This program takes a string and prints it with commas and an "and" at end
#To make it practical it's asking for a shopping list
i = 0
list = []
while True:
    string = input("An item you want to buy.(Press enter if no more items): ")
    if string == "":
        i = 1
        break
    else:
        list.append(string)
        i += 1

print(list)
lengthOfList = len(list)
print("Shopping List:")
for x in list:
    if i < lengthOfList and not i == lengthOfList - 1:
        print(x + ", ", end = "")
        i += 1
    elif i == lengthOfList - 1:
        print(x + ", and ", end = "")
        i += 1
    elif i == lengthOfList:
        print(x + ".")
