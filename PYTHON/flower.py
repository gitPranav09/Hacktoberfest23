import turtle

wn = turtle.Screen()
wn.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)  

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

def draw_petal(radius, color):
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius, 60)
    pen.left(120)
    pen.circle(radius, 60)
    pen.end_fill()

pen.penup()
pen.goto(0, -200)
pen.pendown()

for _ in range(36):
    draw_petal(100, colors[_ % 6])
    pen.right(10)

wn.exitonclick()
