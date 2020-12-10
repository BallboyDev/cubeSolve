import threading
import pygame
from pygame.locals import *
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import time
from cv_pack.package import camera_take


from gl_pack import button, move
from gl_pack.quat import *
from gl_pack.geometry import *

from cv_pack import planar_figure_and_color_extraction

from solve_pack.solve import solve


form_class = uic.loadUiType("gl_pack/button_gui.ui")[0]

solution = {0: solve.first1, 1: solve.first2, 2: solve.second, 3: solve.third, 4: solve.fourth, 5: solve.fifth,
            6: solve.sixth, 7: solve.seventh}

      # '0','1','2','3','4','5','6','7','8'
lst = [[' ',' ',' ','B','B','B',' ',' ',' '], #0    0
       [' ',' ',' ','B','B','B',' ',' ',' '], #1  5 1 4
       [' ',' ',' ','B','B','B',' ',' ',' '], #2    2
       ['R','R','R','Y','Y','Y','O','O','O'], #3    3
       ['R','R','R','Y','Y','Y','O','O','O'], #4
       ['R','R','R','Y','Y','Y','O','O','O'], #5
       [' ',' ',' ','G','G','G',' ',' ',' '], #6
       [' ',' ',' ','G','G','G',' ',' ',' '], #7
       [' ',' ',' ','G','G','G',' ',' ',' '], #8
       [' ',' ',' ','P','P','P',' ',' ',' '], #9
       [' ',' ',' ','P','P','P',' ',' ',' '], #10
       [' ',' ',' ','P','P','P',' ',' ',' ']] #11

position = (((0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1,5 ), (2, 3), (2, 4), (2, 5)),
            ((3,3), (3,4), (3,5), (4,3), (4,4), (4,5), (5,3), (5,4), (5,5)),
            ((6,3), (6,4), (6,5), (7,3), (7,4), (7,5), (8,3), (8,4), (8,5)),
            ((9,3), (9,4), (9,5), (10,3), (10,4), (10,5), (11,3), (11,4), (11,5)),
            ((3,6), (3,7), (3,8), (4,6), (4,7), (4,8), (5,6), (5,7), (5,8)),
            ((3,0), (3,1), (3,2), (4,0), (4,1), (4,2), (5,0), (5,1), (5,2)))

Purple = (0.5, 0, 0.5)
Blue = (0, 0, 1)
Yellow = (1.0, 1, 0.0)
Green = (0.0, 1, 0)
Red = (1, 0, 0)
Orange = (1.0, 0.5, 0.0)

cube_stickers = (
    # 0 0
    ((-2.95, 1.025, 3.01),
    (-2.95, 2.95, 3.01),
    (-1.025, 2.95, 3.01),
    (-1.025, 1.025, 3.01)),

    # 0 1
    ((-0.9625, 1.025, 3.01),
    (-0.9625, 2.95, 3.01),
    (0.9625, 2.95, 3.01),
    (0.9625, 1.025, 3.01)),

    # 0 2
    ((1.025, 1.025, 3.01),
    (1.025, 2.95, 3.01),
    (2.95, 2.95, 3.01),
    (2.95, 1.025, 3.01)),

    # 1 0
    ((-2.95, -0.9625, 3.01),
    (-2.95, 0.9625, 3.01),
    (-1.025, 0.9625, 3.01),
    (-1.025, -0.9625, 3.01)),

    # 1 1
    ((-0.9625, -0.9625, 3.01),
    (-0.9625, 0.9625, 3.01),
    (0.9625, 0.9625, 3.01),
    (0.9625, -0.9625, 3.01)),

    # 1 2
    ((1.025, -0.9625, 3.01),
    (1.025, 0.9625, 3.01),
    (2.95, 0.9625, 3.01),
    (2.95, -0.9625, 3.01)),

    # 2 0
    ((-2.95, -2.95, 3.01),
    (-2.95, -1.025, 3.01),
    (-1.025, -1.025, 3.01),
    (-1.025, -2.95, 3.01)),

    # 2 1
    ((-0.9625, -2.95, 3.01),
    (-0.9625, -1.025, 3.01),
    (0.9625, -1.025, 3.01),
    (0.9625, -2.95, 3.01)),

    # 2 2
    ((1.025, -2.95, 3.01),
    (1.025, -1.025, 3.01),
    (2.95, -1.025, 3.01),
    (2.95, -2.95, 3.01))
)

