import os
import shutil

def cleanup():
    folders = ["downloads", "vector_db"]

    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Deleted {folder}")