import pyautogui as pag
import keyboard, mss
import cv2 as cv
import numpy as np
from PIL import ImageGrab

while True:
    x,y = pag.position()
    position_str = 'x:'+str(x) + ' y:'+str(y)
    print(position_str)

    screen = pag.screenshot()
    screen_np = np.array(screen)
    screen_np = screen_np[:,:,::-1].copy()
    # screen = ImageGrab.grab()
    # screen_numpy = np.array(screen, dtype='uint8').reshape((1920,1080,3))
    # screen_part = screen_np[:100,:100]
    # screen.show()

    # screen.save('1.png')
    # screen = np.array(screen)
    cv.imshow('screen', screen_np)






    # screen_pos = {'left':0, 'top':0, 'width':1920, 'height':1280}
    #
    # with mss.mss() as sct:
    #     screen = np.array(sct.grab(screen_pos))[:,:,:3]
    #
    #     cv.imshow('screen', screen)

    # cv.waitKey(0)
    #
    # if keyboard.is_pressed('esc'):
    #     break

    if cv.waitKey(1)&0xFF == 27:
        break

cv.destroyAllWindows()