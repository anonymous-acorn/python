import turtle as t
import random as r
t.shape("turtle")

                     #UP키를 눌렀을 때 호출되는 함수 선언
def turn_up():       #거북이 방향을 왼쪽으로 2도 회전
    t.left(2)
def turn_down():
    t.right(2)
def fire():
    ang=t.heading()
    while t.ycor()>0:
        t.forward(15)
        t.right(5)
    d=t.distance(target,0)#터틀과 타겟과의 거리
    t.color("red")
    
    t.sety(r.randint(100,200)) #성공 또는 실패를 표시할 위치
    if d<25:
        t.color("black")
            t.write("G00D!",False,"center",("",50))
        else:
        t.color("red")
        t.write("BAD!",False,"center",("",50))

    t.color("black")
    t.goto(-200,10)
    t.setheading(ang)

#땅을 그리는 부분
t.goto(-300,0)
t.down()
t.goto(300,0)

#목표지점을 그리는 부분
target=r.randint(50,150)#목표지점을 랜덤으로 설정
t.pensize(3)
t.color("green")
t.up()
t.goto(target-25,2)
t.down()
t.goto(target+25,2)

#거북이를 검은색으로 바꾸고 발사지점으로 이동
t.color("black")
t.up()
t.goto(-200,10)
t.setheading(20)

#거북이가 동작하는데 필요한 설정
t.onkeypress(turn_up,"Left")
t.onkeypress(turn_down,"Right")
t.onkeypress(fire,"space")

t.listen()

