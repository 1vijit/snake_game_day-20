from turtle import Turtle
ALIGNMENT = "Left"
FONT = "Arial"



class Scoreboard(Turtle):
   def __init__(self):
      super().__init__()
      self.score = 0
      self.color("white")
      self.penup()
      with open("data.txt", mode="r") as file :
         contents= file.read()
         self.high_score = int(contents)
      self.goto(-40,270)
      self.hideturtle()
      self.write(arg=f"Your score: {self.score}",move=False, align= ALIGNMENT,font=(FONT,8,"normal"))
      self.update_scoreboard()


   def update_scoreboard(self):
      self.clear()
      self.write(arg=f"Your score: {self.score}  High score: {self.high_score}", move=False, align=ALIGNMENT, font=(FONT, 8, "normal"))

   def increase_score(self):
      self.score+=1
      self.clear()
      self.update_scoreboard()

   # def game_over(self):
   #    self.goto(0,0)
   #    self.color("red")
   #    self.write(arg="GAME OVER", move=False, align="center", font=(FONT, 25, "bold"))

   def reset(self):
      if self.high_score < self.score:
         self.high_score = self.score
      self.score = 0
      self.update_scoreboard()
      with open("data.txt", mode="w") as file :
         file.write(str(self.high_score))