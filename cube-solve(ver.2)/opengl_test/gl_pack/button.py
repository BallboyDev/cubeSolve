from gl_pack.move import *
from main import *
import main
import copy

def test():
    print("button test입니다.")
    main.lst = copy.deepcopy(U(main.lst))



def control(inc_x, inc_y, accum, zoom, lst):

    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                inc_x = pi / 100
            if event.key == pygame.K_DOWN:
                inc_x = -pi / 100

            if event.key == pygame.K_LEFT:
                inc_y = pi / 100

            if event.key == pygame.K_RIGHT:
                inc_y = -pi / 100

            if event.key == pygame.K_SPACE:
                inc_x = 0
                inc_y = 0
                accum = (0, 1, 0, 0)
                zoom = 1

            if event.key == pygame.K_u:
                print("test_u")
                lst = U(lst)
            if event.key == pygame.K_d:
                print("test_d")
                lst = D(lst)
            if event.key == pygame.K_r:
                print("test_r")
                lst = R(lst)
            if event.key == pygame.K_l:
                print("test_l")
                lst = L(lst)
            if event.key == pygame.K_f:
                print("test_f")
                lst = F(lst)
            if event.key == pygame.K_b:
                print("test_b")
                lst = B(lst)
            if event.key == pygame.K_m:
                print("test_M")
                lst = M(lst)

        if event.type == pygame.KEYUP:
            # Stoping rotation
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                inc_x = 0.0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                inc_y = 0.0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if zoom < 1.6:
                    zoom += 0.05
                # print('scroll up', zoom)

        if event.type == pygame.MOUSEBUTTONUP:
            # Increase scale (zoom) value
            if event.button == 5:
                if zoom > 0.2:
                    zoom -= 0.05
                # print('scroll down', zoom)
    return [inc_x, inc_y, accum, zoom, lst]

