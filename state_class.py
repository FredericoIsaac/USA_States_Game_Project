from turtle import Turtle


class State(Turtle):

    def __init__(self, state_info):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(int(state_info.x.item()), int(state_info.y.item()))
        self.write(arg=state_info.state.item(), align="center", font=("Verdana", 8, "normal"))
