# import all the little functions from functions module
from functions import *
from interface import error
commands = {
    "peek": peek,
    "find_x_in": find_x_in,
    "swap": swap_contents,
    "fmeta": fmeta,
    "jump": jump,
    "gwd": gwd,
    "pdelete": pdelete,
    "create_folder":create_folder,
    "create_file": create_file,
    "username": change_username,
    "search_f": search_filename,
    "search_x": search_extension,
    "search_c": search_content,
}

def execute_func(user_input):
    parts = user_input.split()
    cmd = parts[0]
    params = parts[1:]

    if cmd in commands:
        commands[cmd](params)
    else:
        error(f"Unknown command: {cmd}")
