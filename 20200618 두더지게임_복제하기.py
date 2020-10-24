import pygame as p
import random as r
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(800,400)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True
ml=p.image.load("두더지.png")
ml_list=[]
for x in range(10):
    ml_rect=ml.get_rect(left=r.randint(0,700),top=r.randint(0,300))
    ml_list.append(ml_rect)
while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()

    sc.fill(w)
    for ml_rect in ml_list:
        sc.blit(ml,ml_rect)
        
    p.display.flip()#화면 업데이트
