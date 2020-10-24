import pygame as p

p.init() # 파이썬게임 라이브러리 초기화

w=(255,255,255)
b=(0,0,0)
size=(400,400) #가로 세로

#이미지 불러오기
i=p.image.load("브롤 레온.png")
bg=p.image.load("1.jpg")
x=100
y=100
sc=p.display.set_mode(size) #해상도

p.display.set_caption("키보드 컨트롤")

playing=True

while playing:

    for event in p.event.get(): #사용자가 뭘 누르는지 감지
        if event.type==p.QUIT:#게임창 x 버튼 누르면
            playing=False #계속 반복 종료
            p.quit() #게임 종료
            quit()
        if event.type==p.KEYUP:# 키보드 눌렀을때
                 if event.key==p.K_UP:#위방향키 누르면
                     print("니 손 더러워 손 떼!")
                     y=y-1
                 if event.key==p.K_DOWN:#아래방향키 누르면
                     print("니 손 더러워 손 떼!")
                     y=y+1
                 if event.key==p.K_LEFT:#왼쪽향키 누르면
                     print("니 손 더러워 손 떼!")
                     x=x-1
                 if event.key==p.K_RIGHT:#오른쪽방향키 누르면
                     print("니 손 더러워 손 떼!")
                     x=x+1

        if event.type==p.KEYDOWN:# 키보드 떼면
                 if event.key==p.K_UP:#위방향키 떼면
                     print("니 손 떼지마")
                 if event.key==p.K_DOWN:#아래방향키 떼면
                     print("니 손 떼지마")
                 if event.key==p.K_LEFT:#왼쪽방향키 떼면
                     print("니 손 떼지마")
                 if event.key==p.K_RIGHT:#오른쪽방향키 떼면
                     print("니 손 떼지마")
    sc.fill(w) #배경화면 흰색으로
    p.draw.circle(sc,b,(x,y),40) #x좌표,y좌표,반지름,선굵기
    p.display.flip()#화면 업데이트     
