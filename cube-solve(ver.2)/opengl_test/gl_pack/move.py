# lst[][], lst[][], lst[][], lst[][] = lst[][], lst[][], lst[][], lst[][]
import time

def U(lst):
    time.sleep(0.07)
    lst[3][4], lst[4][3], lst[5][4], lst[4][5] = lst[4][3], lst[5][4], lst[4][5], lst[3][4]
    lst[3][3], lst[5][3], lst[5][5], lst[3][5] = lst[5][3], lst[5][5], lst[3][5], lst[3][3]
    lst[6][5], lst[3][6], lst[2][3], lst[5][2] = lst[3][6], lst[2][3], lst[5][2], lst[6][5]
    lst[6][4], lst[4][6], lst[2][4], lst[4][2] = lst[4][6], lst[2][4], lst[4][2], lst[6][4]
    lst[6][3], lst[5][6], lst[2][5], lst[3][2] = lst[5][6], lst[2][5], lst[3][2], lst[6][3]
    print("spin = U", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("U ")
    f.close()
    return lst

def rU(lst):
    time.sleep(0.07)
    lst[4][3], lst[5][4], lst[4][5], lst[3][4] = lst[3][4], lst[4][3], lst[5][4], lst[4][5]
    lst[5][3], lst[5][5], lst[3][5], lst[3][3] = lst[3][3], lst[5][3], lst[5][5], lst[3][5]
    lst[3][6], lst[2][3], lst[5][2], lst[6][5] = lst[6][5], lst[3][6], lst[2][3], lst[5][2]
    lst[4][6], lst[2][4], lst[4][2], lst[6][4] = lst[6][4], lst[4][6], lst[2][4], lst[4][2]
    lst[5][6], lst[2][5], lst[3][2], lst[6][3] = lst[6][3], lst[5][6], lst[2][5], lst[3][2]
    print("spin = rU", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("rU ")
    f.close()
    return lst

def D(lst):
    time.sleep(0.07)
    lst[9][4], lst[10][3], lst[11][4], lst[10][5] = lst[10][3], lst[11][4], lst[10][5], lst[9][4]
    lst[9][3], lst[11][3], lst[11][5], lst[9][5] = lst[11][3], lst[11][5], lst[9][5], lst[9][3]
    lst[0][3], lst[3][8], lst[8][5], lst[5][0] = lst[3][8], lst[8][5], lst[5][0], lst[0][3]
    lst[0][4], lst[4][8], lst[8][4], lst[4][0] = lst[4][8], lst[8][4], lst[4][0], lst[0][4]
    lst[0][5], lst[5][8], lst[8][3], lst[3][0] = lst[5][8], lst[8][3], lst[3][0], lst[0][5]
    print("spin = D", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("D ")
    f.close()
    return lst

def rD(lst):
    time.sleep(0.07)
    lst[10][3], lst[11][4], lst[10][5], lst[9][4] = lst[9][4], lst[10][3], lst[11][4], lst[10][5]
    lst[11][3], lst[11][5], lst[9][5], lst[9][3] = lst[9][3], lst[11][3], lst[11][5], lst[9][5]
    lst[3][8], lst[8][5], lst[5][0], lst[0][3] = lst[0][3], lst[3][8], lst[8][5], lst[5][0]
    lst[4][8], lst[8][4], lst[4][0], lst[0][4] = lst[0][4], lst[4][8], lst[8][4], lst[4][0]
    lst[5][8], lst[8][3], lst[3][0], lst[0][5] = lst[0][5], lst[5][8], lst[8][3], lst[3][0]
    print("spin = rD", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("rD ")
    f.close()
    return lst

def L(lst):
    time.sleep(0.07)
    lst[3][1], lst[4][0], lst[5][1], lst[4][2] = lst[4][0], lst[5][1], lst[4][2], lst[3][1]
    lst[3][0], lst[5][0], lst[5][2], lst[3][2] = lst[5][0], lst[5][2], lst[3][2], lst[3][0]
    lst[8][3], lst[5][3], lst[2][3], lst[11][3] = lst[5][3], lst[2][3], lst[11][3], lst[8][3]
    lst[7][3], lst[4][3], lst[1][3], lst[10][3] = lst[4][3], lst[1][3], lst[10][3], lst[7][3]
    lst[6][3], lst[3][3], lst[0][3], lst[9][3] = lst[3][3], lst[0][3], lst[9][3], lst[6][3]
    print("spin = L", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("L ")
    f.close()
    return lst

def rL(lst):
    time.sleep(0.07)
    lst[4][0], lst[5][1], lst[4][2], lst[3][1] = lst[3][1], lst[4][0], lst[5][1], lst[4][2]
    lst[5][0], lst[5][2], lst[3][2], lst[3][0] = lst[3][0], lst[5][0], lst[5][2], lst[3][2]
    lst[5][3], lst[2][3], lst[11][3], lst[8][3] = lst[8][3], lst[5][3], lst[2][3], lst[11][3]
    lst[4][3], lst[1][3], lst[10][3], lst[7][3] = lst[7][3], lst[4][3], lst[1][3], lst[10][3]
    lst[3][3], lst[0][3], lst[9][3], lst[6][3] = lst[6][3], lst[3][3], lst[0][3], lst[9][3]
    print("spin = rL", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("rL ")
    f.close()
    return lst

def R(lst):
    time.sleep(0.07)
    lst[3][7], lst[4][6], lst[5][7], lst[4][8] = lst[4][6], lst[5][7], lst[4][8], lst[3][7]
    lst[3][6], lst[5][6], lst[5][8], lst[3][8] = lst[5][6], lst[5][8], lst[3][8], lst[3][6]
    lst[6][5], lst[9][5], lst[0][5], lst[3][5] = lst[9][5], lst[0][5], lst[3][5], lst[6][5]
    lst[7][5], lst[10][5], lst[1][5], lst[4][5] = lst[10][5], lst[1][5], lst[4][5], lst[7][5]
    lst[8][5], lst[11][5], lst[2][5], lst[5][5] = lst[11][5], lst[2][5], lst[5][5], lst[8][5]
    print("spin = R", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("R ")
    f.close()
    return lst

def rR(lst):
    time.sleep(0.07)
    lst[4][6], lst[5][7], lst[4][8], lst[3][7] = lst[3][7], lst[4][6], lst[5][7], lst[4][8]
    lst[5][6], lst[5][8], lst[3][8], lst[3][6] = lst[3][6], lst[5][6], lst[5][8], lst[3][8]
    lst[9][5], lst[0][5], lst[3][5], lst[6][5] = lst[6][5], lst[9][5], lst[0][5], lst[3][5]
    lst[10][5], lst[1][5], lst[4][5], lst[7][5] = lst[7][5], lst[10][5], lst[1][5], lst[4][5]
    lst[11][5], lst[2][5], lst[5][5], lst[8][5] = lst[8][5], lst[11][5], lst[2][5], lst[5][5]
    print("spin = rR", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("rR ")
    f.close()
    return lst

def F(lst):
    time.sleep(0.07)
    lst[6][4], lst[7][3], lst[8][4], lst[7][5] = lst[7][3], lst[8][4], lst[7][5], lst[6][4]
    lst[6][3], lst[8][3], lst[8][5], lst[6][5] = lst[8][3], lst[8][5], lst[6][5], lst[6][3]
    lst[9][3], lst[5][8], lst[5][5], lst[5][2] = lst[5][8], lst[5][5], lst[5][2], lst[9][3]
    lst[9][4], lst[5][7], lst[5][4], lst[5][1] = lst[5][7], lst[5][4], lst[5][1], lst[9][4]
    lst[9][5], lst[5][6], lst[5][3], lst[5][0] = lst[5][6], lst[5][3], lst[5][0], lst[9][5]
    print("spin = F", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("F ")
    f.close()
    return lst

def rF(lst):
    time.sleep(0.07)
    lst[7][3], lst[8][4], lst[7][5], lst[6][4] = lst[6][4], lst[7][3], lst[8][4], lst[7][5]
    lst[8][3], lst[8][5], lst[6][5], lst[6][3] = lst[6][3], lst[8][3], lst[8][5], lst[6][5]
    lst[5][8], lst[5][5], lst[5][2], lst[9][3] = lst[9][3], lst[5][8], lst[5][5], lst[5][2]
    lst[5][7], lst[5][4], lst[5][1], lst[9][4] = lst[9][4], lst[5][7], lst[5][4], lst[5][1]
    lst[5][6], lst[5][3], lst[5][0], lst[9][5] = lst[9][5], lst[5][6], lst[5][3], lst[5][0]
    print("spin = rF", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("rF ")
    f.close()
    return lst

def B(lst):
    time.sleep(0.07)
    lst[0][4], lst[1][3], lst[2][4], lst[1][5] = lst[1][3], lst[2][4], lst[1][5], lst[0][4]
    lst[0][3], lst[2][3], lst[2][5], lst[0][5] = lst[2][3], lst[2][5], lst[0][5], lst[0][3]
    lst[3][3], lst[3][6], lst[11][5], lst[3][0] = lst[3][6], lst[11][5], lst[3][0], lst[3][3]
    lst[3][4], lst[3][7], lst[11][4], lst[3][1] = lst[3][7], lst[11][4], lst[3][1], lst[3][4]
    lst[3][5], lst[3][8], lst[11][3], lst[3][2] = lst[3][8], lst[11][3], lst[3][2], lst[3][5]
    print("spin = B", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("B ")
    f.close()
    return lst

def rB(lst):
    time.sleep(0.07)
    lst[1][3], lst[2][4], lst[1][5], lst[0][4] = lst[0][4], lst[1][3], lst[2][4], lst[1][5]
    lst[2][3], lst[2][5], lst[0][5], lst[0][3] = lst[0][3], lst[2][3], lst[2][5], lst[0][5]
    lst[3][6], lst[11][5], lst[3][0], lst[3][3] = lst[3][3], lst[3][6], lst[11][5], lst[3][0]
    lst[3][7], lst[11][4], lst[3][1], lst[3][4] = lst[3][4], lst[3][7], lst[11][4], lst[3][1]
    lst[3][8], lst[11][3], lst[3][2], lst[3][5] = lst[3][5], lst[3][8], lst[11][3], lst[3][2]
    print("spin = rB", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("rB ")
    f.close()
    return lst

def M(lst):
    time.sleep(0.07)
    lst[7][5], lst[3][7], lst[1][3], lst[5][1] = lst[3][7], lst[1][3], lst[5][1], lst[7][5]
    lst[7][4], lst[4][7], lst[1][4], lst[4][1] = lst[4][7], lst[1][4], lst[4][1], lst[7][4]
    lst[7][3], lst[5][7], lst[1][5], lst[3][1] = lst[5][7], lst[1][5], lst[3][1], lst[7][3]
    print("spin = M", end = "\n\n")
    f = open("solve.txt", 'a')
    f.write("M ")
    f.close()
    return lst
