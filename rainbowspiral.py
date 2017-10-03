import colorsys
import turtle
#turtle setup stuff goes here
turtle.bgcolor("black")
turtle.tracer(0, 0)
for i in range(1000):
	color = colorsys.hsv_to_rgb(i/1000.0, 1.0, 1.0)
	#compatibility quirk: on 2.7 and below, use i/1000.0
	turtle.color(color)
	turtle.forward(i)
	turtle.right(98)
turtle.update()
print ("Done!")
turtle.done()