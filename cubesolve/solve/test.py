from cubesolve.move import blueprint, initlst

def test(a):
    a.output(a.lst)
    a.lst = initlst.lst_R
    a.output(a.lst)
