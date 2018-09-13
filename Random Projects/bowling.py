#Program that will simulate bowling by allowing user to input the number of pins
#that have been knocked down and displaying the final score.
import turtle, random, time


def configureTurtle(): #Initial setup
    turtle.speed(0)
    turtle.hideturtle()
    turtle.color('blue')
    turtle.penup()
    resetPins()
    turtle.goto(-250, 170)
    turtle.write('Frames:', font=('Arial', 14, 'normal'))


def drawX():
    turtle.color('white')
    turtle.stamp()
    turtle.color('black')
    turtle.pendown()
    turtle.right(45)
    turtle.forward(10)
    turtle.forward(-20)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.forward(-20)
    turtle.forward(10)
    turtle.right(225)
    turtle.penup()


def resetPins():
    pins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    turtle.shape('circle')
    turtle.color('blue')
    turtle.goto(0,0)
    turtle.stamp()
    turtle.goto(0,-100)
    turtle.stamp()
    turtle.goto(30,-50)
    turtle.stamp()
    turtle.goto(-30,-50)
    turtle.stamp()
    turtle.goto(60,0)
    turtle.stamp()
    turtle.goto(-60,0)
    turtle.stamp()
    turtle.goto(-30,50)
    turtle.stamp()
    turtle.goto(-90,50)
    turtle.stamp()
    turtle.goto(30,50)
    turtle.stamp()
    turtle.goto(90,50)
    turtle.stamp()
    return pins


def knockpins(n, pins): #Randomly knocks down pins and removes that pin from the list
    knocked = 0
    while knocked < n:
        pin = random.choice(pins)
        pins.remove(pin)
        if pin == 1:
            turtle.goto(0,0)
            drawX()
        elif pin == 2:
            turtle.goto(0,-100)
            drawX()
        elif pin == 3:
            turtle.goto(30,-50)
            drawX()
        elif pin == 4:
            turtle.goto(-30,-50)
            drawX()
        elif pin == 5:
            turtle.goto(60,0)
            drawX()
        elif pin == 6:
            turtle.goto(-60,0)
            drawX()
        elif pin == 7:
            turtle.goto(-30,50)
            drawX()
        elif pin == 8:
            turtle.goto(-90,50)
            drawX()
        elif pin == 9:
            turtle.goto(30,50)
            drawX()
        elif pin == 10:
            turtle.goto(90,50)
            drawX()
        knocked += 1
    return pins


def numberofpins(n, score, pins): #Takes inputted hit pins and returns how many to knock down
    if n == '':
        n = random.randint(0,10)
    elif n == None:
        n = random.randint(0,10)
    if int(n) > len(pins):
        n = len(pins)
    else:
        n = int(n)
    score.append(n)
    return n, score


def strike(): #Write message when gets a strike
    turtle.goto(-30, 150)
    turtle.write('Strike!', font=('Arial', 16, 'normal'))
    time.sleep(2)
    turtle.undo()


def spare(): #Writes message when gets a spare
    turtle.goto(-30, 150)
    turtle.write('Spare!', font=('Arial', 16, 'normal'))
    time.sleep(2)
    turtle.undo()


def openframe(pins): #Writes message when open frame
    turtle.goto(-70, 150)
    turtle.write('Open frame ' + str(len(pins)), font=('Arial', 16, 'normal'))
    time.sleep(2)
    turtle.undo()


def finalScore(score): #Calculates ending game score
    points = 0
    i = 0
    temp = []
    for x in score:
        temp.append(x)
    for x in range(len(temp)):
        if x < len(temp) - 3:
            if temp[x] == 10:
                i += 1
            elif temp[x] + temp[x+1] == 10 and i%2 == 0:
                temp[x] = 0
                temp[x+1] = 100
            i += 1
    l = len(score)
    if temp[l-3] == 100 or score[l-3] == 10:
        if score[l-2] + score[l-1] < 10:
            if i%2 != 0 or i%3 != 0:
                score.append(0)
                temp.append(0)
    i = 0
    for x in range(len(score)):
        if x >= len(score) - 3:
            if score[x] == 10:
                points += 10
            else:
                points += score[x]
        elif score[x] == 10:
            points += 10 + score[x+1] + score[x+2]
        elif temp[x] == 100:
            points += 10 + score[x+1]
        elif temp[x] == 0:
            points
        else:
            points += score[x]
        i += 1
    return points


def main(): #Main game loop
    configureTurtle()
    frame = 1
    pins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    score = []
    while frame <= 10:
        turtle.goto(-250, 160 - (frame*20))
        turtle.write(frame, font=('Arial', 12, 'normal'))
        n = turtle.textinput('', 'Please enter number of pins knocked down(Or null for random) ')
        n, score = numberofpins(n, score, pins)
        pins = knockpins(n, pins)
        if pins == []:
            strike()
            pins = resetPins()
            if frame == 10:
                n = turtle.textinput('', 'Please enter number of pins knocked down(Or null for random) ')
                n, score = numberofpins(n, score, pins)
                pins = knockpins(n, pins)
                if pins == []:
                    strike()
                    pins = resetPins()
                    n = turtle.textinput('', 'Please enter number of pins knocked down(Or null for random) ')
                    n, score = numberofpins(n, score, pins)
                    pins = knockpins(n, pins)
                    if pins == []:
                        strike()
                    else:
                        openframe(pins)
                        pins = resetPins()
                else:
                    n = turtle.textinput('', 'Please enter number of pins knocked down(Or null for random) ')
                    n, score = numberofpins(n, score, pins)
                    pins = knockpins(n, pins)
                    if pins == []:
                        spare()
                        pins = resetPins()
                    else:
                        openframe(pins)
                        pins = resetPins()
                frame += 1
            else:
                frame += 1
        else:
            n = turtle.textinput('', 'Please enter number of pins knocked down(Or null for random) ')
            n, score = numberofpins(n, score, pins)
            pins = knockpins(n, pins)
            if pins == []:
                spare()
                pins = resetPins()
                if frame == 10:
                    pins = resetPins()
                    n = turtle.textinput('', 'Please enter number of pins knocked down(Or null for random) ')
                    n, score = numberofpins(n, score, pins)
                    pins = knockpins(n, pins)
                    if pins == []:
                        strike()
                    else:
                        openframe(pins)
                        pins = resetPins()
                    frame += 1
                else:
                    frame += 1
            else:
                openframe(pins)
                pins = resetPins()
                frame += 1
    points = finalScore(score)
    turtle.color('red')
    turtle.goto(-100,-200)
    turtle.write('Final Score: ' + str(points), font=('Arial', 24, 'normal'))
    time.sleep(5)


if __name__ == '__main__':
    main()
