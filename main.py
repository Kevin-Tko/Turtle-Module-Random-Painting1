from turtle import Turtle, Screen
import random

my_turtle = Turtle()
my_turtle.speed('fast')
colors = ['lawn green', 'yellow', 'blue', 'dark goldenrod', 'teal', 'navy', 'medium violet red']


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        my_turtle.forward(50)
        my_turtle.right(angle)


for shape_sides in range(3, 11):
    my_turtle.color(random.choice(colors))
    draw_shape(shape_sides)

my_screen = Screen()
my_screen.exitonclick()
