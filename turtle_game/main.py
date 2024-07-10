import turtle as turtle_module
import random

is_race_on = False

screen = turtle_module.Screen()
screen.setup(height=400, width = 500)
user_input = screen.textinput(title="Make a bet",prompt="Which turtle win the race? Enter the color?")

color = ["red","blue","yellow","green","orange","purple"]
y_positions = [-70 , -40 , -10 , 20 , 50, 80]
all_turtle = [] 

for turtle_index in range(0,6):
    new_turtle = turtle_module.Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x= -230 , y = y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0 , 10)    
        turtle.forward(random_distance)
   

screen.exitonclick()