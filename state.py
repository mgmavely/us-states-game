from turtle import Turtle
FONT = ("Courier", 10, "normal")


class State(Turtle):

    def __init__(self, x, y, name):
        super().__init__()
        self.x = int(x)
        self.y = int(y)
        self.penup()
        self.hideturtle()
        self.name = name
        self.goto(self.x, self.y)

    def reveal(self):
        self.write(self.name, font=FONT)

    def match(self, text):
        return text == self.name
