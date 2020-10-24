import pygame as p

p.init()
w =(255,255,255)
size = (1000,600)
sc = p.display.set_mode(size)
p.display.set_caption("바운스볼")
playing = True
#공 이미지
ball=p.image.load("공.png")
bg=p.image.load("배경.png")
#발판
pan=p.image.load("발판.png")
p_rect=pan.get_rect(left=0,top=450)

b_rect=ball.get_rect(left=0,top=00)
b_y=0
b_x=0
clock=p.time.Clock()

while playing:
    clock.tick(50) #초당 100개 화면이 지나
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()
        if event.type==p.KEYDOWN:
            if event.key==p.K_LEFT:
                b_x=-5
            if event.key==p.K_RIGHT:
                b_x=5
        if event.type==p.KEYUP:
            if event.key==p.K_LEFT:
                b_x=0
            if event.key==p.K_RIGHT:
                b_x=0


    b_rect.left+=b_x       

    sc.fill(w)
    #배경
    sc.blit(bg,(0,0))
    sc.blit(ball,b_rect)
    sc.blit(pan,p_rect)
    
    b_rect.top+=b_y
    b_y+=1
    if b_rect.top>=570:
        b_y=-15

    #공 좌우 막아
    if b_rect.left<=0:
        b_rect.left=0
    if b_rect.left>=970:
        b_rect.left=970
        
    p.display.flip()
