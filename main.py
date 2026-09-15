from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((-350, 0))
l_paddle = Paddle((350, 0))


screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    screen.update()










screen.exitonclick()