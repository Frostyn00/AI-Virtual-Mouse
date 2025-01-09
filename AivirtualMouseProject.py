import cv2
import numpy as np
import HandTrackingModule as htm
import time
import pyautogui

wCam, hCam = 640, 480
frameR = 100
smoothening = 7

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
detector = htm.handDetector(maxHands=1)
wScr, hScr = pyautogui.size()

clickDone = False
rightClickDone = False

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:]  # Middle finger tip
        x3, y3 = lmList[4][1:]   # Thumb tip
        x4, y4 = lmList[20][1:]  # Pinky tip

        fingers = detector.fingersUp()

        if len(fingers) >= 5:
            if fingers[4] == 1 and not rightClickDone:  # Serçe parmak kalkık
                pyautogui.rightClick()
                rightClickDone = True

            if fingers[1] == 1 and fingers[2] == 0:
                x4 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                y4 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
                clocX = plocX + (x4 - plocX) / smoothening
                clocY = plocY + (y4 - plocY) / smoothening
                pyautogui.moveTo(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

            if fingers[1] == 1 and fingers[2] == 1:
                length, img, lineInfo = detector.findDistance(8, 12, img)
                if length < 20 and not clickDone:
                    pyautogui.click()
                    clickDone = True

            if fingers[1] == 1 and fingers[0] == 1:  # Thumb and Index finger up for scroll
                length, img, lineInfo = detector.findDistance(8, 4, img)
                if length <= 100:
                    pyautogui.scroll(100)
                elif length > 100:
                    pyautogui.scroll(-100)

        if fingers[1] == 0 or fingers[2] == 0:
            clickDone = False
        if fingers[4] == 0:
            rightClickDone = False

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
