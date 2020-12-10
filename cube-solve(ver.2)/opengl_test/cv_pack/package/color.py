import numpy as np
import cv2

def color_check(img, x, y):
    color = img[y, x]

    one_pixel = np.uint8([[color]])
    hsv = cv2.cvtColor(one_pixel, cv2.COLOR_BGR2HSV)[0][0]

    if hsv[0] < 10:
        # print("case1")
        lower_mask1 = np.array([hsv[0] - 10 + 180, 30, 30])
        upper_mask1 = np.array([180, 255, 255])
        lower_mask2 = np.array([0, 30, 30])
        upper_mask2 = np.array([hsv[0], 255, 255])
        lower_mask3 = np.array([hsv[0], 30, 30])
        upper_mask3 = np.array([hsv[0] + 10, 255, 255])
        #     print(i-10+180, 180, 0, i)
        #     print(i, i+10)

    elif hsv[0] > 170:
        # print("case2")
        lower_mask1 = np.array([hsv[0], 30, 30])
        upper_mask1 = np.array([180, 255, 255])
        lower_mask2 = np.array([0, 30, 30])
        upper_mask2 = np.array([hsv[0] + 10 - 180, 255, 255])
        lower_mask3 = np.array([hsv[0] - 10, 30, 30])
        upper_mask3 = np.array([hsv[0], 255, 255])
        #     print(i, 180, 0, i+10-180)
        #     print(i-10, i)
    else:
        # print("case3")
        lower_mask1 = np.array([hsv[0], 30, 30])
        upper_mask1 = np.array([hsv[0] + 10, 255, 255])
        lower_mask2 = np.array([hsv[0] - 10, 30, 30])
        upper_mask2 = np.array([hsv[0], 255, 255])
        lower_mask3 = np.array([hsv[0] - 10, 30, 30])
        upper_mask3 = np.array([hsv[0], 255, 255])
        #     print(i, i+10)
        #     print(i-10, i)
    return hsv[0]


def mat_make(mat, x, y):
    mat_color = ([["", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", "", "", "", "", ""]])
    for i in range(x):
        for j in range(y):
            if (mat[i][j] == -1):  # blank
                mat_color[i][j] = " "

            elif (4 <= mat[i][j] and mat[i][j] <= 20):  # Orange
                mat_color[i][j] = "O"

            elif (21 <= mat[i][j] and mat[i][j] <= 40):  # Yellow
                mat_color[i][j] = "Y"

            elif (45 <= mat[i][j] and mat[i][j] <= 88):  # Green
                mat_color[i][j] = "G"

            elif (90 <= mat[i][j] and mat[i][j] <= 115):  # Blue
                mat_color[i][j] = "B"

            elif (120 <= mat[i][j] and mat[i][j] <= 160):  # Purple
                mat_color[i][j] = "P"

            elif (170 <= mat[i][j] or mat[i][j] <= 3):  # Red
                mat_color[i][j] = "R"

            else:
                mat_color[i][j] = "W"
    return mat_color

def output(mat, x, y):
    # os.system('cls')
    for i in range(x):
        for j in range(y):
            print(mat[i][j], end=' ')
        print()
    #print(time.asctime(time.localtime(time.time())))


