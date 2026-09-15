from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Paddle()


screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")

is_game_on = True
while is_game_on:
    screen.update()










screen.exitonclick()