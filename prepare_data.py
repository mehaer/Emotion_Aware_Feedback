# import os
# import cv2
# import numpy as np
# from utils import get_face_landmarks

# data_dir = '/Users/mehaerchhabda/PythonPlayground/DS_paper/organized_by_emotion'

# output = []
# # for emotion_index, emotion in enumerate(sorted(os.listdir(data_dir))):
# #     emotion_path = os.path.join(data_dir, emotion)
# emotions = ['Happy', 'Sad', 'Surprised']
# for emotion_index, emotion in enumerate(emotions):
#     emotion_path = os.path.join(data_dir, emotion)

#     # Skip files that are not directories
#     if not os.path.isdir(emotion_path):
#         continue

#     for image_path_ in os.listdir(emotion_path):
#         image_path = os.path.join(emotion_path, image_path_)
#         image = cv2.imread(image_path)

#         if image is None:
#             print(f"Failed to read {image_path}")
#             continue

#         face_landmarks = get_face_landmarks(image)

#         if len(face_landmarks) == 1404:
#             face_landmarks.append(int(emotion_index))
#             output.append(face_landmarks)
# np.savetxt('data.txt', np.asarray(output))


import os
import cv2
import numpy as np
from utils import get_face_landmarks

data_dir = '/Users/mehaerchhabda/PythonPlayground/DS_paper/organized_by_emotion'

output = []
emotions = ['Happy', 'Sad', 'Surprised']  # Define fixed list

def augment_image(image):
    augmented_images = []
    
    # Original
    augmented_images.append(image)
    
    # Horizontal flip
    augmented_images.append(cv2.flip(image, 1))
    
    # Slight rotation
    rows, cols, _ = image.shape
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 10, 1)  # rotate 10 degrees
    rotated = cv2.warpAffine(image, M, (cols, rows))
    augmented_images.append(rotated)
    
    # Brightness increase
    brighter = cv2.convertScaleAbs(image, alpha=1.2, beta=30)
    augmented_images.append(brighter)
    
    return augmented_images

for emotion_index, emotion in enumerate(emotions):
    emotion_path = os.path.join(data_dir, emotion)
    if not os.path.isdir(emotion_path):
        continue

    for image_path_ in os.listdir(emotion_path):
        image_path = os.path.join(emotion_path, image_path_)
        image = cv2.imread(image_path)

        if image is None:
            print(f"Failed to read {image_path}")
            continue
        
        # Augment the image
        augmented_versions = augment_image(image)

        for aug_img in augmented_versions:
            face_landmarks = get_face_landmarks(aug_img)

            if len(face_landmarks) == 1404:
                face_landmarks.append(int(emotion_index))
                output.append(face_landmarks)

np.savetxt('data.txt', np.asarray(output))
