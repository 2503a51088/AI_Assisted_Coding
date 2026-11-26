"""
Snake Game

This module contains a simple keyboard-controlled Snake game built with
Python's standard-library turtle graphics module.
"""

import random
import turtle


GRID_SIZE = 20
WINDOW_SIZE = 600


def move_up():
    """Change the snake's direction upward."""
    if snake.direction != "down":
        snake.direction = "up"


def move_down():
    """Change the snake's direction downward."""
    if snake.direction != "up":
        snake.direction = "down"


def move_left():
    """Change the snake's direction to the left."""
    if snake.direction != "right":
        snake.direction = "left"


def move_right():
    """Change the snake's direction to the right."""
    if snake.direction != "left":
        snake.direction = "right"


def create_segment(color="green"):
    """Create and return a new square-shaped snake segment."""
    segment = turtle.Turtle()
    segment.shape("square")
    segment.color(color)
    segment.penup()
    return segment


def move_snake():
    """Move the snake, handle collisions, and schedule the next update."""
    head_x = snake.segments[0].xcor()
    head_y = snake.segments[0].ycor()

    directions = {
        "up": (head_x, head_y + GRID_SIZE),
        "down": (head_x, head_y - GRID_SIZE),
        "left": (head_x - GRID_SIZE, head_y),
        "right": (head_x + GRID_SIZE, head_y)
    }
    new_x, new_y = directions[snake.direction]

    for index in range(len(snake.segments) - 1, 0, -1):
        previous_x = snake.segments[index - 1].xcor()
        previous_y = snake.segments[index - 1].ycor()
        snake.segments[index].goto(previous_x, previous_y)

    snake.segments[0].goto(new_x, new_y)

    if snake.segments[0].distance(snake.food) < GRID_SIZE:
        snake.segments.append(create_segment())
        snake.score += 1
        snake.score_display.clear()
        snake.score_display.write(
            f"Score: {snake.score}",
            align="center",
            font=("Arial", 16, "normal")
        )
        move_food()

    boundary = WINDOW_SIZE // 2 - GRID_SIZE
    outside_boundary = (
        new_x > boundary or new_x < -boundary
        or new_y > boundary or new_y < -boundary
    )
    hit_body = any(
        snake.segments[0].distance(segment) < GRID_SIZE
        for segment in snake.segments[1:]
    )

    if outside_boundary or hit_body:
        snake.score_display.goto(0, 0)
        snake.score_display.write(
            "Game Over! Press Escape to quit.",
            align="center",
            font=("Arial", 18, "normal")
        )
        snake.game_running = False
        return

    snake.window.update()
    turtle.ontimer(move_snake, 150)


def move_food():
    """Place the food at a random position aligned with the game grid."""
    limit = (WINDOW_SIZE // 2 - GRID_SIZE) // GRID_SIZE
    x = random.randint(-limit, limit) * GRID_SIZE
    y = random.randint(-limit, limit) * GRID_SIZE
    snake.food.goto(x, y)


def start_game():
    """Start the Snake game and configure keyboard controls."""
    window = turtle.Screen()
    window.title("Snake Game")
    window.bgcolor("black")
    window.setup(width=WINDOW_SIZE, height=WINDOW_SIZE)
    window.tracer(0)

    snake.score = 0
    snake.direction = "right"
    snake.game_running = True
    snake.segments = [create_segment()]
    snake.segments[0].goto(0, 0)

    snake.food = create_segment("red")
    move_food()

    snake.score_display = turtle.Turtle()
    snake.score_display.hideturtle()
    snake.score_display.color("white")
    snake.score_display.penup()
    snake.score_display.goto(0, WINDOW_SIZE // 2 - 40)
    snake.score_display.write(
        "Score: 0",
        align="center",
        font=("Arial", 16, "normal")
    )

    window.listen()
    window.onkey(move_up, "Up")
    window.onkey(move_down, "Down")
    window.onkey(move_left, "Left")
    window.onkey(move_right, "Right")
    window.onkey(window.bye, "Escape")

    snake.window = window
    move_snake()
    window.mainloop()


class SnakeState:
    """Store the current state and graphical objects for the game."""

    def __init__(self):
        self.score = 0
        self.direction = "right"
        self.game_running = True
        self.segments = []
        self.food = None
        self.score_display = None


snake = SnakeState()


if __name__ == "__main__":
    start_game()
