#Imports
import pygame as pyg
import math
from sys import exit as syexit

pyg.init()

#Globals
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
BG_COLOR=(40,40,40)
SIZE=30
SCREEN = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pyg.font.Font("freesansbold.ttf", 20)

#Main
def get_t_cords(p1,p2,t):
    x1,y1=p1.center
    x2,y2=p2.center

    dist=math.sqrt((x2-x1)**2 + (y2-y1)**2)
    if dist==0:
        dist=1
    dt=t/100*dist
    ratio=dt/dist
    xt=(1-ratio)*x1 + ratio*x2
    yt=(1-ratio)*y1 + ratio*y2
    return (int(xt),int(yt))
def get_tpoint_curve(p1,p2,p3,p4,t,DRAW=False):
    d1=pyg.rect.Rect(get_t_cords(p1,p2,t)[0], get_t_cords(p1,p2,t)[1],1,1)
    d2=pyg.rect.Rect(get_t_cords(p2,p3,t)[0], get_t_cords(p2,p3,t)[1],1,1)
    d3=pyg.rect.Rect(get_t_cords(p3,p4,t)[0], get_t_cords(p3,p4,t)[1],1,1)
    I1=pyg.rect.Rect(get_t_cords(d1,d2,t)[0], get_t_cords(d1,d2,t)[1],1,1)
    I2=pyg.rect.Rect(get_t_cords(d2,d3,t)[0], get_t_cords(d2,d3,t)[1],1,1)

    if DRAW:
        pyg.draw.line(SCREEN, (90, 90, 90), p1.center, p2.center, 6)
        pyg.draw.line(SCREEN, (90, 90, 90), p2.center, p3.center, 6)
        pyg.draw.line(SCREEN, (90, 90, 90), p3.center, p4.center, 6)
        pyg.draw.line(SCREEN, (120, 120, 120), (d1.x,d1.y), (d2.x,d2.y), 4)
        pyg.draw.line(SCREEN, (120, 120, 120), (d2.x,d2.y), (d3.x,d3.y), 4)
        pyg.draw.line(SCREEN, (150, 150, 150), (I1.x,I1.y), (I2.x,I2.y), 4)
        pyg.draw.circle(SCREEN, (0,0,0), (d1.x,d1.y), int(SIZE/2))
        pyg.draw.circle(SCREEN, (0,0,0), (d2.x,d2.y), int(SIZE/2))
        pyg.draw.circle(SCREEN, (0,0,0), (d3.x,d3.y), int(SIZE/2))
        pyg.draw.circle(SCREEN, (128,0,128),(I1.x,I1.y), int(SIZE/3))
        pyg.draw.circle(SCREEN, (128,0,128), (I2.x,I2.y), int(SIZE/3))
        pyg.draw.circle(SCREEN, (255,255,255), get_t_cords(I1,I2,t), int(SIZE/4))
    return get_t_cords(I1,I2,t)
def get_complete(p1,p2,p3,p4):
    t=0
    cords=[]
    while t<=100:
        t+=0.1
        cords.append(get_tpoint_curve(p1,p2,p3,p4,t))
    return cords
def main(drawing=False):
    clock = pyg.time.Clock()

    DRAW=drawing
    T=0
    DRAG1,DRAG2,DRAG3,DRAG4=False,False,False,False
    P1=pyg.rect.Rect(int(SCREEN_WIDTH/4), int(SCREEN_HEIGHT/2), SIZE, SIZE)
    P2=pyg.rect.Rect(int(SCREEN_WIDTH/3), int(SCREEN_HEIGHT/4), SIZE, SIZE)
    P3=pyg.rect.Rect(int(SCREEN_WIDTH/3*2), int(SCREEN_HEIGHT/4*3), SIZE, SIZE)
    P4=pyg.rect.Rect(int(SCREEN_WIDTH/4*3), int(SCREEN_HEIGHT/2), SIZE, SIZE)
    CURVE_CORDS=get_complete(P1,P2,P3,P4)
    print(CURVE_CORDS)

    #MAIN LOOP
    run = True
    while run:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                syexit()
            elif event.type == pyg.MOUSEBUTTONDOWN:
                if event.button == 1:            
                    if P1.collidepoint(event.pos):
                        DRAG1 = True
                        mouse_x, mouse_y = event.pos
                        offset_x = P1.x - mouse_x
                        offset_y = P1.y - mouse_y
                    elif P2.collidepoint(event.pos):
                        DRAG2 = True
                        mouse_x, mouse_y = event.pos
                        offset_x = P2.x - mouse_x
                        offset_y = P2.y - mouse_y
                    elif P3.collidepoint(event.pos):
                        DRAG3 = True
                        mouse_x, mouse_y = event.pos
                        offset_x = P3.x - mouse_x
                        offset_y = P3.y - mouse_y
                    elif P4.collidepoint(event.pos):
                        DRAG4 = True
                        mouse_x, mouse_y = event.pos
                        offset_x = P4.x - mouse_x
                        offset_y = P4.y - mouse_y

            elif event.type == pyg.MOUSEBUTTONUP:
                if event.button == 1:            
                    DRAG1 = False
                    DRAG2 = False
                    DRAG3 = False
                    DRAG4 = False

            elif event.type == pyg.MOUSEMOTION:
                if DRAG1 or DRAG2 or DRAG3 or DRAG4:
                    CURVE_CORDS.clear()
                    CURVE_CORDS=get_complete(P1,P2,P3,P4)
                    mouse_x, mouse_y = event.pos
                if DRAG1:
                    P1.x = mouse_x + offset_x
                    P1.y = mouse_y + offset_y
                elif DRAG2:
                    P2.x = mouse_x + offset_x
                    P2.y = mouse_y + offset_y
                elif DRAG3:
                    P3.x = mouse_x + offset_x
                    P3.y = mouse_y + offset_y
                elif DRAG4:
                    P4.x = mouse_x + offset_x
                    P4.y = mouse_y + offset_y

        SCREEN.fill(BG_COLOR)
        pyg.draw.rect(SCREEN, (240,30,0), P1)
        pyg.draw.rect(SCREEN, (30, 240, 0), P2)
        pyg.draw.rect(SCREEN, (240, 240, 30), P3)
        pyg.draw.rect(SCREEN, (30, 210, 240), P4)
        if DRAW:
            if T<=100:
                T+=0.5
            else:
                T=0
            get_tpoint_curve(P1,P2,P3,P4,T,True)

        for cord in CURVE_CORDS:
            pyg.draw.circle(SCREEN, (255,255,255), cord, int(SIZE/15))

        clock.tick(60)
        pyg.display.set_caption(f'Rendering Bezier Curve--{int(clock.get_fps())}')
        pyg.display.update()

if __name__=='__main__':
    main(False)