from turtle import Turtle
STARTING_POSITION = [(0,  0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        # new_segment.shapesize(stretch_len=1, stretch_wid=1) # shape and size of the turtle
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to thr snake
        self.add_segment(self.segments[-1].position())   # pass the position of the snake's last segment to the add_segment() function

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()     # store co-ordinates of front segment
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)     # going to the front segment coordinates
        self.head.forward(MOVE_DISTANCE)
        # self.segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)   # same as self.head.left(90)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)