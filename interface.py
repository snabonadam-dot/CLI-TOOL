
from colorama import Fore, Style, init

init(autoreset=True)

# Color constants
COLORS = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "yellow": Fore.YELLOW,
    "blue": Fore.BLUE,
    "cyan": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "white": Fore.WHITE,
    "reset": Style.RESET_ALL
}

def cprint(text, color="white"):
    """Custom print function with color."""
    clr = COLORS.get(color.lower(), COLORS["white"])
    print(f"{clr}{text}{COLORS['reset']}")

def title(text):
    cprint("\n" + "=" * len(text), "cyan")
    cprint(text, "cyan")
    cprint("=" * len(text) + "\n", "cyan")

def info(text):
    cprint(text, "blue")

def success(text):
    cprint(text, "green")

def error(text):
    cprint(text, "red")


from interface import cprint

def show_menu():
    cprint("\n=====================================", "cyan")
    cprint("           OH-MY-CLI — Commands      ", "cyan")
    cprint("=====================================\n", "cyan")

    cprint("Available Commands:\n", "yellow")

    # Fake table look
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
