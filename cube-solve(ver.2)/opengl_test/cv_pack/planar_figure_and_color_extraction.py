import cv2, copy
import numpy as np
from cv_pack import data
from cv_pack.package import trans, color


def main(lst, num):
    size = 50 #전개도의 사이즈 단위
    pot = copy.deepcopy(data.location)
    planar_mat = np.linspace(-1, -1, 108).reshape(9, 12)
    mat_x, mat_y = np.shape(planar_mat)

    if num == 1:
        print("1번 실행입니다. image")
        img_GOY = cv2.resize(cv2.imread('cv_pack/image/test7_1.jpg'), (600, 600), interpolation=cv2.INTER_AREA)
        img_BWR = cv2.resize(cv2.imread('cv_pack/image/test7_2.jpg'), (600, 600), interpolation=cv2.INTER_AREA)

    if num == 2:
        print("2번 실행입니다. camera")
        img_GOY = cv2.resize(cv2.imread('test_1.jpg'), (600, 600), interpolation=cv2.INTER_AREA)
        img_BWR = cv2.resize(cv2.imread('test_2.jpg'), (600, 600), interpolation=cv2.INTER_AREA)

    #cv2.imshow("GOY", img_GOY)
    #cv2.imshow("BWR", img_BWR)

    pos = copy.deepcopy(data.pos)
    pos_GOY, stat = trans.point_check(img_GOY, pos)
    pos = copy.deepcopy(data.pos)
    pos_BWR, stat = trans.point_check(img_BWR, pos)
    print("GOY : ", pos_GOY)
    print("BWR : ", pos_BWR)

    if stat == 1:
        trans_GOY = trans.perspective_trans(0, img_GOY, size * 3, pos_GOY)
        trans_BWR = trans.perspective_trans(0, img_BWR, size * 3, pos_BWR)

    if stat == 2:
        trans_GOY = trans.perspective_trans(1, img_GOY, size*3, pos_GOY)
        trans_BWR = trans.perspective_trans(2, img_BWR, size*3, pos_BWR)

    rows, cols = trans_GOY.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 180, 1)
    trans_GOY = cv2.warpAffine(trans_GOY, M, (cols, rows))

    planar_figure = np.hstack((trans_BWR, trans_GOY))

    for [x, y] in pot:
        planar_mat[x][y] = color.color_check(planar_figure, y * size + round(size/2), x * size + round(size/2))
        #cv2.circle(planar_figure, (y * size + round(size/2), x * size + round(size/2)), 3, (122, 122, 122), -1)

    cv2.imshow("final", planar_figure)

    print(planar_mat)
    planar_mat = color.mat_make(planar_mat, mat_x, mat_y)
    #print(planar_mat)
    color.output(planar_mat, mat_x, mat_y)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    for i in range(9):
        for j in range(9):
            lst[i][j] = planar_mat[i][j]

    for i in range(6, 9):
        for j in range(6, 9):
            lst[i][j] = ' '
    #print("test")

    for a, b, x, y in data.set:
        #print(set)
        lst[x][y] = planar_mat[a][b]

    #color.output(lst, 12, 9)


    return lst

#if __name__ == "__main__":
    #main()
