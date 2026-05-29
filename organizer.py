import os
from datetime import datetime

def organize_files():
    print("\n--- File Organizer ---")
    folder = input("Enter folder path to organize (or press Enter for current): ") or "."
    
    try:
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        print(f"Found {len(files)} files.")
        
        for file in files:
            ext = file.split('.')[-1].lower() if '.' in file else "other"
            ext_folder = os.path.join(folder, ext.upper())
            os.makedirs(ext_folder, exist_ok=True)
            os.rename(os.path.join(folder, file), os.path.join(ext_folder, file))
            print(f"Moved: {file} → {ext.upper()}/")
            
        print("✅ Files organized successfully!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    organize_files()
