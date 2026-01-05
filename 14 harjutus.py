import turtle
import math

# Seadista ekraan
screen = turtle.Screen()
screen.bgcolor("white")

# Loo kilpkonn
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")

# Joonista keskne ring
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.circle(100)

# Funktsioon kolmnurga joonistamiseks
def draw_triangle(x, y, angle, size):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.pendown()
    for _ in range(3):
        pen.forward(size)
        pen.left(120)

# Joonista kolmnurgad ringi ümber
triangle_count = 60
radius = 100
triangle_size = 30

for i in range(triangle_count):
    angle = i * (360 / triangle_count)
    x = radius * math.cos(math.radians(angle))
    y = radius * math.sin(math.radians(angle))
    draw_triangle(x, y, angle, triangle_size)

# Lõpeta
turtle.done()
