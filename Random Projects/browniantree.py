import turtle, random, math

def configureTurtle(): #Setup turtle environment
    screen = turtle.getscreen()
    screen.setworldcoordinates(0,0,199,199)
    turtle.hideturtle()
    screen.tracer(0)
    screen.update()
    turtle.bgcolor('gray')
    Turtle1 = turtle.Turtle()
    Turtle1.penup()
    Turtle1.goto(100,100)
    Turtle1.dot(10,'blue')
    Turtle1.hideturtle()
    return Turtle1, screen


def grid(): #Create coordinate grid with booleans
    m = []
    for i in range(0, 200):
        x = [False]*200
        m.append(x)
    m[100][100] = True #Seed
    return m


def polarToCartesian(radius, angle): #Convert polar to cartesian coords
    x = round(radius * math.cos(math.radians(angle))) + 100
    y = round(radius * math.sin(math.radians(angle))) + 100
    return x, y


def randomdirection(x,y): #Gives random direction for turtle to go to
    d = random.randint(1,4)
    if d == 1:
        return x + 1, y
    if d == 2:
        return x - 1, y
    if d == 3:
        return x, y + 1
    if d == 4:
        return x, y - 1


def radiusCheck(x,y,R): #Checks new radius to see if R needs to be increased
    newR = round(((x-100)**2 + (y-100)**2)**(1/2))
    if newR >= R:
        return newR
    else:
        return R


def randomwalk(Turtle1, m, n, R): #Go in random directions until stuck or gone 200 steps
    randangle = random.randrange(0,360)
    x, y = polarToCartesian(R+1,randangle)
    steps = 0
    neighbor = hasNeighbor(m,x,y)
    if x >= 0 and x <= 199 and y >= 0 and y <= 199:
        if hasNeighbor(m,x,y) == True:
            Turtle1.goto(x,y)
            Turtle1.dot(9,'blue')
            m[x][y] = True
            R = radiusCheck(x,y,R)
            return m, R
    while steps <= 200:
        x, y = randomdirection(x,y)
        steps += 1
        neighbor = hasNeighbor(m,x,y)
        if x >= 0 and x <= 199 and y >= 0 and y <= 199:
            if hasNeighbor(m,x,y) == True:
                Turtle1.goto(x,y)
                Turtle1.dot(9,'blue')
                m[x][y] = True
                R = radiusCheck(x,y,R)
                return m, R
        else:
            return m, R
    return m, R


def onGrid(x,y): #Will return false if x,y is not a value on grid
    if x < 0:
        return False
    if x > 199:
        return False
    if y < 0:
        return False
    if y > 199:
        return False
    return True


def hasNeighbor(m,row,col): #Return True if particle has neighbors
    if onGrid(row-1,col) == True and onGrid(row,col-1) == True:
        if m[row - 1][col - 1] != False:
            return True
    if onGrid(row-1,col) == True and onGrid(row,col) == True:
        if m[row - 1][col] != False:
            return True
    if onGrid(row-1,col) == True and onGrid(row,col+1) == True:
        if m[row - 1][col + 1] != False:
            return True
    if onGrid(row,col) == True and onGrid(row,col+1) == True:
        if m[row][col + 1] != False:
            return True
    if onGrid(row+1,col) == True and onGrid(row,col+1) == True:
        if m[row + 1][col + 1] != False:
            return True
    if onGrid(row+1,col) == True and onGrid(row,col) == True:
        if m[row + 1][col] != False:
            return True
    if onGrid(row+1,col) == True and onGrid(row,col-1) == True:
        if m[row + 1][col - 1] != False:
            return True
    if onGrid(row,col) == True and onGrid(row,col-1) == True:
        if m[row][col - 1] != False:
            return True
    return False


def main(): #Main program loop
    Turtle1, screen = configureTurtle()
    m = grid()
    n = int(turtle.textinput('','Please enter number of particles: '))
    R = 0
    particles = 1
    while particles <= n:
        screen.update()
        particles = 1
        for x in m:
            for y in x:
                if y == True:
                    particles += 1
        m, R = randomwalk(Turtle1, m, n, R)


if __name__=='__main__':
    main()
