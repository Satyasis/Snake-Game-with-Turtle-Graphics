from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Courier", 12, "normal")
GAME_OVER_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}  High Score:{self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    # def reset(self):
    #     if self.score > self.high_score:
    #         self.high_score = self.score
    #     self.score = 0
    #     self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over\nScore:{self.score}   High Score:{self.high_score}", align=ALIGNMENT, font=GAME_OVER_FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    
        
