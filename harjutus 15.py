import turtle

t = turtle.Turtle()
t.speed(3)

# Maja alus (ruut)
t.penup()
t.goto(-100, -100)
t.pendown()

for i in range(4):
    t.forward(200)
    t.left(90)

# Uks
t.penup()
t.goto(-30, -100)
t.pendown()
t.color("red")

t.forward(60)
t.left(90)
t.forward(80)
t.left(90)
t.forward(60)
t.left(90)
t.forward(80)

t.color("black")

# Katus (kolmnurk)
t.penup()
t.goto(-100, 100)
t.pendown()
t.color("green")

t.goto(0, 200)
t.goto(100, 100)
t.goto(-100, 100)

turtle.done()