import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7) as hands:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw landmarks and connections
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                # Draw lines across fingers (between tips)
                tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Pinky
                for i in range(len(tips)-1):
                    x1 = int(hand_landmarks.landmark[tips[i]].x * image.shape[1])
                    y1 = int(hand_landmarks.landmark[tips[i]].y * image.shape[0])
                    x2 = int(hand_landmarks.landmark[tips[i+1]].x * image.shape[1])
                    y2 = int(hand_landmarks.landmark[tips[i+1]].y * image.shape[0])
                    cv2.line(image, (x1, y1), (x2, y2), (0,255,0), 3)

        cv2.imshow('Hand Tracking', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
