from data import initlst
from move import blueprint
from solve import solve
from datetime import datetime
import copy, os, sys, time


solution = {0:solve.first1, 1:solve.first2, 2:solve.second, 3:solve.third, 4:solve.fourth, 5:solve.fifth,
            6:solve.sixth, 7:solve.seventh}

def init(memberDir, a):
    # print('init()')
    temp = copy.deepcopy(initlst.lst)
    # a.output(temp)
    return temp

def printList(memberDir, a):
    # print('printList()')
    print(a.output(a.lst))

def solveCube(memberDir, a):
    # print('solve()')
    for i in range(8):
        solution[i](a)
        a.output(a.lst)

def User(memberDir, a):
    # print('user()')
    userInfo = open('./save/userInfo.txt', 'r')
    info = userInfo.readlines()
    for i in info:
        print(i)

def calling(memberDir, a):
    print('calling()')

def finish(memberDir, a):

    print('bye~ bye~')
    time.sleep(1.5)
    sys.exit()

def saveCube(memberDir, a):
    # print('save()')
    print("파일이름을 입력하여 주세요\n미입력시 현재 시간으로 저장이 됩니다.")
    filename = input("파일 이름 : ")

    if(filename == ''):
        now = datetime.now()
        
        filename = str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'_'+str(now.hour)+'_'+str(now.minute)
    
    f = open(memberDir + filename+'.txt', 'w')
    for i in range(12):
        for j in range(9):
            # print(lst[i][j], end = ' ')
            f.write(a.lst[i][j])
            if(j != 8):
                f.write(',')
        f.write('\n')

def makeInitLst(memberDir, a):
#     print(memberDir)
    datas = os.popen('dir /B '+memberDir).readlines()

#     print("datas : ", datas)

    if(datas != []):
        for index, data in enumerate(datas, 0):
            print(str(index) + " : " + data.replace('.txt\n', ''))

        number = int(input('불러올 데이터 : '))
        temp = []
        initLst = os.popen('more '+memberDir+'"'+datas[number].replace('\n','')+'"').readlines()
        for lst in initLst:
            temp.append(lst.replace('\n','').replace('#',' ').split(','))

    elif(datas == []):
        print('데이터가 없습니다.\n큐브를 새로 생성합니다.')
        temp = init(memberDir, a)

    # print(temp)
    return copy.deepcopy(temp)