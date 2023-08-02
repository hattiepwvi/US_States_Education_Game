from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0

    def update(self, position, state_name):
        self.score += 1
        self.goto(position)
        self.write(f"{state_name}", align='center', font=('Arial', 12, 'normal'))
