from turtle import Turtle

pos=[(0,0),(-20,0),(-40,0)]
distance = 20
up=90
down=270
left=180
right=0


class Snake:
   
    def __init__(self):
        self.new=[]
        self.create_snake()

    
    def create_snake(self):
        for position in pos:
            self.add_seg(position)
            

    def add_seg(self,position):
            tim=Turtle("square")
            tim.color("white")
            tim.penup()
            tim.goto(position)
            self.new.append(tim)  
            

    def extend(self):
        self.add_seg(self.new[-1].position())        
       

    def move(self): 
        for seg in range(len(self.new)-1,0,-1):
            new_x=self.new[seg-1].xcor()
            new_y=self.new[seg-1].ycor()
            self.new[seg].goto(x=new_x,y=new_y)
        self.new[0].forward(distance)       

    def up(self):
        if self.new[0].heading() != down:
            self.new[0].setheading(90)
    def down(self):
        if self.new[0].heading() != up:    
            self.new[0].setheading(270)
    def left(self):
        if self.new[0].heading() != right:   
            self.new[0].setheading(180)
    def right(self):
        if self.new[0].heading() != left:
            self.new[0].setheading(0)

    def reset(self):
        for seg in self.new:
            seg.goto(1000,1000)
        self.new.clear()
        self.create_snake()
        self.new[0]




