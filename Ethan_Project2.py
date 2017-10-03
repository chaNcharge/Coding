from turtle import *
screen = Screen()

image = "sprite.gif"

addshape(image)
shape(image)
shape = raw_input("What would you like to do? Choices: colorcircle, staircase, square, octagon ")
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
    
done()