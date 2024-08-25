import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("lightgreen")

# Set up the snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Set up the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Set up the pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Arial", 24, "normal"))

# Score
score = 0

# Segment list
segments = []

# Movement functions
def move_snake():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

# Change direction functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Game loop
def game_loop():
    screen.update()

    # Check for collisions with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        end_game()
        return
    
    # Check for collisions with the food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        
        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)
        
        # Increase the score
        global score
        score += 10
        pen.clear()
        pen.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

    move_snake()

    # Check for collisions with itself, skip the first few frames to avoid collision with the newly added segment
    for index, segment in enumerate(segments):
        if index > 1 and segment.distance(head) < 20:
            end_game()
            return

    # Call game_loop again after a delay
    screen.ontimer(game_loop, 100)

def end_game():
    pen.clear()
    pen.write("Game Over!", align="center", font=("Arial", 24, "normal"))
    screen.update()

# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Start the game
game_loop()
screen.mainloop()
