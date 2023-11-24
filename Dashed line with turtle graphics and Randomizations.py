import random
from turtle import Turtle,Screen

sam = Turtle()
sam.shape('arrow')
sam.shapesize(1,1) #Height, Width, These cannot be zero
sam.color('white')
sam.speed(1)

# for i in range(15):
#     sam.pendown()
#     sam.forward(5)
#     sam.penup()
#     sam.forward(5)


#Random Movements being made by turtle

colors = ['antiquewhite','aqua','aquamarine3','azure4','blue','blueviolet','brown']
angle = [0,90,180,270]
sam.width(10)
screen = Screen()

def random_walk(n):
    for i in range(n):
        screen.colormode(255) #Allows to take color paramteres in the range of 0 to 255
        r = random.randint(0, 255)
        g= random.randint(0, 255)
        b = random.randint(0, 255)
        sam.pendown()
        sam.pencolor((r,g,b))
        sam.forward(20)
        sam.setheading(random.choice(angle))
        sam.forward(20)
        sam.speed(i)

random_walk(100)

screen.exitonclick()