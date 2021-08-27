from turtle import Turtle, mode

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0,y=270)
        self.score=0
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.hideturtle()
        self.write(f"Score:{self.score} Highscore:{self.highscore}",move=False,align="center",font=("Arial",20,"normal"))

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} Highscore:{self.highscore}",move=False,align="center",font=("Arial",20,"normal"))
        
    
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open('data.txt',mode='w') as data:
                data.write(f"{self.highscore}" )
        self.score=0 
        self.update()       

    def inc_score(self):
        self.score+=1 
        self.update()
        
    # def game_over(self):
    #     self.goto(x=0,y=0)
    #     self.write("GAME OVER",move=False,align="center",font=("Arial",20,"normal"))

    
        
        