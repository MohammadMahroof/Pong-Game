from turtle import Turtle
UP_LIMIT = 225
DOWN_LIMIT = -225

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < UP_LIMIT:   
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > DOWN_LIMIT:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)



