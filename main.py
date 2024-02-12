import os
import shutil
from extensions import *


def get_path():
    print('Please type the path to directory you want to clean: ')
    main_path = input('-->')
    if '"' in main_path:
        main_path = main_path[1:-1]
        return main_path
    else:
        return main_path
    
def create_folders(main_path):
    os.chdir(main_path)
    for folders in list_dir:
        if not os.path.exists(folders):
            os.mkdir(folders)
        else:
            continue

def del_empty_folders():
    for folders in list_dir:
        if len(os.listdir(folders)) == 0:
            shutil.rmtree(folders)
        else:
            continue

def move_files_extension(main_path, file_extension, sub_path):
    counter = 1
    for file in os.listdir(main_path):
        if any(file.endswith(extension)
            for extension in file_extension):
            destination_path = os.path.join(sub_path, file)
            while os.path.exists(destination_path):
                filename_parts = os.path.splitext(file)
                destination_path = os.path.join(sub_path, f"{filename_parts[0]} ({counter}){filename_parts[1]}")
                counter += 1
            shutil.move(os.path.join(main_path, file), destination_path)


def move_files_other(main_path, sub_path):
    counter = 1
    for file in os.listdir(main_path):
        if os.path.isfile(os.path.join(main_path, file)):
            destination_path = os.path.join(sub_path, file)
            while os.path.exists(destination_path):
                filename_parts = os.path.splitext(file)
                destination_path = os.path.join(sub_path, f"{filename_parts[0]} ({counter}){filename_parts[1]}")
                counter += 1
            shutil.move(os.path.join(main_path, file), destination_path)


def main():
    while True:
        try: 
            main_path = get_path()
            document_path = (rf"{main_path}\Documents")
            image_path = (rf"{main_path}\Image")
            audio_path = (rf"{main_path}\Music")
            video_path = (rf"{main_path}\Video")
            program_path = (rf"{main_path}\Programs")
            compressed_path = (rf'{main_path}\Compressed')
            other_path = (rf"{main_path}\Others")
            list_path = [image_path, video_path, audio_path, document_path, program_path, compressed_path]
            
            create_folders(main_path)
            counter = 0
            for _ in range(6):
                move_files_extension(main_path, list_extension[counter], list_path[counter])
                counter +=1
            move_files_other(main_path, other_path)
            del_empty_folders()
            exit()
        except Exception as e:
            print(f'Error Occurred: {e}')
    
if __name__ == '__main__':
    main()

