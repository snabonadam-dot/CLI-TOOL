import os
import time
from interface import success,error,title
# please write your functions here


# helper functions
# this helps us check if the file exists beforehand, so we don't run into reading or writing errors after
def file_exists(path):
    return os.path.isfile(path)

def folder_exists(path):
    return os.path.isdir(path)

def gwd(params):
    success(os.getcwd())
def get_username():
    with open("user.txt","r",encoding="utf-8") as f:
        username = f.readline()
        return username

def change_username(params):
    if len(params) < 1:
        success("Usage: username <username>")
        return
    username = params[0]
    with open("user.txt","w",encoding="utf-8") as f:
        f.write(username)
        success("username change, exit and restart application")

def action_prompt():
    confirm = input("ARE YOU SURE YOU WANT TO COMPLETE THIS ACTION Y/N?: ")
    if confirm.lower() == "y":
        return True
    else:
        return False

def delete_folder_recursive(folder):
    for item in os.listdir(folder):
        path = os.path.join(folder, item)

        if os.path.isfile(path):
            os.remove(path)

        elif os.path.isdir(path):
            delete_folder_recursive(path)

    os.rmdir(folder)


# command functions
## peek function, allows you to look at the first n lines in a file, prints the first n lines in the console
def peek(params):
    if len(params) < 2:
        success("Usage: peek <filename> <number_of_lines>")
        return
    filename = params[0]
    number_of_lines = int(params[1])
    # first check if the file exists using our custom util function
    if file_exists(filename):
        with open(filename, "r",encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines[:number_of_lines]:
                print(line, end="")
    else:
        error("This file does not exist!")

# find a certain string in a text file, returns if the word can be found and the line it is in
def find_x_in(params):
    if len(params) < 2:
        success("Usage: find_x_in <filename> <word to find>")
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
        success("Usage: swap <file1> <file2>")
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
        success("Usage: fmeta <filename>")
        return
    filename = params[0].strip('"')
    if file_exists(filename):
        stats = os.stat(filename)
        success("File:", filename)
        success("Size:", stats.st_size, "bytes")
        success("Created:", time.ctime(stats.st_ctime))
        success("Modified:", time.ctime(stats.st_mtime))
        success("Accessed:", time.ctime(stats.st_atime))
        success("Extension:", os.path.splitext(filename)[1])
        success("Absolute Path:", os.path.abspath(filename))
    else:
        error("File does not exist!")



# jump is our way of doing change directory
def jump(params):
    if len(params) < 1:
        success("Usage: jump <path>")
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
        success("Usage: pdelete -f <file> | pdelete -d <folder>")
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
        success("Usage: create_folder <foldername>")
        return

    folder = params[0]

    if folder_exists(folder):
        error(f"Folder already exists!: {folder}")
        return

    os.makedirs(folder)
    success(f"Folder created: {folder}")


def create_file(params):
    if len(params) < 1:
        success("Usage: create_file <filename>")
        return

    filename = params[0]

    if file_exists(filename):
        error(f"File already exists: {filename}")
        return


    with open(filename, "w") as f:
        pass
        success(f"File created: {filename}")

