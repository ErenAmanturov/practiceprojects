import os
from pathlib import Path

from PIL import Image, ImageEnhance

BASE_DIR = Path(__file__).parent.parent
"""
TODO:
1. Need to fix the insertion of absolute path. Sometimes it just don't want to 
   find the directory

"""
def find_file(file_name:str, search_path:str):
    """
    Searches for the file in the written path
    """
    search_path = BASE_DIR.joinpath(search_path)
    for root, dirs, files, in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)

def darken_image(file_path, output_path, brighness=0.8):
    """
    darkens the image and saves it
    """
    try:
        image = Image.open(file_path)
        enchancer = ImageEnhance.Brightness(image)
        darkened_image = enchancer.enhance(brighness)

        darkened_image.save(BASE_DIR.joinpath(output_path))

        return f"Image is darkened by {brighness} and saved in: {output_path}"
    except Exception as e:
        return f'Error while proccesing {e}'

def start():
    try:
        brighness = input("Write the brighness \
                         (1 being normal 0 being \
                         black): (Example: 0.5) Default is 0.8  ")
        if float(brighness) > 1.0:
            return "You can not write higher than 1"
    except Exception as e:
        return f'error while proccesing {e}'
    file_name = input('Write the name of the file: ')
    search_path = input('Write the absolute path of directory\
                        where you want to search (Example: ~): ') 
    
    file = find_file(file_name=file_name, search_path=search_path)
    if file:
        print(file)
        output_path = input('Write the path where you want to save the file: ')
    else:
        return "File not found"
    image = darken_image(
        file_path=file, 
        output_path=output_path, 
        brighness=float(brighness)
    )
    return image
    
if __name__ == "__main__":
    print(start())
