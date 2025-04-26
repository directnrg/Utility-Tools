# Utility Tools

A collection of Python scripts for file management and image processing.

## Scripts Overview

### 1. Extract Images (`extract_images.py`)

This script extracts image and video files from nested directories and moves or copies them to a destination directory.

**Features:**
- Extracts files with specific extensions (images and videos)
- Supports both moving and copying files
- Handles filename collisions by appending a counter
- Converts file extensions to lowercase for consistency
- Creates the destination directory if it doesn't exist

**Usage:**
```
python extract_images.py
```

You will be prompted to enter:
- Source directory path
- Destination directory path
- Action (copy or move) - type 'c' for copy or 'm' for move

**Supported file extensions:**
- Images: .jpg, .jpeg, .png, .gif, .bmp, .JPG, .PNG
- Videos: .MOV, .mov, .mp4, .MP4

### 2. Find Problematic Images (`find_problematic_images.py`)

This script inspects images in a directory for potential issues and moves problematic images to a separate folder.

**Features:**
- Checks for invalid image dimensions
- Verifies EXIF data presence
- Attempts to load images to detect corruption
- Moves problematic images to an "images_with_errors" subfolder
- Provides detailed error reporting

**Usage:**
```
python find_problematic_images.py
```

You will be prompted to enter:
- Directory path to search for images

**Supported file extensions:**
- .jpg, .jpeg, .png, .gif, .bmp

## Requirements

- Python 3.x
- PIL (Pillow) - for image processing
- piexif - for EXIF data handling

## Installation

1. Clone this repository
2. Install required packages:
   ```
   pip install Pillow piexif
   ```

## License

This project is open source and available under the MIT License. 

