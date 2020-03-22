import pyautogui as pag
import keyboard

#마우스 위치 반환해주는 알고리즘

while True:
    x,y = pag.position()
    position_str = 'x:'+str(x) + ' y:'+str(y)
    print(position_str)

    if keyboard.is_pressed('esc'):
        break

