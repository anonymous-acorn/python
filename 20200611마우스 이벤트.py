import pygame as p
import random as r

p.init()#초기화
w=(255,255,255)#red,green,blue
size=(800,400)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("클릭해서 돈을 벌어라!")

m_image=p.image.load("돈.png")
m_rect=m_image.get_rect(left=r.randint(0,700),top=r.randint(0,300))

font=p.font.SysFont('malgungothic',20)
money=0

playing=True


while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()

        if event.type==p.MOUSEBUTTONDOWN:
            if m_rect.collidepoint(event.pos[0],event.pos[1]):
                m_rect.left=r.randint(0,700)
                m_rect.top=r.randint(0,300)
                money+=100
                
        if event.type==p.MOUSEBUTTONUP:
            print("마우스 버튼 업")


    sc.fill(w)#배경색
    sc.blit(m_image,m_rect)
    text=font.render('돈:{}원'.format(money),True,(0,0,0))
    sc.blit(text,(300,0))
    
    p.display.flip()#화면 업데이트
