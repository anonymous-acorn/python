#터틀런 2 ㅅ ㅐ 로 운 ㄱ ㅓ 점 수 ㄱ ㄱ ㅏ ㅈ ㅣ ㄴ ㅏ 오 는 ㄱ ㅓ
import turtle as t
import random

score=0  #점수 저장 변수
playing=False  #현재 게임 플레이하고있는지 확인

#적거북이
te=t.Turtle() #새 거북이 생성코드
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

def message(m1,m2):
    t.clear()
    t.goto(0,100)
    t.write(m1,False,"center",("",15))
    t.goto(0,-100)
    t.write(m2,False,"center",("",20))
    t.home()   #내 거북이 처음 스폰 위치로 돌아감

def start():
    global playing
    if playing==False:
            playing=True
            t.clear()
            play()

def play():
    global score
    global playing
    t.forward(10) # 내 거북이 속도
    te.forward(8)# 적 거북이 속도
    ang=te.towards (t.pos()) #t.pos-내 거북이 방향
    te.setheading(ang)
    if t.distance(te)<12:# 내 거북이랑 적과의 거리가 12보다 작으면
        text="Score:"+str(score) #str-문자열
        message("Game Over[press Space Bar to play game one more]",text)
        playing=False
        score=0
    if t.distance(ts)<12:
        score=score+1
        t.write(score)
        x=random.randint(-230,230)
        y=random.randint(-230,230)
        ts.goto(x,y)
    if playing:
        t.ontimer(play,100)

def fire():
    t.forward(150)
#내 자신 거북이

t.title("Turtle Run 2") # 윈도우 창 이름
t.bgcolor("green")
t.setup(500,500)    
t.shape("turtle")
t.speed(0)
t.up()
t.color("black")

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.onkeypress(start,"space")
t.onkeypress(fire,"v")
t.listen() #onkeypress사용하려면 listen()꼭 써야함.
message("Turtle Run 2","[press Space Bar to start a game]")
t.color("yellowgreen")


