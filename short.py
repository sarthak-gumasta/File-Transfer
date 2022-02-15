import os
import shutil

folders = {
    'videos': ['.mp4', '.gif', '.gifv', '.avi', '.mp4v', '.webm'],
    'audios': ['.wav', '.mp3', '.m4p'],
    'images': ['.jpg', '.png', '.raw', '.ai', '.psd'],
    'documents': ['.doc', '.xlsx', '.xls', '.pdf', '.zip', '.rar']
}
# Create rename function for already existing files.


def rename_folder():
    for folder in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, folder)) == True:
            os.rename(os.path.join(directory, folder),os.path.join(directory, folder.lower()))

# Create a function for transfering file by extention.


def create_move(ext, file_name):
    find = False
    for folder_name in folders:
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directory):
                # if there is no directory so this line will create one.
                os.mkdir(os.path.join(directory, folder_name))
            shutil.move(os.path.join(directory, file_name),
                        os.path.join(directory, folder_name))
            find = True
            break
    if find != True:
        if other_name not in os.listdir(directory):
            os.mkdir(os.path.join(directory, other_name))
        shutil.move(os.path.join(directory, file_name),
                    os.path.join(directory, other_name))


# Enter folder path for moving the files.
directory = input("Enter the Location:")
other_name = input("Enter the floder name for Unknown files:")
rename_folder()
all_files = os.listdir(directory)
length = len(all_files)
count = 1
# print all files.
for i in all_files:
    if os.path.isfile(os.path.join(directory, i)) == True:
        create_move(i.split(".")[-1], i)
print(f"Total Files: {length}| Done:c{count} | Left: {length-count}")
count += 1
