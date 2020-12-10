from solve_pack.solve import solve_spin, spin
from gl_pack import move


def first1(lst): # 밑면 십자가 맞추기
    while True:
        for i in range(4):
            if(lst[9][4] == lst[10][4]):
                move.D(lst)
            else:
                i = 0
                break
        if(lst[10][5] == lst[9][4] == lst[11][4] == lst[10][3] == lst[10][4]):
            break
        elif(lst[10][4] in [lst[3][4], lst[4][5], lst[5][4], lst[4][3]]):
            while True:
                if(lst[5][4] != lst[10][4]):
                   move.U(lst)
                else: break
            move.F(move.F(lst))
        elif(lst[10][4] in [lst[7][3], lst[7][5], lst[5][7], lst[3][7], lst[1][5], lst[1][3], lst[3][1], lst[5][1]]):
            if(lst[5][7] == lst[10][4]):
                move.F(lst)
            elif(lst[5][1] == lst[10][4]):
                move.rF(lst)
            else:
                move.M(lst)
        elif(lst[10][4] in [lst[6][4], lst[4][6], lst[2][4], lst[4][2]]):
            while True:
                if(lst[6][4] != lst[10][4]):
                    move.U(lst)
                else: break
            spin.spin(lst, solve_spin.spin1_1)
        else:
            move.F(move.F(lst))
    return lst

def first2(lst): # 밑면 옆줄 맞추기
    while True:
        if(lst[8][4] != lst[7][4]):
            move.D(lst)
        else:
            if(lst[4][0] == lst[4][1] and lst[4][7] == lst[4][8]):
                break
            elif(lst[1][4] == lst[0][4]):
                spin.spin(lst, solve_spin.spin2_1)
            else:
                if(lst[4][0] == lst[4][7]):
                    move.D(lst)
                    spin.spin(lst, solve_spin.spin2_2)
                else:
                    move.rD(lst)
                    spin.spin(lst, solve_spin.spin2_3)
    return lst

def second(lst): # 밑면 완성하기
    while True:
        if(lst[5][8] == lst[3][8] and lst[0][5] == lst[0][3] and
           lst[3][0] == lst[5][0] and lst[8][3] == lst[8][5] and
           lst[9][5] == lst[10][4] and lst[9][3] == lst[10][4] and
           lst[11][3] == lst[10][4] and lst[11][5] == lst[10][4]):
            break
        elif(lst[10][4] in [lst[6][5], lst[3][6], lst[2][3], lst[5][2]]):
            while True:
                if(lst[6][5] != lst[10][4]):
                    move.U(lst)
                elif(lst[6][5] == lst[10][4] and lst[5][5] == lst[7][4] and lst[5][6] == lst[4][7]):
                    spin.spin(lst, solve_spin.spin3_1)
                    break
                else:
                    move.rD(move.M(lst))
        elif(lst[10][4] in [lst[6][3], lst[5][6], lst[2][5], lst[3][2]]):
            while True:
                if(lst[5][6] != lst[10][4]):
                    move.U(lst)
                elif(lst[5][6] == lst[10][4] and lst[6][5] == lst[7][4] and lst[5][5] == lst[4][7]):
                    spin.spin(lst, solve_spin.spin3_2)
                    break
                else:
                    move.rD(move.M(lst))
        elif(lst[10][4] in [lst[3][3], lst[5][3], lst[5][5], lst[3][5]]):
            while True:
                if(lst[5][5] != lst[10][4]):
                    move.U(lst)
                elif(lst[5][5] == lst[10][4] and lst[6][5] == lst[4][7] and lst[5][6] == lst[7][4]):
                    spin.spin(lst, solve_spin.spin3_3)
                    break
                else:
                    move.rD(move.M(lst))
        elif(lst[10][4] in [lst[8][5], lst[5][8]]):
            spin.spin(lst, solve_spin.spin3_3)
        elif(lst[10][4] == lst[9][5] and lst[4][7] != lst[5][8] and lst[7][4] != lst[8][5]):
            spin.spin(lst, solve_spin.spin3_2)
        else:
            move.rD(move.M(lst))

    return lst

def third(lst): # 2층 완성하기
    while True:
        for i in range(4):
            if(lst[6][4] == lst[4][4] or lst[5][4] == lst[4][4]):
                move.U(lst)
            elif(lst[6][4] != lst[7][4]):
                move.rD(move.M(lst))
            else:
                i = 0
                break
        if(lst[7][3] == lst[7][4] == lst[7][5] and lst[3][7] == lst[4][7] == lst[5][7] and lst[1][3] == lst[1][4] == lst[1][5] and lst[3][1] == lst[4][1] == lst[5][1]):
            break
        elif(lst[6][4] == lst[7][4]):
            if(lst[5][4] == lst[4][7]):
                spin.spin(lst, solve_spin.spin4_1)
            else:
                spin.spin(lst, solve_spin.spin4_2)
        elif(lst[7][5] == lst[4][7] and lst[5][7] == lst[7][4]):
            spin.spin(lst, solve_spin.spin4_3)
        else:
            move.rD(move.M(lst))

    return lst
        

