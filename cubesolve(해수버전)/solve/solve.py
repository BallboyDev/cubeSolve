from move import blueprint, rotate, spin
from solve import solve_spin

def test(a):
    a.output(a.lst)
    rotate.L(a.lst)

def first1(a): # 밑면 십자가 맞추기
    while True:
        for i in range(4):
            if(a.lst[9][4] == a.lst[10][4]):
                rotate.D(a.lst)
            else:
                i = 0
                break
        if(a.lst[10][5] == a.lst[9][4] == a.lst[11][4] == a.lst[10][3] == a.lst[10][4]):
            break
        elif(a.lst[10][4] in [a.lst[3][4], a.lst[4][5], a.lst[5][4], a.lst[4][3]]):
            while True:
                if(a.lst[5][4] != a.lst[10][4]):
                   rotate.U(a.lst)
                else: break
            rotate.F(rotate.F(a.lst))
        elif(a.lst[10][4] in [a.lst[7][3], a.lst[7][5], a.lst[5][7], a.lst[3][7], a.lst[1][5], a.lst[1][3], a.lst[3][1], a.lst[5][1]]):
            if(a.lst[5][7] == a.lst[10][4]):
                rotate.F(a.lst)
            elif(a.lst[5][1] == a.lst[10][4]):
                rotate.rF(a.lst)
            else:
                rotate.M(a.lst)
        elif(a.lst[10][4] in [a.lst[6][4], a.lst[4][6], a.lst[2][4], a.lst[4][2]]):
            while True:
                if(a.lst[6][4] != a.lst[10][4]):
                    rotate.U(a.lst)
                else: break
            spin.spin(a.lst, solve_spin.spin1_1)
        else:
            rotate.F(rotate.F(a.lst))

def first2(a): # 밑면 옆줄 맞추기
    while True:
        if(a.lst[8][4] != a.lst[7][4]):
            rotate.D(a.lst)
        else:
            if(a.lst[4][0] == a.lst[4][1] and a.lst[4][7] == a.lst[4][8]):
                break
            elif(a.lst[1][4] == a.lst[0][4]):
                spin.spin(a.lst, solve_spin.spin2_1)
            else:
                if(a.lst[4][0] == a.lst[4][7]):
                    rotate.D(a.lst)
                    spin.spin(a.lst, solve_spin.spin2_2)
                else:
                    rotate.rD(a.lst)
                    spin.spin(a.lst, solve_spin.spin2_3)

def second(a): # 밑면 완성하기
    while True:
        if(a.lst[5][8] == a.lst[3][8] and a.lst[0][5] == a.lst[0][3] and
           a.lst[3][0] == a.lst[5][0] and a.lst[8][3] == a.lst[8][5] and
           a.lst[9][5] == a.lst[10][4] and a.lst[9][3] == a.lst[10][4] and
           a.lst[11][3] == a.lst[10][4] and a.lst[11][5] == a.lst[10][4]):
            break
        elif(a.lst[10][4] in [a.lst[6][5], a.lst[3][6], a.lst[2][3], a.lst[5][2]]):
            while True:
                if(a.lst[6][5] != a.lst[10][4]):
                    rotate.U(a.lst)
                elif(a.lst[6][5] == a.lst[10][4] and a.lst[5][5] == a.lst[7][4] and a.lst[5][6] == a.lst[4][7]):
                    spin.spin(a.lst, solve_spin.spin3_1)
                    break
                else:
                    rotate.rD(rotate.M(a.lst))
        elif(a.lst[10][4] in [a.lst[6][3], a.lst[5][6], a.lst[2][5], a.lst[3][2]]):
            while True:
                if(a.lst[5][6] != a.lst[10][4]):
                    rotate.U(a.lst)
                elif(a.lst[5][6] == a.lst[10][4] and a.lst[6][5] == a.lst[7][4] and a.lst[5][5] == a.lst[4][7]):
                    spin.spin(a.lst, solve_spin.spin3_2)
                    break
                else:
                    rotate.rD(rotate.M(a.lst))
        elif(a.lst[10][4] in [a.lst[3][3], a.lst[5][3], a.lst[5][5], a.lst[3][5]]):
            while True:
                if(a.lst[5][5] != a.lst[10][4]):
                    rotate.U(a.lst)
                elif(a.lst[5][5] == a.lst[10][4] and a.lst[6][5] == a.lst[4][7] and a.lst[5][6] == a.lst[7][4]):
                    spin.spin(a.lst, solve_spin.spin3_3)
                    break
                else:
                    rotate.rD(rotate.M(a.lst))
        elif(a.lst[10][4] in [a.lst[8][5], a.lst[5][8]]):
            spin.spin(a.lst, solve_spin.spin3_3)
        elif(a.lst[10][4] == a.lst[9][5] and a.lst[4][7] != a.lst[5][8] and a.lst[7][4] != a.lst[8][5]):
            spin.spin(a.lst, solve_spin.spin3_2)
        else:
            rotate.rD(rotate.M(a.lst))

