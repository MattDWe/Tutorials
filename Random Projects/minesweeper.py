import turtle, random, math


class Cell: #Class for all cells on the field
    def __init__(self,xmin,xmax,ymin,ymax,t): #Creates new variables for the cell
        self.__xmin = xmin
        self.__xmax = xmax
        self.__ymin = ymin
        self.__ymax = ymax
        self.__t = t
        self.__bomb = False
        self.__cleared = False
    def isIn(self,x,y): #Returns True if x,y is inside the cell
        return (x <= self.__xmax and x >= self.__xmin and y <= self.__ymax and y >= self.__ymin)
    def setBomb(self): #Sets the cell to contain a bomb
        self.__bomb = True
    def isBomb(self): #Returns if cell contains a bomb
        return self.__bomb
    def clear(self): #Sets the cell to be cleared
        self.__cleared = True
    def isCleared(self): #Returns if the cell is cleared
        return self.__cleared
    def showCount(self,c): #Writes desired symbol onto desired cell
        fontsize = (self.__ymax-self.__ymin)//2
        self.__t.goto(self.__xmin+((self.__xmax-self.__xmin)/2.5),self.__ymin+((self.__ymax-self.__ymin)/5))
        self.__t.write(c,font=("Arial",fontsize))
    def cellColor(self): #Helper function returns color based on state of cleared or if it contains a bomb
        if self.__cleared == False:
            return 'lime'
        if self.__cleared == True:
            if self.__bomb == True:
                return 'red'
            else:
                return 'lightgrey'
    def draw(self): #Draws the cell
        color = self.cellColor()
        self.__t.penup()
        self.__t.goto(self.__xmin,self.__ymin)
        self.__t.color('black', color)
        self.__t.pendown()
        self.__t.pensize(1)
        self.__t.begin_fill()
        self.__t.goto(self.__xmin,self.__ymax)
        self.__t.goto(self.__xmax,self.__ymax)
        self.__t.goto(self.__xmax,self.__ymin)
        self.__t.goto(self.__xmin,self.__ymin)
        self.__t.end_fill()
        self.__t.penup()
        self.__t.hideturtle()


class Minesweeper:
    def __init__(self,rows,cols,mines,visbombs=False): #Sets variables and creates/draws grid
        self.__t = turtle.Turtle()
        self.__t.hideturtle()
        self.__s = self.__t.getscreen()
        self.__s.bgcolor('black')
        self.__s.setworldcoordinates(0,0,rows*30,cols*30)
        self.__s.tracer(0)
        self.__grid = []
        for row in range((rows//2),rows+(rows//2)):
            row *= 15
            newrow = []
            for col in range((cols//2),cols+(cols//2)):
                col *= 15
                newcell = Cell(row,row+15,col,col+15,self.__t)
                newrow.append(newcell)
                newcell.draw()
            self.__grid.append(newrow)
        i = 0
        while i < mines:
            x = random.randint(0,rows-1)
            y = random.randint(0,cols-1)
            if self.__grid[x][y].isBomb() == False:
                self.__grid[x][y].setBomb()
                i += 1
            if visbombs == True:
                self.__grid[x][y].showCount('*')
        self.__s.onclick(self.mouseClick)
    def countBombs(self,row,col): #Return number of bombs neighboring the cell
        bombs = 0
        for x in range(row-1,row+2):
            for y in range(col-1,col+2):
                if x >= 0 and y >= 0:
                    if self.onGrid(x,y) == True:
                        if self.__grid[x][y].isBomb() == True:
                            bombs += 1
        return bombs
    def drawBombs(self): #Helper function that shows locations of bombs after game end
        for row in self.__grid:
            for cell in row:
                if cell.isBomb() == True:
                    cell.clear()
                    cell.draw()
                    cell.showCount('*')
    def onGrid(self,row,col): #Returns True if row and col is valid cell on the grid
        try:
            if self.__grid[row][col] != 0:
                return True
        except:
            return False
    def cellsRemaining(self): #Return cells remaining to clear that do not contain bombs
        toClear = 0
        for row in self.__grid:
            for cell in row:
                if cell.isCleared() == False and cell.isBomb() == False:
                    toClear += 1
        return toClear
    def getRowCol(self,x,y): #Return the grid location of cell located at x,y
        for row in range(0,len(self.__grid)):
            for col in range(0,len(self.__grid[0])):
                if self.__grid[row][col].isIn(x,y):
                    return row, col
        return -1, -1
    def mouseClick(self,x=0,y=0): #Respond to user clicked cell also checks if end game requirements met.
        row, col = self.getRowCol(x,y)
        if row == -1 or col == -1:
            return
        if self.__grid[row][col].isCleared() == False:
            if self.__grid[row][col].isBomb() == True:
                self.__t.penup()
                self.__t.goto(0,0)
                self.__t.color('red')
                self.__t.write('''Game Over: You Lost... :'(
                    (Click To Exit)''',font=("Arial",20))
                self.drawBombs()
                self.__s.exitonclick()
            else:
                self.clearCell(row,col)
                if self.cellsRemaining() == 0:
                    self.__t.penup()
                    self.__t.goto(0,0)
                    self.__t.color('lime')
                    self.__t.write('''Game Over: You Won! :D
                    (Click To Exit)''',font=("Arial",20))
                    self.drawBombs()
                    self.__s.exitonclick()
    def clearCell(self,row,col,n=0): #Clear cell located at row,col and recursively clear cells around it
        if self.onGrid(row,col) and self.__grid[row][col].isCleared() == False and row >= 0 and col >= 0:
            bombs = self.countBombs(row,col)
            self.__grid[row][col].clear()
            self.__grid[row][col].draw()
            if bombs > 0:
                self.__grid[row][col].showCount(bombs)
                return
            else:
                self.clearCell(row+1,col+1)
                for x in range(row-1,row+2):
                    for y in range(col-1,col+2):
                        self.clearCell(x,y)


def main(): #Runs the Minesweeper class starting the game
    rows = 14
    cols = 14
    mines = 15
    Minesweeper(rows,cols,mines)


if __name__ == '__main__':
    main()
