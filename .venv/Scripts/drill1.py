from turtle import *

shape("turtle")
def go_up():
    setheading(90)
    forward(100)
    stamp()
def go_down():
    setheading(270)
    forward(100)
    stamp()
def go_left():
    setheading(180)
    forward(100)
    stamp()
def go_right():
    setheading(0)
    forward(100)
    stamp()

onkeypress(go_up,"Up")
onkeypress(go_down, "Down")
onkeypress(go_left, "Left")
onkeypress(go_right, "Right")
listen()
mainloop()