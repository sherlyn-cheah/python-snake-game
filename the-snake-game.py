# import Turtle Graphics module
import turtle
# import random module for generating food randomly
import random

# define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 200
FOOD_SIZE = 10

offsets = {
    "up":(0, 20),
    "down":(0, -20),
    "left":(-20, 0),
    "right":(20, 0),
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")

def set_snake_direction(direction):
    global snake_direction
    if snake_direction == "pause":
        snake_direction = "pause"
    elif direction == "up":
        if snake_direction != "down":
            snake_direction = "up"
    elif direction == "right":
        if snake_direction != "left":
            snake_direction = "right"
    elif direction == "down":
        if snake_direction != "up":
            snake_direction = "down"
    elif direction == "left":
        if snake_direction != "right":
            snake_direction = "left"

def pause():
    global snake_direction, prev_snake_direction
    prev_snake_direction = snake_direction
    snake_direction = "pause"

def resume():
    global snake_direction, prev_snake_direction
    snake_direction = prev_snake_direction
    screen.title(f'Snake Game | Score: {score}')
    game_loop()

def new_game():
    global snake, snake_direction, prev_snake_direction, score
    snake = [[0,0],[20,0],[40,0],[60,0]]
    snake_direction = "right" # default direction
    prev_snake_direction = ""
    score = 0
    screen.title("Snake Game")
    game_loop()

def exit_game():
    turtle.bye()

# function for snake movement/game loop
def game_loop():

    if snake_direction == "pause":
        screen.title("Game paused. Press Enter to resume.")
    else:
        # create new head for snake (taking existing head and copy)
        new_head = snake[-1].copy()
        
        # change snake direction based on offsets
        new_head[0] += offsets[snake_direction][0] # x-coordinate
        new_head[1] += offsets[snake_direction][1] # y-coordinate

        # check for collisions (body and walls)
        
        if new_head in snake or new_head[0] < -(WIDTH/2) or new_head[0] > WIDTH/2 \
            or new_head[1] < -(HEIGHT/2) or new_head[1] > WIDTH/2:
            screen.title(f'Your snake has died! Final Score: {score} | N for new game | Esc to exit')
        else:
            # clears previous stamps of snake
            stamper.clearstamps() 

            # add new head to snake body
            snake.append(new_head)

            # check for food collision
            if not food_collision():
                # if no food collision, remove tail of snake
                snake.pop(0)

            # draw snake
            for segment in snake:
                stamper.goto(segment[0], segment[1])
                stamper.stamp()

            # refresh screen
            screen.title(f'Snake Game | Score: {score}')
            screen.update()

            # rinse and repeat
            turtle.ontimer(game_loop, DELAY)

def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(- WIDTH/2 + FOOD_SIZE, WIDTH/2 - FOOD_SIZE)
    y = random.randint(- HEIGHT/2 + FOOD_SIZE, HEIGHT/2 - FOOD_SIZE)
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5 # pythagoras' theorem
    return distance

# setup screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgcolor("blue")
screen.tracer(0)  # disables automatic animation

# event handlers
screen.listen()
bind_direction_keys()
screen.onkey(pause, "space")
screen.onkey(resume, "Return")
screen.onkey(new_game, "n")
screen.onkey(exit_game, "Escape")

# setup stamper
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("yellow")
stamper.penup() # to not leave marks as the snake moves

# create snake representation as a list of lists
snake = [[0,0],[20,0],[40,0],[60,0]]
snake_direction = "right" # default direction
prev_snake_direction = "" # to store direction for pause & resume
score = 0 # to store game score

# draw snake for the first time
for segment in snake:
    stamper.goto(segment[0], segment[1])
    stamper.stamp()

# food
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOOD_SIZE/20)
food.penup()
food_pos = get_random_food_pos()
food.goto(food_pos)
food.color("white")

# initial call of function to move snake
game_loop()

# ending statement
turtle.done()
