import pygame as p
p.init()#초기화
w=(255,255,255)#red,green,blue
size=(800,400)#가로 세로 화면 비율
sc=p.display.set_mode(size)
p.display.set_caption("게임판")
playing=True
ball=p.image.load("엔트리봇.png")
b_rect=ball.get_rect(left=0,top=100)
#공 위치 변수
b_y=0
#fps설정
clock=p.time.Clock()

while playing:
    clock.tick(50)
    for event in p.event.get():#사용자가 무엇을 눌렀는지
        if event.type==p.QUIT:#게임창 x버튼 누르면
            playing=False #계속 반복 종료
            p.quit()
            quit()

    sc.fill(w)
    sc.blit(ball,b_rect)
    b_rect.top+=b_y
    b_y+=0.5
    if b_rect.top>=250:
        b_y=-18
    p.display.flip()#화면 업데이트
