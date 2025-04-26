from PIL import Image
import os
import piexif
import shutil

def inspect_and_move_problematic_images(directory):
    """
    Inspects images in the directory for potential issues and moves problematic images to a specific folder.

    :param directory: The directory to search for images.
    :return: A list of file paths of problematic images.
    """
    problematic_images = []
    error_folder = os.path.join(directory, "images_with_errors")

    # Create the error folder if it doesn't exist
    if not os.path.exists(error_folder):
        os.makedirs(error_folder)

    for foldername, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                filepath = os.path.join(foldername, filename)
                
                try:
                    # First, attempt to load the image
                    with Image.open(filepath) as img:
                        img.load()

                    # Check image dimensions
                    with Image.open(filepath) as img:
                        width, height = img.size
                        if width <= 0 or height <= 0:
                            problematic_images.append((filepath, "Invalid dimensions"))
                            shutil.move(filepath, os.path.join(error_folder, filename))
                            continue

                    # Check image metadata (EXIF data)
                    exif_data = piexif.load(filepath)
                    if not exif_data:
                        problematic_images.append((filepath, "Missing EXIF data"))
                        shutil.move(filepath, os.path.join(error_folder, filename))
                        continue

                except Exception as e:
                    problematic_images.append((filepath, f"Error processing: {e}"))
                    shutil.move(filepath, os.path.join(error_folder, filename))

    return problematic_images

if __name__ == "__main__":
    DIRECTORY = input("Enter the directory path to search for images: ")

    problematic_files = inspect_and_move_problematic_images(DIRECTORY)

    if problematic_files:
        print("\nProblematic images identified and moved to 'images_with_errors' folder:")
        for img, reason in problematic_files:
            print(f"{img} - {reason}")
    else:
        print("\nNo problematic images found.")
