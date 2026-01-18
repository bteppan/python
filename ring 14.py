import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("white")


radius = 150
t.penup()
t.goto(0, -radius)
t.pendown()
t.circle(radius)


triangle_count = 60   
triangle_base = 20    
triangle_height = 30  


t.penup()
t.goto(0,0)
t.pendown()

for i in range(triangle_count):
    t.penup()
    t.forward(radius)
    t.pendown()

    
    
    t.left(90)
    t.forward(triangle_base)
    t.right(150)
    t.forward(triangle_height)
    t.right(60)
    t.forward(triangle_height)
    t.right(150)
    t.forward(triangle_base)
    

   
    t.penup()
    t.goto(0,0)
    t.pendown()

    
    t.right(360/triangle_count)

turtle.done()