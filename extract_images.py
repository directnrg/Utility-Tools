import os
import shutil

DEFINED_ACTIONS= {'move': 'm','copy': 'c'}

def extract_files_from_directory(source_dir, dest_dir, file_extensions=None, action=None):
    """
    Extracts files from nested directories and moves them to a destination directory.

    :param source_dir: The root directory to start the search.
    :param dest_dir: The destination directory to move the files.
    :param file_extensions: A list of file extensions to filter. If None, all files are moved.
    """
    try:
        print(f"Checking existence of '{dest_dir}'...")
        if not os.path.exists(dest_dir):
            print(f"'{dest_dir}' does not exist. Creating...")
            os.makedirs(dest_dir)
        else:\
            print(f"'{dest_dir}' already exists. Files will be stored there.")
        
    except Exception as e:
        print(f"Error: {e}")     

    for foldername, subfolders, filenames in os.walk(source_dir):
        for filename in filenames:
            if file_extensions:
                if not any(filename.lower().endswith(ext.lower()) for ext in file_extensions):
                    continue

            source_path = os.path.join(foldername, filename)
            
            # Change the file extension to lowercase
            name, ext = os.path.splitext(filename)
            dest_path = os.path.join(dest_dir, f"{name}{ext.lower()}")

            # Handle potential name collisions by appending a number to the filename
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_dir, f"{name}_{counter}{ext.lower()}")
                counter += 1

            try:
                if action.lower() == DEFINED_ACTIONS.get('move'):
                    shutil.move(source_path, dest_path)
                    print(f"Moved {source_path} to {dest_path}")
                elif action.lower() == DEFINED_ACTIONS.get('copy'):
                    shutil.copy2(source_path, dest_path)
                    print(f"Copied {source_path} to {dest_path}")
            except Exception as e:
                print(f'Something happened. It was not possible to perform the action for {source_path} to {dest_path}. Error: {e}')

if __name__ == "__main__":
    SOURCE_DIRECTORY = input("Enter the source directory path: ")
    DESTINATION_DIRECTORY = input("Enter the destination directory path: ")
    ACTION = input("select if you want to copy or move media. Type c for copy and m for moving: ")
    

    # Supported extensions to be moved. Add more as needed: ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    FILE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp','.JPG','.MOV','.mov','.mp4','.MP4','.PNG']

    extract_files_from_directory(SOURCE_DIRECTORY, DESTINATION_DIRECTORY, FILE_EXTENSIONS, ACTION)
