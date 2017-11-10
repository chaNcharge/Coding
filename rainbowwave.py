#!/usr/bin/env python3
import turtle
from math import sin
def hueGen(hue = 0,val = 1, sat=1):
	"""Generates a 360 degree range of hues
	sat of 1 is full saturation, 0 is B & W.
	val of 1 is full color, 0 is black"""
	if 0 <= hue < 60:
		r = 1
		g = (hue/59) + (1-sat)*(59-hue)/59
		b = 1 - sat
		hueOut = (r*val,g*val,b*val)
	elif 60 <= hue < 120:
		r = ((1-(hue-60)/59) + (1-sat)*(1-(119-hue)/59))
		g = 1
		b = 1 - sat
		hueOut = (r*val,g*val,b*val)
	elif 120 <= hue < 180:
		r = 1 - sat
		g = 1
		b = ((hue-120)/59) + (1-sat)*(179-hue)/59
		hueOut = (r*val,g*val,b*val)
	elif 180 <= hue < 240:
		r = 1 - sat
		g = (1-(hue-180)/59) + (1-sat)*(1-(239-hue)/59)
		b = 1
		hueOut = (r*val,g*val,b*val)
	elif 240 <= hue < 300:
		r = ((hue-240)/59) + (1-sat)*(299-hue)/59
		g = 1 - sat
		b = 1
		hueOut = (r*val,g*val,b*val)
	elif 300 <= hue < 360:
		r = 1
		g = 1 - sat
		b = (1-(hue-300)/59) + (1-sat)*(1-(359-hue)/59)
		hueOut = (r*val,g*val,b*val)
	elif hue >= 360:
		hueOut = hueGen(hue % 360, val, sat)
	return hueOut

def waves(repeats):
	"""Draws nested colored sinusoids emerging from darkness"""
	for i in range(repeats):
		alex.up()
		alex.color(hueGen(i, 1*i/repeats, 1))
		alex.goto(-315,315 - i)
		alex.seth(45) # set heading
		x = alex.xcor()
		y = alex.ycor()
		f = i + 1
		for j in range(630):
			x = alex.xcor()
			alex.goto(x + 1, y + 25*sin(8*j/f + i/25)) # plot sines
			alex.down()
			x = alex.xcor()

turtle.tracer(0, 0)
wn = turtle.Screen()
wn.colormode(1)
turtle.bgcolor("black")
alex = turtle.Turtle()
alex.pensize(2)
alex.ht()
waves(700)
turtle.update()
turtle.done()