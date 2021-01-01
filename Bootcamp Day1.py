from turtle import *

colors = ["red", "yellow", "blue", "orange", "white", "navy"]

steps = 3 # Change steps

bgcolor("black")

for i in range(360):
    forward(i * 3 / steps + 1)
    left(360 / steps + 1)
    pencolor(colors[i%6])
    hideturtle()
    speed(0)