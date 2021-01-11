#Making a torus

from turtle import *

	
#Version 2	

bgcolor("black")
for i in range(0, 4000, 6):
	pencolor("green")
	circle(150)
	left(523/100)
	
	forward(i/100 + 5)
	hideturtle()
	speed(0)
	
