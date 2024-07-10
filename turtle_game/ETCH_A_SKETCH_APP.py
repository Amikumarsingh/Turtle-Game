import turtle as turtle_module

tim = turtle_module.Turtle()



def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = turtle_module.Screen()
screen.listen()
screen.onkey(move_forwards,"f")
screen.onkey(move_backwards,"b")
screen.onkey(turn_left,"l")
screen.onkey(turn_right,"r")
screen.onkey(clear,"c")
screen.exitonclick()