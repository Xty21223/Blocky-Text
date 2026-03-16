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
    print("Uh oh! Your code can't be read. Make sure you wrote it right.\nHere are some solutions:\n- Check your object name\n- Check the coordinates. (They should look like this: (a, b) )")
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
