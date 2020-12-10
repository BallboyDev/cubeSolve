import cv2
import numpy as np
from cv_pack.package import matrix


def perspective_trans(num, img, length = 150, pos = ()):
    if num == 1:
        pos = [[97, 221], [269, 156], [298, 297], [460, 207], [115, 432], [291, 550], [446, 420]]
    if num == 2:
        pos = [[73, 169], [254, 93], [274, 269], [439, 171], [99, 363], [262, 481], [410, 363]]

    u_side1 = np.float32([[pos[0][0], pos[0][1]], [pos[1][0], pos[1][1]], [pos[2][0], pos[2][1]], [pos[3][0], pos[3][1]]])
    r_side1 = np.float32([[pos[0][0], pos[0][1]], [pos[2][0], pos[2][1]], [pos[4][0], pos[4][1]], [pos[5][0], pos[5][1]]])
    f_side1 = np.float32([[pos[2][0], pos[2][1]], [pos[3][0], pos[3][1]], [pos[5][0], pos[5][1]], [pos[6][0], pos[6][1]]])

    u_side2 = np.float32([[0, 0], [length, 0], [0, length], [length, length]])
    r_side2 = np.float32([[0, 0], [length, 0], [0, length], [length, length]])
    f_side2 = np.float32([[0, 0], [length, 0], [0, length], [length, length]])

    M1 = cv2.getPerspectiveTransform(u_side1, u_side2)
    M2 = cv2.getPerspectiveTransform(r_side1, r_side2)
    M3 = cv2.getPerspectiveTransform(f_side1, f_side2)

    dst1 = cv2.warpPerspective(img, M1, (length, length))
    dst2 = cv2.warpPerspective(img, M2, (length, length))
    dst3 = cv2.warpPerspective(img, M3, (length, length))

    img_blank = matrix.blank_mat(length, length)

    mat02 = np.vstack((img_blank, dst2, img_blank))
    mat13 = np.vstack((dst1, dst3, img_blank))
    result = np.hstack((mat02, mat13))
    return result


num = 0
def point_check(img, pos):
    print(pos)

    def onMouse(event, x, y, flags, param):
        global num
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(param, (x, y), 5, (0, 0, 255), 2)
            pos[num] = [x, y]
            print(pos[num])
            if num < 6:
                num = num + 1
            else:
                num = 0

    cv2.namedWindow('paint')
    cv2.setMouseCallback('paint', onMouse, param=img)
    stat = 0
    while (True):
        cv2.imshow('paint', img)
        if cv2.waitKey(1) & 0xFF == 27:
            stat = 1
            print("test1")
            break
        if cv2.waitKey(1) & 0xFF == 13:
            stat = 2
            print("test2")
            break

    cv2.destroyAllWindows()
    return pos, stat
