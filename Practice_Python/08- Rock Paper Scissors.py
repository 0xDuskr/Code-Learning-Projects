'''
Make a two-player Rock-Paper-Scissors game.
Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game
Rock beats scissors | Scissors beats paper | Paper beats rock
'''


def players_input():
    print("\n>>> Choose rock, paper or scissors <<<")

    global p1
    p1 = input("\n-> Player 1: ").lower()
    print("\n\n\n\n----> Don't look above! \n\n\n")

    global p2
    p2 = input("\n-> Player 2: ").lower()


def game_core():
    print("\n\n\nAnd the result is...")

    if p1 == p2:
        print("\nIt's a tie!")
    elif p1 == "rock":
        if p2 == "scissors":
            print("\nPlayer 1 wins!")
        else:
            print("\nPlayer 2 wins!")
    elif p1 == "scissors":
        if p2 == "paper":
            print("\nPlayer 1 wins!")
        else:
            print("\nPlayer 2 wins!")
    elif p1 == "paper":
        if p2 == "rock":
            print("\nPlayer 1 wins!")
        else:
            print("\nPlayer 2 wins!")
    else:
        print("\nInvalid option! Quitting!")
        exit()


p1 = ""
p2 = ""

players_input()
game_core()
