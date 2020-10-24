import pygame as p
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(600,800)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True
#비행기
p_image=p.image.load("plane.png")
p_rect=p_image.get_rect(left=250,top=700)
x=0
y=0
#배경
bg=p.image.load("universe.png")
#미사일
bullet=p.image.load("bullet.png")
b_list=[]


while playing:
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()
        if event.type==p.KEYDOWN:
            if event.key==p.K_UP:
                y=-15
        
            if event.key==p.K_DOWN:
                y=15
        
            if event.key==p.K_RIGHT:
                x=15
        
            if event.key==p.K_LEFT:
                x=-15
            if event.key==p.K_SPACE:
                b_rect=bullet.get_rect(left=p_rect.left+36,top=p_rect.top)
                b_list.append(b_rect)

        if event.type==p.KEYUP:
            if event.key==p.K_UP:
                y=0
        
            if event.key==p.K_DOWN:
                y=0
        
            if event.key==p.K_RIGHT:
                x=0
        
            if event.key==p.K_LEFT:
                x=0

    p_rect.left+=x#+= --> p_rect.left=p_rect.left+x
    p_rect.top+=y

    sc.fill(w)
    sc.blit(bg,(0,0))
    for b_rect in b_list:
        sc.blit(bullet,b_rect)
    for b_rect in b_list:
        b_rect.top-=20
        if b_rect.top<=0:
            b_list.remove(b_rect)
        
    sc.blit(p_image,p_rect)
    p.display.flip()#화면 업데이트
