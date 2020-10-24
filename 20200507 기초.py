import pygame as p

p.init() #pygame 라이브러리 초기화

#빛의 3원색 RedGreenBlue
Black=(0,0,0)
White=(255,255,255)
Red=(255,0,0)
Blue=(0,0,255)
Green=(0,255,0)
Poop=[0,153,153]
#해상도
size=[500,500]
screen=p.display.set_mode(size)

#창제목
p.display.set_caption("Game Title")


done=False
clock=p.time.Clock() #FPS=초당 프레임

while not done:

    clock.tick(10) #1초에 10번 사진을 찍는다
    for event in p.event.get(): #우리가 누르는 버튼 체크
        if event.type==p.QUIT: #만일 창옆에 x버튼을 누르면
            done=True #계속 반복

    

        
    screen.fill(Poop) #배경화면 색깔

    p.draw.rect(screen,Black,[360,360,50,50],2) #사각형
    p.draw.polygon(screen,White,[[30,150],[125,100],[220,150]],2) #이등변삼각형
    

    p.display.flip() #화면 업데이트
