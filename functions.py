import os
from interface import success,error,info


# Helper Functions - Caleb
# this helps us check if the file exists beforehand
def file_exists(path):
    return os.path.isfile(path)

# this helps us check if the folder exists beforehand
def folder_exists(path):
    return os.path.isdir(path)

# simple utility to know our current folder we are in
def gwd(params):
    success(os.getcwd())

# get all files in the current folder
def get_files():
    return os.listdir(os.getcwd())

# a simple helper function to read file contents into a string for search
def read_files_into_str(filename):
    with open(filename,'r',encoding="utf-8") as f:
        contents = f.read()
    return contents


# a simple helper to confirm actions
def action_prompt():
    confirm = input("ARE YOU SURE YOU WANT TO COMPLETE THIS ACTION Y/N?: ")
    if confirm.lower() == "y":
        return True
    else:
        return False

# using recursion to delete folder and files in it
def delete_folder_recursive(folder):
    for item in os.listdir(folder):
        path = os.path.join(folder, item)

        if os.path.isfile(path):
            os.remove(path)

        elif os.path.isdir(path):
            delete_folder_recursive(path)

    os.rmdir(folder)


# Command functions for cli tool - Hakim

## peek function, allows you to look at the first n lines in a file, prints the first n lines in the console
def peek(params):
    if len(params) < 2:
        info("Usage: peek <filename> <number_of_lines>")
        return
    filename = params[0]
    number_of_lines = int(params[1])

    # first check if the file exists using our custom util function
    if file_exists(filename):
        with open(filename, "r",encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[:number_of_lines]:
                print(line, end="")
                success()
    else:
        error("This file does not exist!")

# find a certain string in a text file, returns if the word can be found and the line it is in
def find_x_in(params):
    if len(params) < 2:
        info("Usage: find_x_in <filename> <word to find>")
        return
    filename = params[0]
    word_to_find = params[1].strip('"')
    if file_exists(filename):
        with open(filename, "r",encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                line_num = lines.index(line)+1
                if word_to_find in line:
                    success(f"Results Found on line {line_num} in {filename}")
                    success(line.strip())
                    break
    else:
        error("This file does not exist!")

# swap the contents of two files
def swap_contents(params):
    if len(params) < 2:
        info("Usage: swap <file1> <file2>")
        return
    file1 = params[0].strip('"')
    file2 = params[1].strip('"')

    if file_exists(file1) and file_exists(file2):
        with open(file1, "rb") as f1:
            data1 = f1.read()
        with open(file2, "rb") as f2:
            data2 = f2.read()

        # Write swapped contents
        with open(file1, "wb") as f1:
            f1.write(data2)
        with open(file2, "wb") as f2:
            f2.write(data1)
    else:
        error("File does not exist!")
    

# this gives us all the metadata information about a file in the current directory
def fmeta(params):
    if len(params) < 1:
        info("Usage: fmeta <filename>")
        return
    filename = params[0].strip('"')
    if file_exists(filename):
        stats = os.stat(filename)
        success("File:", filename)
        success("Size:", stats.st_size, "bytes")
        success("Extension:", os.path.splitext(filename)[1])
        success("Absolute Path:", os.path.abspath(filename))
    else:
        error("File does not exist!")



# jump is our way of doing change directory
def jump(params):
    if len(params) < 1:
        info("Usage: jump <path>")
        return
    path = params[0]

    # Check if the folder exists
    if folder_exists(path):
        os.chdir(path)
        success(f"Changed directory to: {os.getcwd()}")
    else:
        error("Folder does not exist!")

# close our wonderful program
def exit():
    pass

# permanently delete file
def pdelete(params):
    if len(params) < 2:
        info("Usage: pdelete -f <file> | pdelete -d <folder>")
        return
    
    flag = params[0]
    target = params[1]

    # Delete a file
    if flag == "-f":
        if file_exists(target):
            if action_prompt():
                os.remove(target)
                success(f"File permanently deleted: {target}")
        else:
            error("file does not exist! ")

    # Delete a directory manually using recursion
    elif flag == "-d":
        if folder_exists(target):
            if action_prompt():
                delete_folder_recursive(target)
                success(f"Folder permanently deleted: {target}")
        else:
            error("folder does not exists")

    else:
        error("Unknown flag: ", flag)


def clean():
    print("\n" * 100)

def create_folder(params):
    if len(params) < 1:
        info("Usage: create_folder <foldername>")
        return

    folder = params[0]

    if folder_exists(folder):
        error(f"Folder already exists!: {folder}")
        return

    os.makedirs(folder)
    success(f"Folder created: {folder}")


def create_file(params):
    if len(params) < 1:
        info("Usage: create_file <filename>")
        return

    filename = params[0]

    if file_exists(filename):
        error(f"File already exists: {filename}")
        return


    with open(filename, "w") as f:
        pass
        success(f"File created: {filename}")

# search functions - Salma

# search file by name
def search_filename(params):
    if len(params) < 1:
        info("Usage: search_f <filename>")
        return
    
    filename = params[0]
    files = get_files()

    if filename in files:
        success(f'"{filename}" was found in this directory')
    else:
        error("file not available in this directory")  
    return

# search by extension
def search_extension(params):
    if len(params) < 1:
        info("Usage: search_x <extension>")
        return
    
    extension = params[0]
    files = get_files()
    found_files = []
    
    for file in files:
        if file.endswith(extension):
            found_files.append(file)
        
    if len(found_files) == 0:
        error("not available")  
    else:
        success(f'"{found_files}" was found in this directory')
    return

# search by content
def search_content(params):
    if len(params) < 1:
        info("Usage: search_c <text>")
        return
    
    text = params[0]
    files = get_files()
    found_files = []
    for file in files:
        if file_exists(file):
            file_contents = read_files_into_str(file)
            if text in file_contents:
                found_files.append(file)
        
    if len(found_files) == 0:
        error("this word cannot be found in any file in this directory")  
    else:
        success(f'These files {found_files} contain the search term "{text}"')
    return