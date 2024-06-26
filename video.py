import numpy as np
import cv2



cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xff == ord('q'):     # 按q退出
        break
    print(cap.isOpened())

cap.release()
cv2.destroyAllWindows()