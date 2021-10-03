import core
import sqlite3

def main():  # Main menu of the application, redirects to the core functions
    print()
    print("---------------")
    print("|  MAIN MENU  |")
    print("---------------")
    print()

    action = 0
    while action < 1 or action > 5:
        print("(1) Add  (2) Edit  (3) Remove  (4) List  (5) Exit")
        print()
        action = int(input("Type the selected option: "))
        print()

        if action == 1:
            core.add()

        elif action == 2:
            core.edit()

        elif action == 3:
            core.remove()

        elif action == 4:
            core.full_list()

        elif action == 5:
            print("Session closed.")
            exit()

        else:
            print("** Choose one of the options! **")
            print()
            continue

if __name__ == "__main__":
    main()
