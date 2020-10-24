import turtle as t
import random as r

#악당거북이
te=t.Turtle()
te.shape("turtle")
te.color("black")
te.speed(0)
te.up()
te.goto(0,200)
#먹이
ts=t.Turtle()
ts.shape("circle")
ts.color("cyan")
ts.speed(0)
ts.up()
ts.goto(0,-200)

def turn_right():
    t.setheading(0)
def turn_left():
    t.setheading(180)
def turn_up():
    t.setheading(90)
def turn_down():
    t.setheading(270)
def play():
    t.forward(10)
    ang=te.towards(t.pos()) #.pos-내 거북이 위치
    te.setheading(ang)
    te.forward(7)
    if t.distance(ts)<12:
        x=r.randint(-230,230)
        y=r.randint(-230,230)
        ts.goto(x,y)
    if t.distance(te)>=12:
        t.ontimer(play,100)

        
        
        
#내 거북이
t.setup(500,500)
t.bgcolor("blue")
t.shape("turtle")
t.speed(0)
t.up()
t.color("yellowgreen")

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()
play()



