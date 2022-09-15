from turtle import Turtle
ALIGNMENT = "Left"
FONT = "Arial"


class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.score = 0
      self.color("white")
      self.penup()
      self.goto(-40,270)
      self.hideturtle()
      self.write(arg=f"Your score: {self.score}",move=False, align= ALIGNMENT,font=(FONT,8,"normal"))

   def update_scoreboard(self):
      self.write(arg=f"Your score: {self.score}", move=False, align=ALIGNMENT, font=(FONT, 8, "normal"))

   def increase_score(self):
      self.score+=1
      self.clear()
      self.update_scoreboard()

   def game_over(self):
      self.goto(0,0)
      self.color("red")
      self.write(arg="GAME OVER", move=False, align="center", font=(FONT, 25, "bold"))