cube_pieces = (
    (-2.95, -2.95, 2.95),
    (-2.95, -1.025, 2.95),
    (-1.025, -1.025, 2.95),
    (-1.025, -2.95, 2.95),
    (-2.95, -2.95, 1.025),
    (-2.95, -1.025, 1.025),
    (-1.025, -1.025, 1.025),
    (-1.025, -2.95, 1.025)
)

up_face = (
    (-3.0, 1.0, 3.0),
    (-3.0, 3.0, 3.0),       # 1
    (3.0, 3.0, 3.0),        # 2
    (3.0, 1.0, 3.0),
    (-3.0, 1.0, -3.0),
    (-3.0, 3.0, -3.0),      # 5
    (3.0, 3.0, -3.0),        # 6
    (3.0, 1.0, -3.0)
)

def up():
    global lst
    lst = move.U(lst)


def select_color(cls):
    if cls == "P":
        return Purple
    elif cls == "R":
        return Red
    elif cls == "Y":
        return Yellow
    elif cls == "B":
        return Blue
    elif cls == "G":
        return Green
    elif cls == "O":
        return Orange


def draw_stickers(num, lst):
    for v in range(len(cube_stickers)):
        cls = select_color(lst[position[num][v][0]][position[num][v][1]])
        glColor3fv(cls)
        glBegin(GL_QUADS)
        for i in range(4):
            glVertex3fv(cube_stickers[v][i])
        glEnd()

