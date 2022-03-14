'''
Make a two-player Rock-Paper-Scissors game.
Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game
Rock beats scissors | Scissors beats paper | Paper beats rock
'''
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def players_input():
    print("\n >>> Choose rock, paper or scissors <<<")

    p1 = input("\n -> Player 1: ").lower()
    clear()
    p2 = input("\n -> Player 2: ").lower()
    clear()
    game_core(p1,p2)


def game_core(p1,p2):
    print("\n And the result is...")

    if p1 == p2:
        print("\n It's a tie!")
    elif p1 == "rock":
        if p2 == "scissors":
            print("\n Player 1 wins!")
        else:
            print("\n Player 2 wins!")
    elif p1 == "scissors":
        if p2 == "paper":
            print("\n Player 1 wins!")
        else:
            print("\n Player 2 wins!")
    elif p1 == "paper":
        if p2 == "rock":
            print("\n Player 1 wins!")
        else:
            print("\n Player 2 wins!")
    else:
        print("\n Invalid option! Quitting!")
        quit()

players_input()