import os
import shutil
import time

SOURCE_DIR = "/Users/jonok/Downloads"
DOCUMENTS_DIR = "/Users/jonok/Documents"
PICTURES_DIR = "/Users/jonok/Pictures"
MOVIES_DIR = "/Users/jonok/Movies"

document_index = '.doc', '.docx', '.pdf', '.txt', '.odt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.ods', '.odp', '.md', '.epub', '.pages'
picture_index = '.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg', '.heif', '.heic', '.webp', '.raw', '.cr2', '.nef', '.arw', '.orf', '.dng', '.rw2'
movies_index = '.mp4', '.mov', '.wmv', '.avi', '.mkv', '.flv', '.mpeg', '.mpg', '.m4v', '.webm', '.3gp'

#Gets the files from the directory
def sorted_directory(directory):
    items = os.listdir(directory)
    sorted_items = sorted(items)
    return sorted_items

#Sorts the files and hides the 2 system files
def sorting():
    sorted_list = sorted_directory(SOURCE_DIR)
    sorted_list = sorted_list[2:]
    return sorted_list

#Moves the files
def file_mover(file):
    for fname in file:
        if fname.lower().endswith(document_index):
            shutil.move(os.path.join(SOURCE_DIR, fname), DOCUMENTS_DIR)
            print(f"{fname} has been moved to {DOCUMENTS_DIR}")
        elif fname.lower().endswith(picture_index):
            shutil.move(os.path.join(SOURCE_DIR, fname), PICTURES_DIR)
            print(f"{fname} has been moved to {PICTURES_DIR}")
        elif fname.lower().endswith(movies_index):
            shutil.move(os.path.join(SOURCE_DIR, fname), MOVIES_DIR)
            print(f"{fname} has been moved to {MOVIES_DIR}")
    return True

#Runs the program
def main():
    while True:
        file_mover(sorting())
        time.sleep(600)

main()