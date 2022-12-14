## LinkedIn Learning - Building the Classic Snake Game with Python

## Create starter template for snake game
# import Turtle Graphics module
import turtle


# define program constants
WIDTH = 500
HEIGHT = 500


# setup screen for drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Starter template - drawing a star")
screen.bgcolor("light pink")

# setup turtle
my_turtle = turtle.Turtle()
my_turtle.shape("arrow")
my_turtle.color("black")

# commands for turtle to draw a star
my_turtle.forward(100)
my_turtle.right(144)
my_turtle.forward(100)
my_turtle.left(72)
my_turtle.forward(100)
my_turtle.right(144)
my_turtle.forward(100)
my_turtle.left(72)
my_turtle.forward(100)
my_turtle.right(144)
my_turtle.forward(100)
my_turtle.left(72)
my_turtle.forward(100)
my_turtle.right(144)
my_turtle.forward(100)
my_turtle.left(72)
my_turtle.forward(100)
my_turtle.right(144)
my_turtle.forward(100)

# ending statement for all turtle programs
turtle.done()