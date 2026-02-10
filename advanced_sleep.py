import cv2
import mediapipe as mp
import numpy as np
import os
from scipy.spatial import distance

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

def eye_aspect_ratio(eye_points, facial_landmarks):
    p1 = facial_landmarks[eye_points[1]]
    p2 = facial_landmarks[eye_points[5]]
    p3 = facial_landmarks[eye_points[2]]
    p4 = facial_landmarks[eye_points[4]]
    p5 = facial_landmarks[eye_points[0]]
    p6 = facial_landmarks[eye_points[3]]

    vertical1 = distance.euclidean(p1, p2)
    vertical2 = distance.euclidean(p3, p4)
    horizontal = distance.euclidean(p5, p6)

    ear = (vertical1 + vertical2) / (2.0 * horizontal)
    return ear

cap = cv2.VideoCapture(1)

sleep_counter = 0
threshold_frames = 20
EAR_THRESHOLD = 0.22
alarm_on = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = frame.shape
            landmarks = []

            for lm in face_landmarks.landmark:
                x, y = int(lm.x * w), int(lm.y * h)
                landmarks.append((x, y))

            leftEAR = eye_aspect_ratio(LEFT_EYE, landmarks)
            rightEAR = eye_aspect_ratio(RIGHT_EYE, landmarks)
            ear = (leftEAR + rightEAR) / 2.0

            cv2.putText(frame, f"EAR: {ear:.2f}", (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            if ear < EAR_THRESHOLD:
                sleep_counter += 1

                if sleep_counter > threshold_frames:
                    cv2.putText(frame, "UTH JAA BKL!", (200,100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 3)

                    if not alarm_on:
                        os.system("afplay alarm.mp3 &")
                        alarm_on = True
            else:
                sleep_counter = 0
                if alarm_on:
                    os.system("killall afplay")
                    alarm_on = False

    cv2.imshow("AI Drowsiness Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
