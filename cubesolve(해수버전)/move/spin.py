from move import rotate, blueprint


direction = {"L":rotate.L, "R":rotate.R, "F":rotate.F, "B":rotate.B, "U":rotate.U, "D":rotate.D,
             "L'":rotate.rL, "R'":rotate.rR, "F'":rotate.rF, "B'":rotate.rB, "U'":rotate.rU, "D'":rotate.rD, "M":rotate.M}

def spin(lst, order):
    order = order.upper().split()
    for i in order:        
        try:
            if(i.count('2')):
                i = i.replace('2', '')
                direction[i](direction[i](lst))
            else:
                direction[i](lst)
            result = 'spin success'
        except KeyError:
            result = 'KeyError, Invalied command, Please command again'
            continue
        
        
    return (lst, result)
