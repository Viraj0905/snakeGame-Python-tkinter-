from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(height=600, width=600)
screen.tracer(0)

start_position = [(0, 0), (-20, 0), (-40, 0)]
tails = []
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect collition of food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    #Detect collition with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # is_game_on = False
        # score.game_over()
        score.reset()
        snake.reset()
    #Detect collition with tail
    for segment in snake.tails[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # is_game_on = False
            # score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()
