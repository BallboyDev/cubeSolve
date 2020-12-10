# r d r2 u' f' u r' l' f b' l' d2 u' r' u f2 u2 l2 r2 b' d' u d2 l' r

from move import spin, blueprint
from defPack import defPack
import os, sys, time

orders = {
    'INIT':defPack.init,
    'PRINT':defPack.printList,
    'SOLVE':defPack.solveCube,
    'USER':defPack.User,
    'EXIT':defPack.finish,
    'SAVE':defPack.saveCube,
    'CALL':defPack.calling
}



print("**************************************")
print("**                                  **")
print("**python을 이용한 큐브 해법 프로그램**")
print("**                                  **")
print("**************************************")

while(True):
    print('1. 로그인')
    print('2. 회원가입')
    status = input("===>>")

    if(status != '1' and status != '2'):
        print("1, 2중에서 선택해주세요")
    else:
        break

ID = input("ID : ")
PW = input("PW : ")

if(status == '1'):
    userInfo = open('./save/userInfo.txt', 'r').readlines()
elif(status == '2'):
    userInfo = open('./save/userInfo.txt', 'r')
    temp = len(userInfo.readlines())
    userInfo.close()
    userInfo = open('./save/userInfo.txt', 'a')
    userInfo.write(ID + " " + PW+"\n")
    name = input("닉네임을 입력해주세요 : ")
    os.system('mkdir .\\save\\'+str(temp))
    os.system("echo '' > .\\save\\"+str(temp)+"\\"+name)
    os.system("attrib +H .\\save\\"+str(temp)+"\\"+name)

    print("새로 로그인 해주세요")
    time.sleep(2)
    sys.exit()


index = 0
for info in userInfo:
    print(len(userInfo), index)
    if(info.find(ID + ' ' + PW) != -1):
        # user = os.popen('more .\\save\\'+str(index)+'\\saveData.txt')
        user = os.popen('dir /AH /B .\\save\\'+str(index))
            # result = os.popen('dir')
        # print(user)
        print(user.read().replace('\n','') + '님 반갑습니다.')
        memberDir = '.\\save\\'+str(index)+'\\'
        break

    if(index+1 == len(userInfo)):
        print('ID또는 PW가 잘못되었습니다.\n다시 확인하여 주세요')
        time.sleep(1.5)
        sys.exit()

    index = index + 1

a = blueprint.cube()
a.lst = defPack.makeInitLst(memberDir, a)

while True:
    order = input('Next command? ').upper().split()
    # print(order)
    for i in order:
        if(i in orders):
            # print(i)
            orders[i](memberDir, a)

        else:
            (a.lst, result) = spin.spin(a.lst, i)

            a.output(a.lst)
            print(result)
