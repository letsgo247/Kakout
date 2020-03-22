import pyautogui as pag
import keyboard, mss
import cv2 as cv
import numpy as np
import pyperclip

w,h = pag.size()
katok_pre = np.array([h,round(w/2),3])
content_pre = ""

while True:
    #마우스 위치 확인하는 코드
    x,y = pag.position()
    position_str = 'x:'+str(x) + ' y:'+str(y)
    print(position_str)

    scr = pag.screenshot()      #전체화면 스크린샷
    scr_np = np.array(scr)
    scr_np = scr_np[:,:,::-1].copy()      #X,Y는 놔두고 RGB -> BGR로 변환
    # print(h,w,t)
    katok = scr_np[:,round(w/2):,:]     #우측 카톡방 영역 선택
    # cv.imshow('Show', katok)


    if np.array_equal(katok, katok_pre):      #직전 채팅방 스샷과 비교
        continue

    else:           #뭔가 변화가 생겼을 경우, 알고리즘 시행
        pag.rightClick(1040,950)     #최신 말풍선에 우클릭
        pag.leftClick((1050,1000))      #'복사' 버튼 클릭

        content = pyperclip.paste()     #말풍선 내용 가져오기
        print(content)

        if content == content_pre:      #읽은사람 숫자만 바뀌었을 수 있으므로, 말풍선 내용도 비교
            continue
        else:                               #새로운 대화로 판별될 경우, 알고리즘 실행
            if '(하트)' or ('별') in content:
                profile_area = scr_np[130:970, 970:1020, :]     #마지막 말풍선을 보낸 프로필 아이콘 위치 탐색
                # cv.imshow('Show',profile_area)
                # cv.waitKey(0)
                profile_area_gray = cv.cvtColor(profile_area, cv.COLOR_BGR2GRAY)
                # cv.imshow('Show',profile_area_gray)
                # cv.waitKey(0)
                profile_area_edge = cv.Canny(profile_area_gray, 50, 150)
                # cv.imshow('Show',profile_area_edge)
                # cv.waitKey(0)

                retval, labels, stats, centroids = cv.connectedComponentsWithStats(profile_area_edge)
                cx = centroids[-1,0]
                cy = centroids[-1,1]
                px = 970+round(cx)
                py = 130+round(cy)
                # print(px,py)
                pag.click(px,py)        #프로필 클릭
                keyboard.wait('space')      #space 누를 때까지 대기


            katok_pre = katok       #다음 루프때 비교를 위해 pre에 저장
            cv.waitKey(0)

            if keyboard.is_pressed('esc'):
                break
            #
            # if cv.waitKey(1)&0xFF == 27:
            #     break

cv.destroyAllWindows()