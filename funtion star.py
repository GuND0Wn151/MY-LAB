import turtle
s=turtle.Turtle()
s.speed(0)
def star(turtle,size):
    if size<10:
        return
    for i in range(5):
        turtle.fd(size)
        star(turtle,size/3)
        turtle.left(144)
    turtle.end_fill()
star(s,250)

turtle.done()

