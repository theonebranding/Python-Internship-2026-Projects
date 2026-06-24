from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

def bulk(path):
    
    record = 0
    duplicate = 0

    
    files = sorted(
    [file for file in path.rglob("*") if file.is_file()]
    )
     

    
    for file in files:
        name_offile = input("enter name")
        record += 1
        name = file.name
        new_name = file.with_name(f"{name_offile}_{record}{file.suffix}")

        if name == new_name.name:
            print(f"Skipped (already correct): {name}")
            continue

        counter = 1
        while new_name.exists():
            new_name = file.with_name(f"file_{record}_{counter}{file.suffix}")
            counter += 1

        file.rename(new_name)
        print(f"File renamed from {name} to: {new_name.name}")

    if record == 0:
        print("No files found.")
    else:
        print(f"{record} files processed successfully.")


       

while True:
    print()
    confirm = input("This will rename files only inside the 'input' folder. Continue? (y/n): ").strip().lower()
    print()


    if confirm == 'n':
        print("Cancelled.")
        break

    if confirm == 'y':
        path = input("Enter path: ")
        default_folder = BASE_DIR / path

        if default_folder.is_dir():
            print(f"Folder exists: {default_folder}")
            try:
                bulk(default_folder)
            except Exception as e:
                print(f"Error: {e}")
                continue
        else:
            print("Input folder is missing.")
            break
    else:
        print("Please choose a valid option (y/n).")