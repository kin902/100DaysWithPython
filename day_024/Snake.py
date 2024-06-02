from turtle import Turtle

start_position = [(0.0, 0.0), (-20.0, 0.0), (-40.0, 0.0)]
Up = 90
Down = 270
Left = 180
Right = 0


class Snake:
    def __init__(self):
        # A list that contain all the snake's segments
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Create a snake with 3 segments in the position
        for position in start_position:
            segment = (Turtle("square"))
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self, speed):
        # Move the segments to the previous segments
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
            self.segments[seg].showturtle()
        self.head.forward(speed)

    def more_segments(self):
        segment = (Turtle("square"))
        segment.hideturtle()
        segment.penup()
        self.segments.append(segment)

    def reset_game(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

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
