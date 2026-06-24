import os
import shutil

base_path = r"C:\Users\DELL\Desktop\python internship\file organzer"

file_types = {
    "Images": ["jpg", "jpeg", "png", "gif", "bmp", "webp", "jfif"],
    "Videos": ["mp4", "avi", "mkv", "mov", "wmv"],
    "PDFs": ["pdf"],
    "Python": ["py"],
    "CSV": ["csv"],
    "Documents": ["doc", "docx", "txt"]
}

for folder in file_types:
    folder_path = os.path.join(base_path, folder)
    os.makedirs(folder_path, exist_ok=True)

files = [f for f in os.listdir(base_path) if os.path.isfile(os.path.join(base_path, f))]

for file in files:
    ext = os.path.splitext(file)[1].lower().strip(".")
    print(file, ext)

    for folder, extensions in file_types.items():
        if ext in extensions:
            src = os.path.join(base_path, file)
            dst = os.path.join(base_path, folder, file)

            if not os.path.exists(dst):
                shutil.move(src, dst)
                print(f"Moved: {file} -> {folder}")
            else:
                print(f"Skipped (already exists): {file}")
            break

print("Files successfully organized!")