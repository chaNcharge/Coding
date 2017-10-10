import turtle
from math import sin, cos, pi
from colorsys import hsv_to_rgb
r=350
inc=2*pi/100
t=0;n=1.95

turtle.bgcolor("black")
#turtle.tracer(0, 0)
turtle.speed(10)
for i in range(100):
	color = hsv_to_rgb(i/100.0, 1.0, 1.0)
	turtle.color(color)
	x1=r*sin(t);  y1=r*cos(t)
	x2=r*sin(t+n);y2=r*cos(t+n)
	turtle.penup(); turtle.goto(x1,y1)
	turtle.pendown(); turtle.goto(x2,y2)
	t+=inc
#turtle.update()
turtle.done()