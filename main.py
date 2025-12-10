from interface import show_menu
from functions import clean,get_files
from commands import execute_func
import os
from interface import cprint, success, error,info

# this is where the main application will run
def main():
    show_menu()
    while True:
        user_input = input(f"hacker@CLI-T>>> ").strip()
        if user_input == "":
            continue
        elif user_input == "clear":
            clean()
        elif user_input == "help":
            show_menu()
        elif user_input == "exit":
            info("Exiting filecli...")
            break
        else:
            execute_func(user_input)
if __name__ == "__main__":
    main()
