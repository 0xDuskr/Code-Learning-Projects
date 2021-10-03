import main
import sqlite3

def convertTuple(tup):  # To convert tuple to string
    str = ''.join(tup)
    return str

#####

def add():  # To add a new item to the list
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    name = input("Name: ")
    print()
    platform = input("Platform: ")
    print()
    date = input("Release Date (ex. 2020-12-31): ")

    action = "action"
    while action != "OK" or action != "CANCEL":
        print()
        print(">>> Name: {} - Platform: {} - Release Date: {}".format(name, platform, date))
        print()
        action = input("Confirm? Type OK or CANCEL: ")
        action = action.upper()

        if action == "OK":
            cursor.execute("""INSERT INTO list(name, platform, date) VALUES (?,?,?)""", (name, platform, date))
            conn.commit()
            conn.close()
            print()
            print("Success!")
            print()
            advance = input("** PRESS ENTER TO CONTINUE **")
            main.main()

        elif action == "CANCEL":
            print()
            print("Canceled. Returning to the menu.")
            conn.close()
            main.main()

        else:
            print()
            print("** Choose one of the options! **")
            continue

if __name__ == "__main__":
    add()

#####

def edit():  # To change the name, platform and release date of the item
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    action = 0
    while action < 1 or action > 4:
        print("(1) Name  (2) Platform  (3) Release Date  (4) Cancel")
        print()
        action = int(input("Type the selected option: "))
        print()

        if action == 1:
            id = int(input("Item ID: "))
            print()
            new_name = input("New name: ")
            sql_update = """UPDATE list SET name=? WHERE rowid=?"""
            cursor.execute(sql_update, (new_name, id, ))
            conn.commit()
            conn.close()

            print()
            print("Success!")
            print()
            advance = input("** PRESS ENTER TO CONTINUE **")
            main.main()

        elif action == 2:
            id = int(input("Item ID: "))
            print()
            new_platform = input("Platforms: ")
            sql_update = """UPDATE list SET platform=? WHERE rowid=?"""
            cursor.execute(sql_update, (new_platform, id, ))
            conn.commit()
            conn.close()

            print()
            print("Success!")
            print()
            advance = input("** PRESS ENTER TO CONTINUE **")
            main.main()

        elif action == 3:
            id = int(input("Item ID: "))
            print()
            new_date = input("Release Date (ex. 2020-12-31): ")
            sql_update = """UPDATE list SET date=? WHERE rowid=?"""
            cursor.execute(sql_update, (new_date, id, ))
            conn.commit()
            conn.close()

            print()
            print("Success!")
            print()
            advance = input("** PRESS ENTER TO CONTINUE **")
            main.main()

        elif action == 4:
            print("Canceled. Returning to the menu.")
            conn.close()
            main.main()

        else:
            print("** Choose one of the options! **")
            continue

if __name__ == "__main__":
    edit()

#####

def remove():  # To remove an item from the list, based on the ID provided
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    id = int(input("Item ID: "))
    print()

    sql_get_name = """SELECT name FROM list WHERE rowid=?"""
    cursor.execute(sql_get_name, (id, ))
    tuple = cursor.fetchone()
    str = convertTuple(tuple)
    new_name = str

    action = "action"
    while action != "OK" or action != "CANCEL":
        action = input("Confirm remove '{}'? Type OK or CANCEL: ".format(new_name))
        action = action.upper()

        if action == "OK":
            sql_remove = """DELETE FROM list WHERE rowid=?"""
            cursor.execute(sql_remove, (id, ))
            conn.commit()
            conn.close()
            break

        elif action == "CANCEL":
            print()
            print("Canceled. Returning to the menu.")
            conn.close()
            main.main()

        else:
            print()
            print("** Choose one of the options! **")
            print()
            continue

    print()
    print("Success!")
    print()
    advance = input("** PRESS ENTER TO CONTINUE **")
    main.main()

if __name__ == "__main__":
    remove()

#####

def full_list():  # To show the full items list, released (no Date) first, then closest to release date
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    print(">>> Full List:")
    print()
    print("ID || Name || Platform || Release Date")
    print()
    for row in cursor.execute("SELECT rowid, * FROM list ORDER BY date"):
        print(row)
    conn.close()

    print()
    advance = input("** PRESS ENTER TO CONTINUE **")
    main.main()

if __name__ == "__main__":
    full_list()
