import cv2
import mediapipe as mp
import serial

# Open serial connection to Arduino
ser = serial.Serial('/dev/cu.usbmodem101', 115200)

# Initialize MediaPipe FaceMesh
mp_face = mp.solutions.face_mesh.FaceMesh()
cap = cv2.VideoCapture(0)

# Landmarks for upper and lower lip
UP = 13
DOWN = 14

THRESH = 0.015  # Mouth open threshold

while True:
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = mp_face.process(rgb)

    if result.multi_face_landmarks:
        lm = result.multi_face_landmarks[0].landmark
        mouth_open = abs(lm[UP].y - lm[DOWN].y)

        # Check if mouth is open or closed and send to Arduino
        if mouth_open > THRESH:
            ser.write(b"OPEN\n")
            cv2.putText(frame, "OPEN", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            ser.write(b"CLOSE\n")
            cv2.putText(frame, "CLOSE", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the video feed
    cv2.imshow("Mouth Detector", frame)
    if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
        break

# Cleanup
cap.release()
ser.close()
cv2.destroyAllWindows()
