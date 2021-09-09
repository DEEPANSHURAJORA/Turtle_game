from turtle import Turtle




class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.color("white")
            self.level = 1
            self.hideturtle()
            self.penup()
            self.goto(-250,220)
            self.update()
        def update(self):
            self.clear()
            self.write(f" level:{self.level}", align="left", font=("Courier", 20, "normal"))
        def increase_level(self):
            self.level +=1
            self.update()
        def game_over(self):
            self.goto(0,0)
            self.color("red")
            self.write(f"GAME OVER",align= "center",font= ("Courier", 44, "bold"))
