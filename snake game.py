import turtle
import time
import random
delay=0.1
#screen
s = turtle.Screen()
s.title("game")
s.bgcolor("green")
s.setup(width=600, height=500)
s.tracer(0)
#snake head
p=turtle.Turtle()
p.speed(0)
p.shape("square")
p.color("black")
p.penup()
p.goto(0,0)
p.direction="stop"
#funtions
def up():
    if p.direction != "down":
        p.direction="up"
def down():
    if p.direction != "up":
        p.direction="down"
def left():
    if p.direction != "left":
        p.direction="left"
def right():
    if p.direction != "right":
        p.direction="right"

def move():
    if p.direction == "up":
        y = p.ycor()
        p.sety(y+20)
    if p.direction == "down":
        y = p.ycor()
        p.sety(y-20)
    if p.direction == "left":
        x = p.xcor()
        p.setx(x-20)
    if p.direction == "right":
        x = p.xcor()
        p.setx(x+20)
#food
f=turtle.Turtle()
f.speed(0)
f.shape("circle")
f.color("red")
f.penup()
f.goto(0,100)

segments=[]


#keybaord
s.listen()
s.onkey(up,"w")
s.onkey(down,"s")
s.onkey(right,"d")
s.onkey(left,"a")
#main loop
while True: 
    s.update()
    #border
    if p.xcor()>290 or p.xcor()<-290 or p.ycor()>290 or p.ycor()<-290:
        time.sleep(1)
        p.goto(0,0)
        p.direction="stop"
        for segment in segments:
            segment.goto(1000,1000)
        segments=[]
    #segments
    if p.distance(f) < 20:
        f.goto(x=random.randint(-290,270),y=random.randint(-290,290))
        #body
        segment=turtle.Turtle()
        segment.color("white")
        segment.penup()
        segment.speed(0)
        segment.shape("square")
        segments.append(segment)
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    if len(segments)>0:
        x=p.xcor()
        y=p.ycor()
        segments[0].goto(x,y)

   
   
   
    move()
    for segment in segments:
        if segment.distance(p) < 20:
            time.sleep(1)
            p.goto(0,0)
            p.direction="stop"
            for segment in segments:
                segment.goto(1000,1000)
            segments=[]

           
    time.sleep(delay)
#s.mainloop()