from turtle import Turtle,Screen

sam = Turtle()
sam.shape('turtle')
sam.shapesize(2,2) #Height, Width, These cannot be zero
sam.color('#abcdef')
sam.speed(1)

n = int(input("Enter the number of sides(minimum 3) for the shape you want to draw: "))

for i in range(n):
    degrees = int(360/n)
    sam.forward(100)
    sam.right(degrees)











screen = Screen()
screen.exitonclick()