from turtle import *

shape("turtle")
def go_up():
    setheading(90)
    forward(50)
    stamp()
def go_down():
    setheading(270)
    forward(50)
    stamp()
def go_left():
    setheading(180)
    forward(50)
    stamp()
def go_right():
    setheading(0)
    forward(50)
    stamp()
def tutle_reset():
    reset()
onkey(go_up,"w")
onkey(go_down, "s")
onkey(go_left, "a")
onkey(go_right, "d")
onkey(tutle_reset, "Escape")
listen()
mainloop()