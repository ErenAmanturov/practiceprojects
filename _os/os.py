from pathlib import Path
BASE_DIR = Path(__file__).parent.parent.parent.parent

# path = input('Path where you want to see all the directories: ')
# dir_list = os.listdir(path)
# print(f'directories in {path}')
#
# for dir in dir_list:
#     print(dir)
# cwd = os.getcwd()
# while True:
#     file_to_delete = input('Which you want to delete in current directory: ')
#
#     path = os.path.join(cwd, file_to_delete)
#     try:
#         os.remove(path)
#     except FileNotFoundError:
#         print('File Does not exist')
"""
GLOBAL TODO:
1. JPG, PNG and JPEG in one folder
2. Add sorting by creation of file
3. Add dry-run to preview without actually moving files (70%)
    TODO:
    1. There is bug, when it's invalid choice it still goes through messages
    2. Fix that piece of shiiet called start()
    3. Find the different way of implementation
"""



def organize_files(directory: str, dry: bool):
    """
    Organizes the files depending on the extenstion
    """
    directory = BASE_DIR.joinpath(directory)
    directory = Path(directory).resolve()

    try:
        message= []
        for file in directory.iterdir():
            
            
            if file.is_file():
                file_extension = file.suffix # .pdf, .png etc
                if file_extension:
                    folder_name = file_extension[1:]
                else:
                    folder_name = 'Others' # for the ones which dont have extension

            # Creating the pathes(or paths) of folders and files
            folder_path = directory / folder_name
            new_file_path = folder_path / file.name

            if not dry:
                add = f'Moving {file.name} to {folder_name} folder {folder_name}'
                message.append(add) # i don't like the implementation of it
            else:
                # Creating the folder
                folder_path.mkdir(exist_ok=True)

                # Move the files into the created folders
                file.rename(new_file_path)
        
    except Exception as e:
        return f'Error while processing: {e}'
    return message if not dry else f'Files in {directory} has been organized'

def start():
    directory = input('Write the directory you want to organize: ')
    dry = input('Choose the mode (1 preview without touching files | 2 organizing): ')

    try:
        dry = int(dry)
        if dry not in [1, 2]:           # what the fuck is this
            print('Invalid choice')     # I don't like it 
            return None

        files = organize_files(directory=directory, dry=dry - 1)

        if not dry - 1 and type(files) == list:
            for file in files:
                print('-------------------------------')
                print(file)
        else:
            print(files)
    except ValueError:
        print('Invalid insertion')

if __name__ == '__main__':
   start() 
