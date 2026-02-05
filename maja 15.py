import turtle

t = turtle.Turtle()
t.speed(0)


t.penup()
t.goto(-50, -50)
t.pendown()
t.color("black")

for _ in range(4):
    t.forward(100)
    t.left(90)



t.penup()
t.goto(-50, 50)
t.pendown()
t.color("green")
t.goto(0, 100)
t.goto(50, 50)
t.goto(-50, 50)
t.end_fill()

# Punane ruut (uks)
t.penup()
t.goto(-20, -50)
t.pendown()
t.color("red")

for _ in range(4):
    t.forward(40)
    t.left(90)

turtle.done()