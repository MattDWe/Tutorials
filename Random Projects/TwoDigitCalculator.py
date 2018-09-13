#This program will work as a basic two value calculator.

while True:
    print("Please enter your first value.") 
    valueOne = input()
    try:                                            #Tests if value is a integer
        float(valueOne) + 1                         #If failed will loop back to start
    except:
        print("Error, please enter an actual value.")
        continue
    valueOne = float(valueOne)
    
    print("Please enter your second value.")
    valueTwo = input()
    try:
        float(valueTwo) + 1
    except:
        print("Error, please enter an actual value.")
        continue
    valueTwo = float(valueTwo)
    
    print("Would you like to Add Subtract Divide or Multiply?")
    sign = input()
    if sign == 'Add':
        solution = valueOne + valueTwo
    elif sign == 'Subtract':
        solution = valueOne - valueTwo
    elif sign == 'Divide':
        solution = valueOne / valueTwo
    elif sign == 'Multiply':
        solution = valueOne * valueTwo
    else:                                           #If string was not entered correctly will loop back to start
        print("Sorry you did not enter a recognized method. Please make sure you type your method exactly as listed.")
        continue
        
    print("Your solution is: " + str(solution))
    
    print("Do you have another equation?")
    quit = input("Yes or No: ")
    if quit == "Yes":
        continue
    elif quit == "No":
        print("Have a nice day!")
        break
