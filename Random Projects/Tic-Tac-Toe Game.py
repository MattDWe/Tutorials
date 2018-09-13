#Basic Tic-Tac-Toe game in Python using dictionaries
#This project is suggested from Automate the Boring Stuff Chap 5
import pprint
theBoard = {"top-L": " ", "top-M": " ", "top-R": " ",
            "mid-L": " ", "mid-M": " ", "mid-R": " ",
            "low-L": " ", "low-M": " ", "low-R": " "}

def printBoard(board):
    print("")
    print(theBoard["top-L"] + "|" + theBoard["top-M"] + "|" + theBoard["top-R"])
    print("-+-+-")
    print(theBoard["mid-L"] + "|" + theBoard["mid-M"] + "|" + theBoard["mid-R"])
    print("-+-+-")
    print(theBoard["low-L"] + "|" + theBoard["low-M"] + "|" + theBoard["low-R"])


print("Move options are ")
pprint.pprint(list(theBoard.keys()))

turn = "X"
while True:
    printBoard(theBoard)
    move = input(turn + "'s turn. Take which space? (If there is a winner press enter.) ")

    if move not in theBoard: #Test if valid entry or to exit
        if move == "":
            print("Good Game!")
            break
        else:
            print("Not a valid move. Please try again.")
            continue
    elif theBoard[move] == " ": #Test if space taken
        theBoard[move] = turn
        if turn == "X": #Swapping turns
            turn = "O"
        else:
            turn = "X"
    else:
        print("\nSpace is taken. Please try again")
        continue
    
    if " " not in theBoard.values(): #Test if moves available
        printBoard(theBoard)
        print("\nNo more moves available. Good game!")
        break
