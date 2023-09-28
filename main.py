from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake game")

segment = []

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect Collision with wall
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        game_is_on = False
        score.game_over()
    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
