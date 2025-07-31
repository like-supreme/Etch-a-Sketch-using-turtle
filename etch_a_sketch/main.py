""" w for forward
s for backward
d for clockwise
a for counterclockwise
c for clear and turtle will return to center
"""
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_clockwise():
    tim.right(10)  

def turn_counter_clockwise():
    tim.left(10)   

def clear_screen():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.setheading(0) 
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_clockwise, "d")
screen.onkey(turn_counter_clockwise, "a")
screen.onkey(clear_screen, "c")

screen.exitonclick()
  
       
