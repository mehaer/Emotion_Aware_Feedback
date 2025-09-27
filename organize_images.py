import os
import shutil

# Paths
source_root = '/Users/mehaerchhabda/PythonPlayground/DS_paper/archive (5)/images'  # Replace with your actual path
dest_root = 'organized_by_emotion'

# Create destination directory if it doesn't exist
os.makedirs(dest_root, exist_ok=True)

# Iterate through folders 0 to 18
for folder_name in os.listdir(source_root):
    folder_path = os.path.join(source_root, folder_name)
    if not os.path.isdir(folder_path):
        continue

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            continue
        
        emotion = os.path.splitext(filename)[0]  # Gets 'Angry' from 'Angry.jpg'
        emotion_folder = os.path.join(dest_root, emotion)
        os.makedirs(emotion_folder, exist_ok=True)

        # Create a unique filename
        new_filename = f"{folder_name}_{filename}"
        src_file = os.path.join(folder_path, filename)
        dst_file = os.path.join(emotion_folder, new_filename)

        shutil.copy(src_file, dst_file)  # Use move() if you want to relocate

print("Dataset restructured successfully!")
