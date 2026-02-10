import cv2
import numpy as np
import os
import time

face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(1)   # use 0 for Mac camera

sleep_counter = 0
threshold = 7
alarm_on = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)

    eye_closed = True  # assume closed initially

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye.detectMultiScale(roi_gray, scaleFactor=1.3, minNeighbors=6, minSize=(30,30))

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)

            eye_region = roi_gray[ey:ey+eh, ex:ex+ew]
            avg_intensity = np.mean(eye_region)

            # if eye bright -> open
            if avg_intensity > 70:
                eye_closed = False

    # -------- FINAL LOGIC ----------
    if not eye_closed:
        sleep_counter = 0

        if alarm_on:
            os.system("killall afplay")
            alarm_on = False

    else:
        sleep_counter += 1

        if sleep_counter > threshold:
            cv2.putText(frame, "WAKE UP DRIVER!", (50,50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

            if not alarm_on:
                os.system("afplay alarm.mp3 &")
                alarm_on = True

    cv2.imshow("Driver Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
