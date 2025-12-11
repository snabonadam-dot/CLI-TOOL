
from colorama import Fore, Style, init

# initialize colorama
init(autoreset=True)

# Color constants
COLORS = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "white": Fore.WHITE,
    "reset": Style.RESET_ALL
}

# custom print with color parameter
def cprint(text, color):
    text_color = COLORS.get(color.lower())
    print(f"{text_color}{text}")

# for information
def info(text):
    cprint(text, "blue")

# purple
def purple(text):
    cprint(text, "magenta")

# for success messages
def success(text):
    cprint(text, "green")

# for error messages
def error(text):
    cprint(text, "red")


name = """
 ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓██████████████▓▒░ ░▒▓██████▓▒░        ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░  
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░     
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░         ░▒▓█▓▒░     
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░▒▓██▓▒░▒▓█▓▒░         ░▒▓█▓▒░     
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
 """
def show_menu():
    purple(name)
    success("    Created by @hakim @salma @caleb")
    info("""
    N.B. '<>' is used to represent the input space for your target file path when combining with
    the given command(s)    
    """)
    print('''      
    ---------------------------------AVAILABLE COMMANDS--------------------------------------------------

    peek <target file>                                  -      Preview the first n lines of a file
    find_x_in <target word> in <target file>                 -      Find files matching a pattern
    swap <target file 1> with <target file 2>           -      Swap contents of two files
    fmeta <target file>                                 -      Show metadata for a file
    jump <target folder>                                -      Change working directory    
    getwd <target folder>                               -      Show current working directory
    pdelete -f <target file>                            -      Permanently delete file
    pdelete -d <target folder>                          -      Permanently delete folder 
    cfile <filename>                                    -      Create a new empty file   
    cfolder <folder name>                               -      Create a new folder
    search_f <filename.ext>                                 -      find file in the current directory
    search_ex <extension eg .txt>                        -      search for files with a certain extension
    search_w <search word>                              -      search files for a certain keyword
    exit                                                -      Quit the CLI tool
''')
    print()