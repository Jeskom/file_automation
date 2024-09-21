import os
import shutil

#Change directories according to your operating system and username
SOURCE_DIR = "/Users/[username]/Downloads"
DOCUMENTS_DIR = "/Users/[username]/Documents"
PICTURES_DIR = "/Users/[username]/Pictures"
MOVIES_DIR = "/Users/[username]/Movies"

document_index = '.doc', '.docx', '.pdf', '.txt', '.odt', '.rtf', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.ods', '.odp', '.md', '.epub', '.pages'
picture_index = '.jpeg', '.jpg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg', '.heif', '.heic', '.webp', '.raw', '.cr2', '.nef', '.arw', '.orf', '.dng', '.rw2'
movies_index = '.mp4', '.mov', '.wmv', '.avi', '.mkv', '.flv', '.mpeg', '.mpg', '.m4v', '.webm', '.3gp'

def sorted_directory(directory):
    items = os.listdir(directory)
    sorted_items = sorted(items)
    return sorted_items

sorted_list = sorted_directory(SOURCE_DIR)
sorted_list = sorted_list[2:]

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

file_mover(sorted_list)
