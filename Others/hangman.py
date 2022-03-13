# A different take on the hangman game

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear()
    tentatives = 5
    word = input("\n [>] Choose a word: ").upper()
    clear()
    print("\n [>] The game begins, you have 5 lives!")
    main(tentatives,word)


def main(tentatives,word):
    secret = [x for x in word]
    letters = ["_" for y in secret]
    chosen = []
    
    while tentatives > 0:
        print(f"\n [>] Letters already chosen: [ {' - '.join(chosen)} ]")
        print(f"\n [>] Current status: [ {' '.join(letters)} ]")
        print(f"\n [>] Tentatives left: {tentatives}")
        choice = input("\n [>] Choose a letter: ").upper()
        if choice in word:
            if choice not in letters:
                for x in secret:
                    print(x)
                    if choice == x:
                        letters[secret.index(x)] = choice
                        secret[secret.index(x)] = "0"
                clear()
                print("\n [>] Good guess!")
                if "_" not in letters:
                    clear()
                    print(f"\n [ {' '.join(letters)} ]")
                    print("\n [!] You Won! Game Over!")
                    quit()
                else:
                    if choice not in chosen:
                        chosen.append(choice)
            else:
                clear()
                print("\n [>] Letter already chosen correctly, try another!")
                continue
        else:
            clear()
            tentatives -= 1
            if choice not in chosen:
                chosen.append(choice)
            if tentatives == 0:
                print("\n [!] You Lost! Game over!")
                quit()
            print("\n [>] Wrong choice!")

intro()
