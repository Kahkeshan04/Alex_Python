import os, shutil

# Path in which all types of files are present
path = r'D:\DA\File Transfer Python Code Exp/'

# Saving all the name of the files present in the path. It will get stored in the form of List
file_names=os.listdir(path)

# Saving the extensions. It will be used to compare with the file name and move it to the respective folder
file_extensions = [os.path.splitext(file_name)[1] for file_name in file_names]

# Saving the extensions without '.' for folder names. Making 1st letter capital.
extension_name = [ext[1:].capitalize()+ ' Files' for ext in file_extensions]
# Just to check 
print(file_extensions)

# Loop to get the value or folder name from extension_name[loop] (ex: py files, txt files, etc.,)
for loop in range(0,len(extension_name)):
    # Check whether the folder exists or not. If it does not exist then create the folder/dir
    if not os.path.exists(path + extension_name[loop]):
        # Just to check 
        print(path + extension_name[loop])
        # Creating the folder or dir in the given path with the given name 
        # (ex: D:\DA\File Transfer Python Code Exp/py files -> path/extension_name[loop])
        os.makedirs(path + extension_name[loop])

# Iterating over three lists simultaneously using zip
# zip(file_extensions, extension_names) pairs up corresponding elements from file_extensions and extension_names.
# The for ext, name in zip(...) loop then iterates over these pairs.
# file: The current file name.
# extensions: The corresponding file extension with the dot.
# name: The modified extension without the dot and with ' files' suffix.
for file, extensions, name  in zip(file_names, file_extensions, extension_name):

    # Checks if the current file has the corresponding extension.
    # Checks if a directory with the extension_name (name) exists in the specified path.
    # If both conditions are met, it proceeds to the next step.
    if extensions in file and not os.path.exists(path + name + '/' + file):

        # Moves the file to a subdirectory named with the extension_name and ' files' suffix.
        shutil.move(path + file, path + name + '/' + file)

