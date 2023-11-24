from turtle import Turtle, Screen
import random

sam = Turtle()
screen = Screen()
screen.colormode(255)
sam.pendown()
screen.bgcolor("black")

for i in range(100):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    sam.setheading(i*5)
    sam.speed(100)
    sam.pencolor((r,g,b))
    sam.circle(radius= 100)


screen.exitonclick()