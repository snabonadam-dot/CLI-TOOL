# SALMA CLI.PY TOOL

## Overview

The SALMA CLI.PY TOOL is a CLI tool that allows you to perform various operations on files and folders in your filesystem using Python. It provides the user with a lot simple commands to execute simple daily tasks like creating folders, files, searching for keywords and also swapping the contents of two files.

## Functionality

This tool provides the user with the following commands to manage their files:
`peek` - Preview the first n lines of a file
`swap` - Swap the contents of two files
`search_f` - Search for a file in the current directory
`search_ex` - Search for files with a certain extension
`search_w` - Search for a word in a file
`cfile` - Create a new empty file
`cfolder` - Create a new folder
`pdelete` - Permanently delete a file or folder
`fmeta` - Show metadata for a file
`jump` - Change working directory to another folder
`getwd` - Show current working directory

## Installation/setup instructions

This project is fully in python, as a result your will need a python runtime environment.
The next thing is to install the neccesary packages, this project uses a third party called "Colorama" for coloring the output in the command line tool.

You can install colorama by doing `pip install colorama` or simply run this command to install the requirments file

`pip install -r requirements.txt`
This contains the third party library requirements for this project.
After this this command runs successfully, you can now run the program

You can run the tool by typing `python main.py` in the terminal

## Usage Examples

### Search Examples

```
hacker@SALMA>>> search_f hello.txt # search for a file in the current directory

hacker@SALMA>>> search_w "hello" # search for all files that contain the word "hello"

hacker@SALMA>>> search_ex ".txt" # search for all files with this extension

hacker@SALMA>>> find_x_in "hello" in words.txt # find a certain word in a text file
```

### File Management Examples

```
hacker@SALMA>>> swap text1.txt text2.txt # swap the contents of the files

hacker@SALMA>>> cfile example.txt # create a file called example.txt

hacker@SALMA>>> cfolder books # create a folder called books
```

### Navigation Examples

```
hacker@SALMA>>> jump C:/Users/salma # change the working directory to C:/Users/salma
```

Description of each module and team member responsibility

## Modules and Team Member Responsibilities

### Modules created by Salma
Search Functions - Salma
includes `search_f`, `search_ext`, `search_w` functions which allows the user to search by extension
search by a word and finally search by file name.
Font and colors chosen - Salma
help menu revisions


### Modules created by Abdul Hakim
Project structure - Hakim
this includes the design choice to seperate the modules into 4 files
`interface.py`, `commands.py`, `functions.py`, `main.py` and allow them to integrate 
and work together smoothly

Command Functions - Hakim
functions are as follows: 
`peek()`, `find_x_in()`, `swap_contents()`, `fmeta()`, `jump()`, `gwd()`, `pdelete()`

implementation of custom print functions for colored outputs in the tool - Hakim

a custom print `cprint()`, which was then used to create the rest of the custom print functions such as success, `error` and `info`, `stylish`, with colors ranging from green,red, blue and magenta respectively.


### Modules created by Caleb
Helper Functions - Caleb

this includes the small functions that allowed us to write the main commands
functions are as follows: 
`file_exists()`, `foler_exists()`, `get_files()`, `get_folders()`, `read_files_into_str()`, `clean()`

Help menu structure and Notes - Caleb
This includes the help menu design and the notes for the help menu

We also collaborated using github and the public repo is linked below
https://github.com/snabonadam-dot/CLI-TOOL

## Sources for external libraries
colorama
https://www.geeksforgeeks.org/python/introduction-to-python-colorama/
