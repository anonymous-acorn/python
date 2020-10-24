import pygame as p
import random as r

p.init() # 파이썬게임 라이브러리 초기화

w=(255,255,255)
b=(0,0,0)
size=(740,340) #가로 세로

#이미지 불러오기
i=p.image.load("파인애플.png") #i 비행기 



#이미지------>좌표화
pl_rect = i.get_rect(left=0)#left=x top=y


bg=p.image.load("bg3.png")
#적군이미지 불러오기
en=p.image.load("01.png")
en_rect=en.get_rect(left=700,top=0)

bg1=bg.copy() #배경화면 복사

bg_rect=bg.get_rect(left=0)
bg1_rect=bg1.get_rect(left=800)

x=10
y=10
sc=p.display.set_mode(size) #해상도
#점수
font=p.font.SysFont('malgungothic',20)
font1=p.font.SysFont('malgungothic',50)
score=0

p.display.set_caption("파인애플의 모험!")

playing=True
#비행기 좌표
x=0
y=0
#비행기 부드럽게
pl_rect
#배경좌표
bg_x=0
bg1_x=800
#적군 좌표
en_x=700
en_y=0

bo = p.image.load("123.png") # 폭탄

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
    pl_rect.top+=y
    pl_rect.left+=x
    sc.fill(w) #배경화면 흰색으로
    sc.blit(bg,bg_rect) #이미지 업로드
    sc.blit(bg1,bg1_rect)
    bg_rect.left-=2#배경이동
    bg1_rect.left-=2#복사본 배경이동
    if bg_rect.left==-800:
        bg_rect.left=800
    if bg1_rect.left==-800:
        bg1_rect.left=800
    sc.blit(i,pl_rect) #이미지 업로드
    if pl_rect.top>= 240:
        y=0
    if pl_rect.top<= -5:
        y=0
    if pl_rect.left>= 657:
        x=0
    if pl_rect.left<= -5:
        x=0
    sc.blit(en,en_rect)#적군좌표
    en_rect.left-=8#적군 오른쪽 왼쪽 이동
    if en_rect.left<=-100:#만일닿으면
        en_rect.left=800
        en_rect.top=r.randint(5,260)
        score +=1
    text=font.render('score:{}'.format(score),True,(255,255,0))
    text1=font1.render('GAME OVER! score:{}'.format(score),True,(255,0,0))
    sc.blit(text,(650,0))

    if pl_rect.colliderect(en_rect):
        sc.blit(bo,pl_rect)
        playing=False
        sc.blit(text1,(80,160))
    p.display.flip()#화면 업데이트     
