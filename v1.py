import turtle
import math
from random import choice
win = turtle.Screen()
W,H=750,700
win.setup(W,H)
win.title("quadratic curve")
painter = turtle.Turtle()
substitute = turtle.Turtle()
curve = turtle.Turtle()
#turtle.tracer(0, 0)
        
P1,P2,P3=((20-W/2),0),(0,(H/2-20)),((W/2-20),0)
#P1,P2,P3=(-300,-50),(50,-100),(300,100)
Dist1=math.sqrt((P2[0]-P1[0])**2 + (P2[1]-P1[1])**2)
Dist2=math.sqrt((P2[0]-P3[0])**2 + (P2[1]-P3[1])**2)
Angle1=math.atan((P2[0]-P1[0])/(P2[1]-P1[1]))
Angle2=math.atan((P3[0]-P2[0])/(P3[1]-P2[1]))
if Angle1<0:
    Angle1=math.radians(math.degrees(Angle1)+180)
if Angle2<0:
    Angle2=math.radians(math.degrees(Angle2)+180)

def setup():
    painter.speed(0)
    painter.left(90)
    painter.penup()
    painter.goto(P3)
    painter.dot(10,'blue')
    painter.goto(P2)
    painter.dot(10,'green')
    painter.goto(P1)
    painter.dot(10,'red')
    painter.pendown()
    substitute.left(90)
    substitute.speed(0)
    substitute.penup()
    substitute.goto(P2)
    substitute.pendown()
    curve.speed(0)
    curve.penup()
    curve.color('gold')
def draw_curve(itr=3):
    t=0
    while t<=100:
        painter.pendown()
        xp=math.sin(Angle1)*(t/100*Dist1)+P1[0]
        yp=math.cos(Angle1)*(t/100*Dist1)+P1[1]
        painter.goto(xp, yp)
        painter.penup()

        substitute.pendown()
        xp=math.sin(Angle2)*(t/100*Dist2)+P2[0]
        yp=math.cos(Angle2)*(t/100*Dist2)+P2[1]
        substitute.goto(xp, yp)
        substitute.penup()

        curve.goto(painter.pos())
        curve.pendown()
        curve.goto(substitute.pos())
        curve.penup()
        t+=itr

setup()
print(round(Dist1), round(Dist2))
print(Angle1, Angle2)
draw_curve()
turtle.update()
turtle.exitonclick()
