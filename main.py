import turtle as t
def move_forward():
    Annu.forward(10)

def move_backward():
    Annu.backward(10)

def counter_clockwise():
    Annu.setheading(Annu.heading()+10)

def clockwise():
    Annu.setheading(Annu.heading()-10)

def clear_screen():
    Annu.clear()
    Annu.penup()
    Annu.home()
    Annu.pendown()

Screen = t.Screen()
Annu = t.Turtle()
Annu.speed("fastest")


Screen.listen()
Screen.onkey(key='w', fun=move_forward)
Screen.onkey(key='s', fun=move_backward)
Screen.onkey(key='a', fun=counter_clockwise)
Screen.onkey(key='d', fun=clockwise)
Screen.onkey(key='c', fun=clear_screen)
Screen.exitonclick()