def third(a): # 2층 완성하기
    while True:
        for i in range(4):
            if(a.lst[6][4] == a.lst[4][4] or a.lst[5][4] == a.lst[4][4]):
                rotate.U(a.lst)
            elif(a.lst[6][4] != a.lst[7][4]):
                rotate.rD(rotate.M(a.lst))
            else:
                i = 0
                break
        if(a.lst[7][3] == a.lst[7][4] == a.lst[7][5] and a.lst[3][7] == a.lst[4][7] == a.lst[5][7] and a.lst[1][3] == a.lst[1][4] == a.lst[1][5] and a.lst[3][1] == a.lst[4][1] == a.lst[5][1]):
            break
        elif(a.lst[6][4] == a.lst[7][4]):
            if(a.lst[5][4] == a.lst[4][7]):
                spin.spin(a.lst, solve_spin.spin4_1)
            else:
                spin.spin(a.lst, solve_spin.spin4_2)
        elif(a.lst[7][5] == a.lst[4][7] and a.lst[5][7] == a.lst[7][4]):
            spin.spin(a.lst, solve_spin.spin4_3)
        else:
            rotate.rD(rotate.M(a.lst))
        

def fourth(a): # 윗면 십자가 맞추기
    while True:
        for i in range(4):
            if(a.lst[4][3] != a.lst[4][4]):
                rotate.U(a.lst)
            else:
                break
        if(a.lst[3][4] == a.lst[4][3] == a.lst[5][4] == a.lst[4][5]):
            break
        elif(a.lst[4][3] == a.lst[4][5]):
            spin.spin(a.lst, solve_spin.spin5_1)
        elif(a.lst[4][3] == a.lst[3][4]):
            rotate.rU(a.lst)
        elif(a.lst[4][3] == a.lst[5][4]):
            spin.spin(a.lst, solve_spin.spin5_2)
        else:
            spin.spin(a.lst, solve_spin.spin5_1)

def fifth(a):  # 윗면 십자가 옆라인 맞추기
    while True:
        for i in range(4):
            if(a.lst[1][4] != a.lst[2][4]):
                rotate.U(a.lst)
            else: break
        if(a.lst[6][4] == a.lst[7][4] and a.lst[4][6] == a.lst[4][7] and a.lst[2][4] == a.lst[1][4] and a.lst[4][2] == a.lst[4][1]):
            break
        elif(a.lst[4][6] == a.lst[7][4] and a.lst[6][4] == a.lst[4][1] and a.lst[4][2] == a.lst[4][7]):
            spin.spin(a.lst, solve_spin.spin6_1)
        elif(a.lst[4][6] == a.lst[4][1] and a.lst[4][2] == a.lst[7][4] and a.lst[6][4] == a.lst[4][7]):
            spin.spin(a.lst, solve_spin.spin6_2)
        elif(a.lst[6][4] == a.lst[7][4]):
            spin.spin(a.lst, solve_spin.spin6_3)
        else:
            spin.spin(a.lst, solve_spin.spin6_4)