def cube(lst):
    glBegin(GL_QUADS)
    for surface in cube_surfaces:
        glColor3fv((0, 0, 0))
        for vertex in surface:
            glVertex3fv(cube_verts[vertex])
    glEnd()


    # Purple
    draw_stickers(0, lst)
    glRotate(90, 1, 0, 0)

    # Blue
    draw_stickers(1, lst)
    glRotate(90, 1, 0, 0)

    # Yellow
    draw_stickers(2, lst)
    glRotate(90, 1, 0, 0)

    # Green
    draw_stickers(3, lst)
    glRotate(90, 0, 1, 0)
    glRotate(180, 0, 0, 1)

    # Orange
    draw_stickers(4, lst)
    glRotate(180, 0, 1, 0)

    # Red
    draw_stickers(5, lst)


    glBegin(GL_LINES)
    glColor3fv((0.5, 0.5, 0.5))
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_verts[vertex])
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_pieces[vertex])
    glEnd()


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.UP)
        self.pushButton_2.clicked.connect(self.rUP)
        self.pushButton_8.clicked.connect(self.DOWN)
        self.pushButton_7.clicked.connect(self.rDOWN)
        self.pushButton_9.clicked.connect(self.LEFT)
        self.pushButton_10.clicked.connect(self.rLEFT)
        self.pushButton_12.clicked.connect(self.RIGHT)
        self.pushButton_11.clicked.connect(self.rRIGHT)
        self.pushButton_4.clicked.connect(self.FRONT)
        self.pushButton_3.clicked.connect(self.rFRONT)
        self.pushButton_6.clicked.connect(self.BACK)
        self.pushButton_5.clicked.connect(self.rBACK)
        self.pushButton_16.clicked.connect(self.INIT)
        self.pushButton_17.clicked.connect(self.QUIT)
        self.pushButton_18.clicked.connect(self.MIX)
        self.pushButton_14.clicked.connect(self.IMAGE)
        self.pushButton_19.clicked.connect(self.CAMERA)
        self.pushButton_15.clicked.connect(self.SOLVE)

    def UP(self):
        global lst
        lst = move.U(lst)

    def DOWN(self):
        global lst
        lst = move.D(lst)

    def RIGHT(self):
        global lst
        lst = move.R(lst)

    def LEFT(self):
        global lst
        lst = move.L(lst)

    def FRONT(self):
        global lst
        lst = move.F(lst)

    def BACK(self):
        global lst
        lst = move.B(lst)

    def rUP(self):
        global lst
        lst = move.rU(lst)

    def rDOWN(self):
        global lst
        lst = move.rD(lst)

    def rRIGHT(self):
        global lst
        lst = move.rR(lst)

    def rLEFT(self):
        global lst
        lst = move.rL(lst)

    def rFRONT(self):
        global lst
        lst = move.rF(lst)

    def rBACK(self):
        global lst
        lst = move.rB(lst)

    def INIT(self):
        global lst
        lst = [
        [' ',' ',' ','B','B','B',' ',' ',' '], #0    1
        [' ',' ',' ','B','B','B',' ',' ',' '], #1   625
        [' ',' ',' ','B','B','B',' ',' ',' '], #2    3
        ['R','R','R','Y','Y','Y','O','O','O'], #3    4
        ['R','R','R','Y','Y','Y','O','O','O'], #4
        ['R','R','R','Y','Y','Y','O','O','O'], #5
        [' ',' ',' ','G','G','G',' ',' ',' '], #6
        [' ',' ',' ','G','G','G',' ',' ',' '], #7
        [' ',' ',' ','G','G','G',' ',' ',' '], #8
        [' ',' ',' ','P','P','P',' ',' ',' '], #9
        [' ',' ',' ','P','P','P',' ',' ',' '], #10
        [' ',' ',' ','P','P','P',' ',' ',' ']] #11
        # 0   1   2   3   4   5   6   7   8

    def QUIT(self):
        quit()

    def MIX(self):
        global lst
        #Dwhile True:
        for i in range(50):
            #time.sleep(0.07)
            k = random.randint(0, 12)
            if (k == 0):
                lst = move.U(lst)
            elif (k == 1):
                lst = move.rU(lst)
            elif (k == 2):
                lst = move.D(lst)
            elif (k == 3):
                lst = move.rD(lst)
            elif (k == 4):
                lst = move.L(lst)
            elif (k == 5):
                lst = move.rL(lst)
            elif (k == 6):
                lst = move.R(lst)
            elif (k == 7):
                lst = move.rR(lst)
            elif (k == 8):
                lst = move.F(lst)
            elif (k == 9):
                lst = move.rF(lst)
            elif (k == 10):
                lst = move.B(lst)
            elif (k == 11):
                lst = move.rB(lst)

    def IMAGE(self):
        global lst
        lst = planar_figure_and_color_extraction.main(lst, 1)

    def CAMERA(self):
        print("Camera")
        global lst
        camera_take.capture(1)
        print("finish 1")
        camera_take.capture(2)
        print("finish 2")
        lst = planar_figure_and_color_extraction.main(lst, 2)

    def SOLVE(self):
        global lst, solution
        print("test")
        for j in range(8):
            lst = solution[j](lst)
            print("%d success" % j)
        print(lst)

    

def BUTTON_GUI():
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()


def main():
    global lst

    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    pygame.display.set_caption('3D CUBE')
    glClearColor(1, 1, 1, 0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.5, 40)
    glTranslatef(0.0, 0, -17.5)

    inc_x = 0
    inc_y = 0
    accum = (0, 1, 0, 0)
    zoom = 1


    t = threading.Thread(target = BUTTON_GUI)
    t.daemon = True
    t.start()

    while True:
        [inc_x, inc_y, accum, zoom, lst] = button.control(inc_x, inc_y, accum, zoom, lst)

        if pygame.mouse.get_pressed()[0] == 1:
            (tmp_x, tmp_y) = pygame.mouse.get_rel()
            inc_x = -tmp_y * pi / 450
            inc_y = -tmp_x * pi / 450

        pygame.mouse.get_rel()

        rot_x = normalize(axisangle_to_q((1.0, 0.0, 0.0), inc_x))
        rot_y = normalize(axisangle_to_q((0.0, 1.0, 0.0), inc_y))

        accum = q_mult(accum, rot_x)
        accum = q_mult(accum, rot_y)

        glMatrixMode(GL_MODELVIEW)
        glLoadMatrixf(q_to_mat4(accum))
        glScalef(zoom, zoom, zoom)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        cube(lst)

        pygame.display.flip()
        pygame.time.wait(1)


if __name__ == "__main__":
    main()
