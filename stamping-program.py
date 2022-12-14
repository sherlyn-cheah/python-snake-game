# import Turtle Graphics module
import turtle


# define program constants
WIDTH = 500
HEIGHT = 500


# setup screen for drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Stamping")
screen.bgcolor("light pink")

# setup stamper
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("black")
stamper.shapesize(50/20) # provide pixel size, divide by 20
# make a stamp
stamper.stamp()
# command to not leave a mark while moving
stamper.penup()
# move location of stamp
stamper.goto(100, 100)
stamper.stamp()

# ending statement for all turtle programs
turtle.done()