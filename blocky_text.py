from turtle import *
import time as clock

cat_shape = [(0, 30),(10, 40),(15, 30),(30, 25),(30, -10),(15, -30),(0, -25),(-15, -30),(-30, -10),(-30, 25),(-15, 30),(-10, 40),(0, 30)]
screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("white")
register_shape("cat", cat_shape)

cat = Turtle()
cat.shape("cat")
cat.color("orange", "white")
cat.speed(5)
cat.penup()

class Stage():
    def __init__(self, size=1.0):
        self.size=size

def move(amount, object):
    try:
        object.fd(amount*2)
    except TypeError:
        print("Error: The value is invalid. Check that it's a number!")
    except:
        print("Uh oh! Your code can't be read. Make sure you wrote it right.")

def turn(amount, object):
    try:
        object.rt(amount*2)
    except:
        print("Uh oh! Your code can't be read. Make sure you wrote it right.")

def glideto(coordinates, object):
    try:
        object.goto(coordinates)
    except:
        print("Uh oh! Your code can't be read. Make sure you wrote it right.")

def say(string, object):
    try:
        object.write(string, font=("Arial", 12, "normal"))
    except:
        print("Uh oh! Your code can't be read. Make sure you wrote it right.")

def wait(delay):
    try:
        clock.sleep(delay)
    except TypeError:
        print(f"Error: The delay value '{delay}' is invalid. Check that it's a number!")
    except:
        print("Uh oh! Your code can't be read. Make sure you wrote it right.")

def change_x(amount, object):
    try:
        object.setx(object.xcor() + amount)
    except:
        print("Error: Could not change X coordinate.")

def change_y(amount, object):
    try:
        object.sety(object.ycor() + amount)
    except:
        print("Error: Could not change Y coordinate.")

def bounce_on_edge(object):
    try:
        w = screen.window_width() / 2
        h = screen.window_height() / 2
        x, y = object.position()
        if abs(x) >= w or abs(y) >= h:
            object.setheading(object.heading() + 180)
    except:
        pass

def pen_down(object):
    object.pendown()

def pen_up(object):
    object.penup()

def set_pen_color(color, object):
    try:
        object.pencolor(color)
    except:
        print("Error: Invalid color name.")

def clear_all():
    clearscreen()

def hide(object):
    object.hideturtle()

def show(object):
    object.showturtle()

def change_size(amount, object):
    try:
        current_stretch = object.shapesize()[0]
        new_size = current_stretch + (amount / 10)
        object.shapesize(new_size, new_size)
    except:
        print("Error: Could not change size.")
