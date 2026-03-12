import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.width(2)

raadius = 150
hammaste_arv = 24
hamba_korgus = 30

nurk = 360 / 24

t.penup()
t.goto(0, -raadius)
t.setheading(0)
t.pendown()

t.circle(raadius)

for i in range(7):
    t.penup()
    t.goto(0, 0)
    t.setheading(nurk * i)
    t.forward(raadius)
    t.pendown()

t.left(90)
t.forward(20)
t.right(135)
t.forward(20* 1.4)
t.right(90)
t.forward(20 * 1.4)
t.right(135)
t.forward(20)

turtle.done()