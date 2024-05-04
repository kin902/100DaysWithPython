from turtle import Turtle, Screen
start_position = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]
Up = 90
Down = 270
Left = 180
Right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in start_position:
            segment = (Turtle("square"))
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self, speed):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(speed)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)
