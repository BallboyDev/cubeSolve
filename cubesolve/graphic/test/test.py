import turtle as t

k = 35

def right():
    t.setheading(0)
    t.forward(k)
    
def left():
    t.setheading(180)
    t.forward(k)
def up():
    t.setheading(90)
    t.forward(k)

def down():
    t.setheading(270)
    t.forward(k)

def blank():
    #t.home()
    t.clear()

def color_start():
    t.fillcolor("RED")
    t.begin_fill()

def color_finish():
    t.end_fill()

def position():
    print(t.position())

def line():
    print("====================")

def long():
    global k
    k += 5
    print("현 거리 : ", k)

def short():
    global k
    k -= 5
    print("현 거리 : ", k)
    
t.shape("turtle")
t.speed(0)

t.onkeypress(right, "Right")
t.onkeypress(left, "Left")
t.onkeypress(up, "Up")
t.onkeypress(down, "Down")
t.onkeypress(blank, "Escape")
t.onkeypress(position, "e")
t.onkeypress(line, "g")
t.onkeypress(color_start, "s")
t.onkeypress(color_finish, "f")
t.onkeypress(long, ">")
t.onkeypress(short, "<")
t.listen()
    