def sixth(a): # 윗면 맞추기
    while True:
        for i in range(4):
            if(a.lst[3][3] != a.lst[4][4]):
                rotate.U(a.lst)
        if(a.lst[3][3] == a.lst[4][4] and a.lst[3][5] == a.lst[4][4] and a.lst[5][3] == a.lst[4][4] and a.lst[4][4] == a.lst[5][5]):
            break
        elif(a.lst[4][4] == a.lst[5][5]):
            if(a.lst[4][4] == a.lst[2][5] and a.lst[4][4] == a.lst[5][2]):
                rotate.U(rotate.U(a.lst))
                spin.spin(a.lst, solve_spin.spin7_1)
            else:
                spin.spin(a.lst, solve_spin.spin7_1) 
        elif(a.lst[5][3] == a.lst[4][4]):
            if(a.lst[3][6] == a.lst[4][4] and a.lst[5][6] == a.lst[4][4]):
                spin.spin(a.lst, solve_spin.spin7_1)
            elif(a.lst[2][5] == a.lst[4][4] and a.lst[6][5] == a.lst[4][4]):
                rotate.U(rotate.U(a.lst))
                spin.spin(a.lst, solve_spin.spin7_1)
        elif(a.lst[3][5] == a.lst[4][4]):
            if(a.lst[6][3] == a.lst[4][4] and a.lst[6][5] == a.lst[4][4]):
                rotate.rU(a.lst)
                spin.spin(a.lst, solve_spin.spin7_1)
            elif(a.lst[5][2] == a.lst[4][4] and a.lst[5][6] == a.lst[4][4]):
                rotate.U(a.lst)
                spin.spin(a.lst, solve_spin.spin7_1)
        elif(a.lst[3][6] == a.lst[4][4] and a.lst[6][5] == a.lst[4][4] and a.lst[5][2] == a.lst[4][4]):
            spin.spin(a.lst, solve_spin.spin7_1)
        elif(a.lst[2][5] == a.lst[4][4] and a.lst[5][6] == a.lst[4][4] and a.lst[6][3] == a.lst[4][4]):
            rotate.U(rotate.U(a.lst))
            spin.spin(a.lst, solve_spin.spin7_1)
        elif(a.lst[6][3] == a.lst[4][4] and a.lst[6][6] == a.lst[4][4]):
            spin.spin(a.lst, solve_spin.spin7_1)
            
def seventh(a): # 3층 엣지(모서리) 맞추
    while True:
        for i in range(4):
            if(a.lst[2][4] != a.lst[1][4] or a.lst[3][6] != a.lst[4][6]):
                rotate.U(a.lst)
            else: break
        if(a.lst[6][3] == a.lst[6][5] and a.lst[5][6] == a.lst[3][6] and
           a.lst[2][3] == a.lst[2][5] and a.lst[3][2] == a.lst[5][2] and
           a.lst[6][5] == a.lst[7][4] and a.lst[3][6] == a.lst[4][7] and
           a.lst[2][3] == a.lst[1][4] and a.lst[5][2] == a.lst[4][1] and a.lst[6][4] == a.lst[7][4]):
            break
        elif(a.lst[3][2] == a.lst[5][2] and a.lst[3][2] != a.lst[4][2]):
            spin.spin(a.lst, solve_spin.spin8_1)
        elif(a.lst[6][3] == a.lst[6][5] and a.lst[6][3] != a.lst[6][4]):
            spin.spin(a.lst, solve_spin.spin8_2)
        elif(a.lst[5][2] == a.lst[5][6] and a.lst[3][2] == a.lst[3][6] and
             a.lst[2][3] == a.lst[6][3] and a.lst[2][5] == a.lst[6][5]):
            spin.spin(a.lst, solve_spin.spin8_3)
        else:
            spin.spin(a.lst, solve_spin.spin8_4)
