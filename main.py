from interface import show_menu
from functions import clean,get_username
from commands import execute_func
import os
from interface import cprint,title, success, error
# this is where the main application will run
def main():
    user = get_username()
    while True:
        user_input = input(f"{user}@CLI-T>>> ").strip()
        if user_input == "":
            continue
        elif user_input == "clean":
            clean()
        elif user_input == "help":
            show_menu()
        elif user_input == "exit":
            success("Exiting filecli...")
            break
        else:
            execute_func(user_input)
if __name__ == "__main__":
    main()
