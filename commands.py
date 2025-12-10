# import all the custom functions from functions module
from functions import *
from interface import error
commands = {
    "peek": peek,
    "find_x_in": find_x_in,
    "swap": swap_contents,
    "fmeta": fmeta,
    "jump": jump,
    "getwd": gwd,
    "pdelete": pdelete,
    "cfolder":create_folder,
    "cfile": create_file,
    "search_f": search_filename,
    "search_ex": search_extension,
    "search_w": search_content,
}

def execute_func(user_input):
    parts = user_input.split()
    cmd = parts[0]
    params = parts[1:]

    if cmd in commands:
        commands[cmd](params)
    else:
        error(f"Unknown command: {cmd}")
