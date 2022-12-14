# import Turtle Graphics module
import turtle


# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 20 # milliseconds between screen updates

# creating a function for animation
def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY) # function will keep looping once called

# setup screen for drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Circle animation")
screen.bgcolor("light pink")
# adding this turns off the automatic animation
screen.tracer(0)

# setup turtle
my_turtle = turtle.Turtle()
my_turtle.shape("arrow")
my_turtle.color("black")

# set animation
move_turtle()

# ending statement for all turtle programs
turtle.done()