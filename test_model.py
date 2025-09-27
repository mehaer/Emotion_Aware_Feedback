import pickle
import cv2
from utils import get_face_landmarks

emotions = ['Happy', 'Sad', 'Surprised']

with open('./model', 'rb') as f:
    model = pickle.load(f)

cap = cv2.VideoCapture(1)
ret, frame = cap.read()

while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        print("⚠️ Frame capture failed")
        break

    face_landmarks = get_face_landmarks(frame, static_image_mode=False)

    if len(face_landmarks) != 1404:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue

    output = model.predict([face_landmarks])
    emotion_index = int(output[0])
    print(f"Predicted index: {emotion_index}")

    if 0 <= emotion_index < len(emotions):
        cv2.putText(frame, emotions[emotion_index], (10, frame.shape[0]-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# while ret:
#     ret, frame = cap.read()
#     face_landmarks = get_face_landmarks(frame, static_image_mode=False)

#     if len(face_landmarks) != 1404:
#         cv2.imshow('frame', frame)
#         cv2.waitKey(1)
#         continue

#     # output = model.predict([face_landmarks])
#     output = model.predict([face_landmarks])
#     emotion_index = int(output[0])
#     print(f"Predicted index: {emotion_index}")

if 0 <= emotion_index < len(emotions):
    cv2.putText(frame, emotions[emotion_index], (10, frame.shape[0]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

    emotion_index = int(output[0])

    cv2.putText(frame, emotions[emotion_index], (10, frame.shape[0]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    # cv2.waitKey(10)

# while ret:
#     ret, frame = cap.read()
#     face_landmarks = get_face_landmarks(frame, static_image_mode=False)
#     output = model.predict([face_landmarks])

#     cv2.putText(frame, emotions[int(output[0])], (10, frame.shape[0]-1), cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 5)

    print(output)
    cv2.imshow('frame', frame)
    cv2.waitKey(25)
cap.release()
cv2.destroyAllWindows()