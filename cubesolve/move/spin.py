from move import move, blueprint
from graphic import graphic

direction = {"L":move.L, "R":move.R, "F":move.F, "B":move.B, "U":move.U, "D":move.D,
             "L'":move.rL, "R'":move.rR, "F'":move.rF, "B'":move.rB, "U'":move.rU, "D'":move.rD, "M":move.M, "PRINT":list}

def spin(lst, order):
    order = order.upper().split()
    for i in order:        
        try:
            if(i.count('2')):
                i = i.replace('2', '')
                direction[i](direction[i](lst))
            else:
                direction[i](lst)
            
        except KeyError:
            print('KeyError, Invalied command, Please command again')
            continue
        
        #print('spin = %s' % i, end = '\n\n')
        #graphic.image(lst)
    return lst