def fourth(lst): # 윗면 십자가 맞추기
    while True:
        for i in range(4):
            if(lst[4][3] != lst[4][4]):
                move.U(lst)
            else:
                break
        if(lst[3][4] == lst[4][3] == lst[5][4] == lst[4][5]):
            break
        elif(lst[4][3] == lst[4][5]):
            spin.spin(lst, solve_spin.spin5_1)
        elif(lst[4][3] == lst[3][4]):
            move.rU(lst)
        elif(lst[4][3] == lst[5][4]):
            spin.spin(lst, solve_spin.spin5_2)
        else:
            spin.spin(lst, solve_spin.spin5_1)

    return lst

def fifth(lst):  # 윗면 십자가 옆라인 맞추기
    while True:
        for i in range(4):
            if(lst[1][4] != lst[2][4]):
                move.U(lst)
            else: break
        if(lst[6][4] == lst[7][4] and lst[4][6] == lst[4][7] and lst[2][4] == lst[1][4] and lst[4][2] == lst[4][1]):
            break
        elif(lst[4][6] == lst[7][4] and lst[6][4] == lst[4][1] and lst[4][2] == lst[4][7]):
            spin.spin(lst, solve_spin.spin6_1)
        elif(lst[4][6] == lst[4][1] and lst[4][2] == lst[7][4] and lst[6][4] == lst[4][7]):
            spin.spin(lst, solve_spin.spin6_2)
        elif(lst[6][4] == lst[7][4]):
            spin.spin(lst, solve_spin.spin6_3)
        else:
            spin.spin(lst, solve_spin.spin6_4)

    return lst

def sixth(lst): # 윗면 맞추기
    while True:
        for i in range(4):
            if(lst[3][3] != lst[4][4]):
                move.U(lst)
            if lst[6][3] == lst[6][5] == lst[4][4]:
                if lst[2][3] == lst[2][5]:
                    spin.spin(lst, solve_spin.spin7_2)
                else:# lst[3][2] == lst[3][6]:
                    spin.spin(lst, solve_spin.spin7_3)
        if(lst[3][3] == lst[4][4] and lst[3][5] == lst[4][4] and lst[5][3] == lst[4][4] and lst[4][4] == lst[5][5]):
            break
        elif(lst[4][4] == lst[5][5]):
            if(lst[4][4] == lst[2][5] and lst[4][4] == lst[5][2]):
                move.U(move.U(lst))
                spin.spin(lst, solve_spin.spin7_1)
            else:
                spin.spin(lst, solve_spin.spin7_1) 
        elif(lst[5][3] == lst[4][4]):
            if(lst[3][6] == lst[4][4] and lst[5][6] == lst[4][4]):
                spin.spin(lst, solve_spin.spin7_1)
            elif(lst[2][5] == lst[4][4] and lst[6][5] == lst[4][4]):
                move.U(move.U(lst))
                spin.spin(lst, solve_spin.spin7_1)
        elif(lst[3][5] == lst[4][4]):
            if(lst[6][3] == lst[4][4] and lst[6][5] == lst[4][4]):
                move.rU(lst)
                spin.spin(lst, solve_spin.spin7_1)
            elif(lst[5][2] == lst[4][4] and lst[5][6] == lst[4][4]):
                move.U(lst)
                spin.spin(lst, solve_spin.spin7_1)
        elif(lst[3][6] == lst[4][4] and lst[6][5] == lst[4][4] and lst[5][2] == lst[4][4]):
            spin.spin(lst, solve_spin.spin7_1)
        elif(lst[2][5] == lst[4][4] and lst[5][6] == lst[4][4] and lst[6][3] == lst[4][4]):
            move.U(move.U(lst))
            spin.spin(lst, solve_spin.spin7_1)
        elif(lst[6][3] == lst[4][4] and lst[6][6] == lst[4][4]):
            spin.spin(lst, solve_spin.spin7_1)
    return lst
            
def seventh(lst): # 3층 엣지(모서리) 맞추
    while True:
        for i in range(4):
            if(lst[2][4] != lst[1][4] or lst[3][6] != lst[4][6]):
                move.U(lst)
            else: break
        if(lst[6][3] == lst[6][5] and lst[5][6] == lst[3][6] and
           lst[2][3] == lst[2][5] and lst[3][2] == lst[5][2] and
           lst[6][5] == lst[7][4] and lst[3][6] == lst[4][7] and
           lst[2][3] == lst[1][4] and lst[5][2] == lst[4][1] and lst[6][4] == lst[7][4]):
            break
        elif(lst[3][2] == lst[5][2] and lst[3][2] != lst[4][2]):
            spin.spin(lst, solve_spin.spin8_1)
        elif(lst[6][3] == lst[6][5] and lst[6][3] != lst[6][4]):
            spin.spin(lst, solve_spin.spin8_2)
        elif(lst[5][2] == lst[5][6] and lst[3][2] == lst[3][6] and
             lst[2][3] == lst[6][3] and lst[2][5] == lst[6][5]):
            spin.spin(lst, solve_spin.spin8_3)
        else:
            spin.spin(lst, solve_spin.spin8_4)
    return lst
