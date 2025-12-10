
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

# for success messages
def success(text):
    cprint(text, "green")

# for error messages
def error(text):
    cprint(text, "red")


name = """
 ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░         ░▒▓█▓▒░  ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░         ░▒▓█▓▒░   ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░ 
                                                                                                                                  
                                               
"""
def show_menu():
    cprint("\n=====================================", "cyan")
    cprint("           OH-MY-CLI — Commands      ", "cyan")
    cprint("=====================================\n", "cyan")
    success(name)

    cprint("Available Commands:\n", "yellow")

    table = [
        ("peek <file>",              "Preview the first n lines of a file"),
        ("find_x_in <pattern>",      "Find files matching a pattern"),
        ("swap <f1> <f2>",           "Swap contents of two files"),
        ("fmeta <file>",             "Show metadata for a file"),
        ("jump <path>",              "Change working directory"),
        ("gwd",                      "Show current working directory"),
        ("pdelete -f/-d <target>",   "Permanently delete file or folder"),
        ("create_folder <name>",     "Create a new folder"),
        ("create_file <name>",       "Create a new empty file"),
        ("username <name>",          "Change Username"),
        ("exit",                     "Quit the CLI tool")
    ]

    # Render the table rows
    for cmd, desc in table:
        cprint(f"  {cmd:<25} - {desc}", "white")

    print()
