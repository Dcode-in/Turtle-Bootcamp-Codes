from turtle import *

#Function explained
def my_turtle(inner=150, outer=17, angle=33): #Change as you'd like
    for i in range(inner): #inner loop create the number of loops it moves global
        for j in range(outer): #outer loop create the number of loops it moves local
            forward(0.2 * i * j) #moving forward from 0.2 pixels times inner and outer loop
            left(angle / 0.01) #moves left in the angle we have defines
            speed(0) #The fastest speed in turtle graphics
            hideturtle() #hides our turtle
            pencolor("navy") #pencolor is in this case navy. It has the best 3D effect

my_turtle()