import cv2
import numpy as np
import os

import time



face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(1)

sleep_counter = 0
threshold = 7   # frames (increase/decrease)

alarm_on = False   # alarm state

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye.detectMultiScale(roi_gray,1.1,4)

        # draw eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

        # -------- LOGIC ----------
        if len(eyes) >= 1:
            # Eyes open
            sleep_counter = 0

            if alarm_on:
                os.system("killall afplay")  # stop sound
                alarm_on = False

        else:
            # Eyes not detected
            sleep_counter += 1

            if sleep_counter > threshold:
                cv2.putText(frame, "WAKE UP DRIVER!", (50,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

                if not alarm_on:
                    os.system("afplay alarm.mp3 &")   # play your sound
                    alarm_on = True

            

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
