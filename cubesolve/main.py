# r d r2 u' f' u r' l' f b' l' d2 u' r' u f2 u2 l2 r2 b' d' u d2 l' r

from move import move, blueprint
from data import initlst
from solve import solve
import copy

a = blueprint.cube()

spin = {"L":move.L, "R":move.R, "F":move.F, "B":move.B, "U":move.U, "D":move.D,
       "L'":move.rL, "R'":move.rR, "F'":move.rF, "B'":move.rB, "U'":move.rU, "D'":move.rD,
        "M":move.M, "PRINT":list}

solution = {0:solve.first1, 1:solve.first2, 2:solve.second, 3:solve.third, 4:solve.fourth, 5:solve.fifth,
            6:solve.sixth, 7:solve.seventh}

#level_select = input("select base level : ").upper()
a.lst = copy.deepcopy(initlst.lst)

while True:
    order = input('Next command? ').upper().split()
    #print(order)
    for i in order:
        if(i == 'INIT'):
            a.lst = copy.deepcopy(initlst.lst)
            a.output(a.lst)
            continue
        
        elif(i == 'EXIT'):
            print("byebye")
            exit()
        elif(i == "SOLVE"):
            mix = input("cube mix spin : ").upper().split()
            for j in mix:
                if(j.count('2')):
                    j = j.replace('2', '')
                    spin[j](spin[j](a.lst))
                else:
                    spin[j](a.lst)
        
                print('spin = %s' % j, end = '\n\n')

            for j in range(8):
                solution[j](a)
                a.output(a.lst)
                print("%d success" % j)

        try:
            if(i.count('2')):
                i = i.replace('2', '')
                spin[i](spin[i](a.lst))
            else:
                spin[i](a.lst)

            a.output(a.lst)
            
        except KeyError:
            print('KeyError, Invalied command, Please command again')
            continue
        
        print('spin = %s' % i, end = '\n\n')
