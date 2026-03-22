import cv2
import mediapipe as mp
from pythonosc import udp_client

# --- Configuration ---
WEKINATOR_IP = "127.0.0.1"
WEKINATOR_PORT = 6448
OSC_PATH = "/wek/inputs"

client = udp_client.SimpleUDPClient(WEKINATOR_IP, WEKINATOR_PORT)
mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Mirror the frame
        frame = cv2.flip(frame, 1)

        # Convert to RGB for MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(frame_rgb)
        h, w, _ = frame.shape

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0]
            nose = landmarks.landmark[1]
            x, y = nose.x, nose.y

            # Send nose position to Wekinator via OSC
            client.send_message(OSC_PATH, [x, y])

            # Draw the nose tip and display coordinates
            cx, cy = int(x * w), int(y * h)
            cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
            cv2.putText(frame, f"x={x:.2f}, y={y:.2f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Show output window
        cv2.imshow("Face to Wekinator (Mirror)", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # Press ESC to exit
            break

cap.release()
cv2.destroyAllWindows()
