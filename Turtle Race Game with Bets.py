import turtle
from turtle import Turtle, Screen
import random

turtles = []
screen = Screen()
screen.setup(width = 500, height = 400)
screen.colormode(255)
turtle_colors = ['violet','indigo','blue','green','yellow','red']
turtles = []
turtle.speed('fastest')
turtle.hideturtle()

user_bet = screen.textinput(title = "Place your bets!!", prompt = "Which turtle will win the race? Enter the color: ").lower()
print(user_bet)

is_race_on = True

for i in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.color(turtle_colors[i])
    new_turtle.penup()
    new_turtle.setx(-200)
    new_turtle.sety(-150 + (60*i+1))
    turtles.append(new_turtle)

if user_bet == True:
    is_race_on = True

while is_race_on:
    for some_turtle in turtles:
        if some_turtle.xcor() == 200:
            is_race_on = False
            winning_color = some_turtle.pencolor
            if winning_color == user_bet:
                turtle.write("Hoorayyy!! You Win. Congratulations")
            else:
                turtle.write(f"Oops! The {user_bet} turtle lost. Try Again Next Time!",font=("Verdana",
                                    15, "normal"),align = 'center')
        else:
            forward_spaces = random.randint(0, 10)
            some_turtle.forward(forward_spaces)

screen.exitonclick()
