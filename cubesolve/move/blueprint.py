import time, os
from graphic import graphic

class cube:
    lst = []
    
    def output(self, lst):
        #graphic.image()
        os.system('cls')
        for i in range(12):
            for j in range(9):
                print(lst[i][j], end = ' ')
            print()
        print(time.asctime(time.localtime(time.time())))
