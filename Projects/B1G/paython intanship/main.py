
from pathlib import Path
import shutil

BASE_DIR = Path(__file__).resolve().parent

def analyzer(path):
    total_file = 0
    total_size = 0

    for file in path.rglob('*'):
        file = Path(file)
        if file.is_file():
            total_file+=1
            total_size+= file.stat().st_size

    size = total_size
    units = ["Bytes", "KB", "MB", "GB", "TB"]
    index = 0

    while size >=1024 and index <= len(units) - 1:
        size /= 1024
        index += 1

    if index == 0: #ops
        print(f"folder name: {path.name}")
        print(f"Total files: {total_file}")
        print(f"Total size: {int(size)},{units[index]}")
    else:
        print(f"Folder name: {path.name}")
        print(f"Total files: {total_file}")
        print(f"Total size: {size: 2},{units[index]}")               





    output_dir = BASE_DIR / "output"
    if output_dir.exists():
        confirm = input("output folder exists, Delete and continue [y/n]:").strip().lower()

        if confirm!= "y":
            print("cancelled!")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)    
    

while True:
    print()
    path = input("Enter full folder path (or 'q' for quite):").strip()
    print()

    default_folder = BASE_DIR / "input"

    if path.lower() == "q":
        break

    if not path:
        Path = default_folder

        if path.is_dir():
            print(f"No path provide - using default folder {path.name}")
        else:
            print("No path provided and default file is missing!")
            continue
    else:
        path = Path(path)

        if not path.is_dir():
            print("No folder found!")
            continue

    try:
        analyzer(path)
    except Exception as e:
         print(f"Error:{e}")

            
