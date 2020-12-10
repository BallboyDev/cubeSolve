import turtle as t
#import a
from move import blueprint

k = 35
color = {"B":"BLUE", "G":"GREEN", "O":"ORANGE", "R":"RED", "W":"WHITE", "Y":"YELLOW", " ": "BLACK"} 

x = [-5*k, -4*k, -3*k, -2*k, -1*k, 0*k, 1*k, 2*k, 3*k]
y = [6*k, 5*k, 4*k, 3*k, 2*k, 1*k, 0*k, -1*k, -2*k, -3*k, -4*k, -5*k]

def square():
    t.setheading(0)
    t.pendown()
    t.forward(k)
    t.right(90)
    t.forward(k)
    t.right(90)
    t.forward(k)
    t.right(90)
    t.forward(k)
    t.right(90)
    t.penup()

def setcolor(lst, lx, ly):
    return color[lst[lx][ly]]

def image(lst):
    t.bgcolor("BLACK")
    t.ht()
    t.speed(0)
    t.penup()
    for j in y:
        for i in x:
            t.goto(i, j)
            if(setcolor(lst, y.index(j), x.index(i)) == "BLACK"):
                continue
            t.fillcolor(setcolor(lst, y.index(j), x.index(i)))
            t.begin_fill()
            square()
            t.end_fill()
