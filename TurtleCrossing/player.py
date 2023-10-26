from turtle import Turtle
STARTING_POSITION = (0, -280) #a tuple
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# the turtle move forward 
class Player(Turtle):
    def __init__(self):
        super().__init__() # super()- call a method from the parent, super()-return an object of the superclass, here is Turtle 
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def go_up(self):
        self.forward(MOVE_DISTANCE)
        
    def is_at_finish_line(self): #return true if at the finish line:
        if self.ycor()> FINISH_LINE_Y:
            return True
        else:
            return False 
        
    def go_to_start(self):
        self.goto(STARTING_POSITION)
        
        

    
