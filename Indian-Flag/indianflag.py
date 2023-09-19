import turtle
from turtle import*

#screen for output
screen = turtle.Screen()

# Defining a turtle Instance
t = turtle.Turtle()
speed(10)

# write text
# styling font
t.write("'We are Indians'",
font=("Verdana", 25, "bold"),
 align="center")

t.hideturtle()

# initially penup()
t.penup()
t.goto(-230, -40)
t.pendown()

# Orange Rectangle
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(450)
t.right(90)
t.forward(90)
t.right(90)
t.forward(450)
t.end_fill()
t.left(90)
t.forward(90)

# Green Rectangle
t.color("green")
t.begin_fill()
t.forward(90)
t.left(90)
t.forward(450)
t.left(90)
t.forward(90)
t.end_fill()

# Big Blue Circle
t.penup()
t.goto(45, -175)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(40)
t.end_fill()

# Big White Circle
t.penup()
t.goto(40, -175)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(35)
t.end_fill()

# Spokes
t.penup()
t.goto(5, -175)
t.pendown()
t.pensize(2)
t.color("navy")
for i in range(24):
	t.forward(35)
	t.backward(35)
	t.left(15)
	
turtle.done()
