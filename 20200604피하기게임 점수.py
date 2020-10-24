import pygame as p
import random as r

p.init() # 파이썬게임 라이브러리 초기화

w=(255,255,255)
b=(0,0,0)
size=(740,340) #가로 세로

#이미지 불러오기
i=p.image.load("파인애플.png")
bg=p.image.load("bg3.png")
#적군이미지 불러오기
en=p.image.load("01.png")
bg1=bg.copy() #배경화면 복사
x=10
y=10
sc=p.display.set_mode(size) #해상도
#점수
font=p.font.SysFont('malgungothic',20)
score=0

p.display.set_caption("파인애플의 모험!")

playing=True
#비행기 좌표
x=0
y=0
#비행기 부드럽게
y_c=0
x_c=0
#배경좌표
bg_x=0
bg1_x=800
#적군 좌표
en_x=700
en_y=0
while playing:

    for event in p.event.get(): #사용자가 뭘 누르는지 감지
        if event.type==p.QUIT:#게임창 x 버튼 누르면
            playing=False #계속 반복 종료
            p.quit() #게임 종료
            quit()
        if event.type==p.KEYUP:# 키보드 눌렀을때
                 if event.key==p.K_UP or event.key==p.K_DOWN:
                     y=0
                 if event.key==p.K_LEFT or event.key==p.K_RIGHT:
                     x=0
        if event.type==p.KEYDOWN:# 키보드 떼면
                 if event.key==p.K_UP:#위방향키 떼면
                     y=-6
                 if event.key==p.K_DOWN:#아래방향키 떼면
                     y=6
                 if event.key==p.K_LEFT:#왼쪽방향키 떼면
                     x=-6
                 if event.key==p.K_RIGHT:#오른쪽방향키 떼면
                     x=6
    y_c+=y
    x_c+=x
    sc.fill(w) #배경화면 흰색으로
    sc.blit(bg,(bg_x,0)) #이미지 업로드
    sc.blit(bg1,(bg1_x,0))
    bg_x-=2#배경이동
    bg1_x-=2#복사본 배경이동
    if bg_x==-800:
        bg_x=800
    if bg1_x==-800:
        bg1_x=800
    sc.blit(i,(x_c,y_c)) #이미지 업로드
    if y_c>= 240:
        y=0
    if y_c<= -5:
        y=0
    if x_c>= 657:
        x=0
    if x_c<= -5:
        x=0
    sc.blit(en,(en_x,en_y))#적군좌표
    en_x-=8#적군 오른쪽 왼쪽 이동
    if en_x<=-100:#만일닿으면
        en_x=800
        en_y=r.randint(5,260)
        score +=1
    text=font.render('점수:{}'.format(score),True,(255,255,0))
    sc.blit(text,(650,0))

    
    p.display.flip()#화면 업데이트     
