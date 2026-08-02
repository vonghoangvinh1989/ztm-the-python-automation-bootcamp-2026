from pathlib import Path
import shutil

test_path = r'E:\LearningCourses\ZeroToMastery\ztm-the-python-automation-bootcamp\paths_and_folders\project\clean_sweep_example_folder'

# get user_input and validation
user_path = ''
while True:
    try:
        user_input = input('Please input your target directory path: ').strip()
        user_path = Path(user_input)

        if user_path.exists() and user_path.is_dir():
            break
        print('Your target directory path is not valid. Please enter a valid path.')
    except Exception as error:
        print(f'Error message: {error}')
        continue

# create a new folder within user_path
create_folder_path = user_path / 'closet'
if not create_folder_path.exists():
    print(f'--> Creating folder "closet"')
    create_folder_path.mkdir()
else:
    print(f'Folder "closet" already exists. No need to create.')

sub_directory_path_1 = create_folder_path / 'text_files'
sub_directory_path_2 = create_folder_path / 'csv_files'
sub_directory_path_3 = create_folder_path / 'folders'

if not sub_directory_path_1.exists():
    print(f'--> Creating folder "closet/text_files"')
    sub_directory_path_1.mkdir()
else:
    print(f'Folder "text_files" already exists. No need to create.')

if not sub_directory_path_2.exists():
    print(f'--> Creating folder "closet/csv_files"')
    sub_directory_path_2.mkdir()
else:
    print(f'Folder "csv_files" already exists. No need to create.')

if not sub_directory_path_3.exists():
    print(f'--> Creating folder "closet/folders"')
    sub_directory_path_3.mkdir()
else:
    print(f'Folder "folders" already exists. No need to create.')


for item in user_path.iterdir():
    if not item.name.strip().lower() == 'closet':
        # moving text files into text_files folder
        if item.is_file() and item.suffix == '.txt':
            text_file_des = sub_directory_path_1 / item.name
            if item.exists():
                print(f'--> Copying "{item.name}" into "closet/text_files/{item.name}"')
                shutil.move(item, text_file_des)

        # moving csv files into csv_files folder
        if item.is_file() and item.suffix == '.csv':
            csv_file_des = sub_directory_path_2 / item.name
            if item.exists():
                print(f'--> Copying "{item.name}" into "closet/csv_files/{item.name}"')
                shutil.move(item, csv_file_des)

        # delete directory with 'temp' in its name
        if item.is_dir() and "temp" in item.name:
            print(f'--> Deleting directory {item.name} has "temp" in its name')
            if item.exists():
                shutil.rmtree(item)

        # moving folders does not have 'temp' in its name
        if item.is_dir() and "temp" not in item.name:
            moving_folder_des = sub_directory_path_3 / item.name
            if item.exists():
                shutil.move(item, moving_folder_des)

        # moving remaining files into 'closet' directory
        if item.is_file():
            moving_file_des = create_folder_path / item.name
            if item.exists():
                shutil.move(item, moving_file_des)
print('--> Folder cleanup complete!')