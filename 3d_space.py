
#created by GuND0Wn151
import turtle
s = turtle.Turtle()
s.color("red")
s.speed(0)
s.goto(0,0)
s.fd(500)
s.goto(0,0)
s.bk(500)
s.goto(0,0)
s.left(90)
s.fd(500)
s.goto(0,0)
s.bk(500)


#y ot x
for i in range(0,500,25):
    s.penup()
    s.goto(0,0)
    s.pendown()
    s.goto(0,i)
    s.goto(500-i,0)
#-y to -x
for i in range(0,500,25):
    s.penup()
    s.goto(0,0)
    s.pendown()
    s.goto(0,-i)
    s.goto(-(500-i),0)
#x to -y
for i in range(0,500,25):
    s.penup()
    s.goto(0,0)
    s.pendown()
    s.goto(i,0)
    s.goto(0,-(500-i))

for i in range(0,500,25):
    s.penup()
    s.goto(0,0)
    s.pendown()
    s.goto(0,i)
    s.goto(-(500-i),0)





turtle.done()
