from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.new_score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreBoard()

    def update_scoreBoard(self):
        self.clear()
        self.write(f"Score:  {self.new_score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.new_score > self.high_score:
            self.high_score = self.new_score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        self.new_score = 0
        self.update_scoreBoard()

    def increase_score(self):
        self.new_score += 1
        self.update_scoreBoard()
