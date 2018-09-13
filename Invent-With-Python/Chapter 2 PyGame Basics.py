"""
Invent With Python Chapter 2
PyGame Basics
Github: MattDWe
"""

import pygame, sys, time
from pygame.locals import *

"""
This opens a Pygame window with the header saying Hello World

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World")
while True: #Main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            continue
        pygame.display.update()
"""
#Colors
print(pygame.Color(255, 0, 0))
myColor = pygame.Color(255, 0, 0, 128)
print(myColor == (255, 0, 0, 128))
#Rectangles
spamRect = pygame.Rect(10, 20, 200, 300)
print(spamRect == (10, 20, 200, 300))
print(spamRect.right)

"""
Attributes used for Rect objects
myRect.left The int value of the X-coordinate of the left side of the rectangle.
myRect.right The int value of the X-coordinate of the right side of the rectangle.
myRect.top The int value of the Y-coordinate of the top side of the rectangle.
myRect.bottom The int value of the Y-coordinate of the bottom side.
myRect.centerx The int value of the X-coordinate of the center of the rectangle.
myRect.centery The int value of the Y-coordinate of the center of the rectangle.
myRect.width The int value of the width of the rectangle.
myRect.height The int value of the height of the rectangle.
myRect.size A tuple of two ints: (width, height)
myRect.topleft A tuple of two ints: (left, top)
myRect.topright A tuple of two ints: (right, top)
myRect.bottomleft A tuple of two ints: (left, bottom)
myRect.bottomright A tuple of two ints: (right, bottom)
myRect.midleft A tuple of two ints: (left, centery)
myRect.midright A tuple of two ints: (right, centery)
myRect.midtop A tuple of two ints: (centerx, top)
myRect.midbottom A tuple of two ints: (centerx, bottom)
"""

pygame.init()
#Drawing and Colors
"""
This program draws some shapes
#Set up window
DISPLAYSURF = pygame.display.set_mode((500,400), 0, 32)
pygame.display.set_caption("Drawing")

#Colors
BLACK = (0, 0,  0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Draw on surface object
DISPLAYSURF.fill(WHITE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

pixObj = pygame.PixelArray(DISPLAYSURF)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
"""
#Animation
"""
Drawing
fill(color)
pygame.draw.polygon(surface, color, pointlist, width)
pygame.draw.line(surface, color, start_point, end_point, width)
pygame.draw.lines(surface, color, closed, pointlist, width)
pygame.draw.circle(surface, color, center_point, radius, width)
pygame.draw.ellipse(surface, color, bounding_rectangle, width)
pygame.draw.rect(surface, color, rectangle_tuple, width)
"""

"""
Program moves an image of a cat around in a box.
pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

#Window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Cat Animation")

WHITE = (255, 255, 255)
catImg = pygame.image.load(".\\cat.png")
catx = 10
caty = 10
direction = "right"

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == "right":
        catx += 5
        if catx == 280:
            direction = "down"
    elif direction == "down":
        caty += 5
        if caty == 220:
            direction = "left"
    elif direction == "left":
        catx -= 5
        if catx == 10:
            direction = "up"
    elif direction == "up":
        caty -= 5
        if caty == 10:
            direction = "right"

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
"""

#Fonts
"""
Program writes Hello world with green text and blue background
pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World!")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font("freesansbold.ttf", 32)
textSurfaceObj = fontObj.render("Hello World!", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
"""

#To enable anti-aliasing with text pass True with renders second parameter

#Sounds
soundObj = pygame.mixer.Sound("beeps.wav")
soundObj.play()
time.sleep(1)
soundObj.stop()
