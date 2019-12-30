#created by GuND0Wn151
import turtle
t=turtle.Turtle()
t.speed(0)
d=p=0
while d!=50:
    t.penup()
    t.goto(0,0)
    t.left(p)
    t.fd(50)
    t.pendown()
    t.left(90)
    t.fd(50)
    for i in range(3):
        t.left(90)
        t.fd(100)

    t.left(90)
    t.fd(50)
    
    
    
    
    p+=2
    d+=1 
turtle.done()
