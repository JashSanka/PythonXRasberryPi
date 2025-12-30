import os

file_to_be_delete="delete.me"

if os.path.exists(file_to_be_delete):
    os.remove(file_to_be_delete)
else:
    print("The file does not exist, Bozo")

# delete folder
# os.rmdir("folder path")