from turtle import *
screen = Screen()

shape("triangle")
shape = raw_input("What would you like to do? Choices: colorcircle, staircase, grid, octagon ")
colorchoice = raw_input("What color? Color must be typed in all lowercase, and must be in the color range for the turtle. ")

color(colorchoice)
if shape == "colorcircle":
    speed(0)
    for i in range(360):
        forward(300)
        backward(300)
        right(1)
        
if shape == "staircase":
    penup()
    goto(-300, -300)
    pendown()
    for i in range(10):
        forward(50)
        left(90)
        forward(50)
        right(90)
    forward(50)
    right(90)
    forward(500)
    right(90)
    forward(500)
    
if shape == "grid":
    for i in range(4):
        for i in range(4):
            forward(300)
            right(90)
        right(90)

if shape == "octagon":
    begin_fill()
    for i in range(8):
        forward(100)
        right(45)
    end_fill()
done()