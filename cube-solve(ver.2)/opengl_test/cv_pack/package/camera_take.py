import cv2

def capture(num):
    camid = 0
    cam = cv2.VideoCapture(camid)
    if cam.isOpened() == False:
        print('cant open the cam (%d)' % camid)
        return None

    ret, frame = cam.read()
    if frame is None:
        print('frame is not exist')
        return None

    # jpg로 압축 없이 영상 저장
    name = "test_" + str(num) + ".jpg"
    print(name)
    cv2.imwrite(name, frame, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
    cam.release()

    print("test")