from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.tails = []
        self.create_snake()
        self.head = self.tails[0]

    def create_snake(self):
        """ Creating intial Snake..."""
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self,position):
        tail = Turtle(shape="square")
        tail.color("white")
        tail.penup()
        tail.goto(position)
        self.tails.append(tail)
    def reset(self):
        for seg in self.tails:
            seg.goto(1000, 1000)
        self.tails.clear()
        self.create_snake()
        self.head = self.tails[0]
    def extend(self):
        #add new segment to the snake in my code adding new tail
        self.add_segment(self.tails[-1].position())
    def move(self):
        for position in range(len(self.tails)-1, 0, -1):
            new_x = self.tails[position-1].xcor()
            new_y = self.tails[position-1].ycor()
            self.tails[position].goto(new_x, new_y)
        self.tails[0].forward(MOVE_DISTANCE)
#if face to left then up=left,right=down

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

