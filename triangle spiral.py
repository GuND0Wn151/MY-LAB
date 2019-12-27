import turtle
t=turtle.Turtle()
t.color("red")
t.speed(0)


d=0
for i in range(0,1000):
    t.fd(d)
    t.left(120.5)
    d+=2

turtle.done()