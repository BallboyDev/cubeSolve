import turtle as t
import a
print(a.lst)

k = 35
color = {"B":"BLUE", "G":"GREEN", "O":"ORANGE", "R":"RED", "W":"WHITE", "Y":"YELLOW", " ": "BLACK"} 

x = [-175, -140, -105, -70, -35, 0, 35, 70, 105]
y = [210, 175, 140, 105, 70, 35, 0, -35, -70, -105, -140, -175]

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

def setcolor(lx, ly):
    return color[a.lst[lx][ly]]

t.bgcolor("BLACK")
t.ht()
t.speed(0)
t.penup()
for j in y:
    for i in x:
        t.goto(i, j)
        if(setcolor(y.index(j), x.index(i)) == "BLACK"):
            continue
        t.fillcolor(setcolor(y.index(j), x.index(i)))
        t.begin_fill()
        square()
        t.end_fill()
