import cv2
import mediapipe as mp

def preprocess_video(video_path):
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)
    cap = cv2.VideoCapture(video_path)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)
        
        # Aquí procesas los puntos clave
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                print(hand_landmarks)
        # Guardas las coordenadas clave o haces cualquier preprocesado adicional
        
    cap.release()