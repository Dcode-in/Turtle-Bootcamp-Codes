#Making a star
from turtle import*

bgcolor("black") 

for i in range(420):
    for j in range(4):
        forward(2 * i * j) 
        left(65)
        hideturtle()
        pensize(1)
        pencolor("white")
        goto(0,0)
        forward(25)
        speed(0)
penup()
goto(0,0)
forward(25)
left(33*2.5)
pendown() 


# goto function is used to change the postition of the turtle.
# penup function is used to pick pen up, so you can move turtle without leaving tracks.
# pendown function is used to lower the pen, so you can move the turtle and leave tracks.