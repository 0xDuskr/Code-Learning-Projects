'''
Create a program that will play the “cows and bulls” game with the user.
The game works like this:
- Randomly generate a 4-digit number.
- Ask the user to guess a 4-digit number.
- For every digit that the user guessed correctly in the correct place, they have a “cow”.
- For every digit the user guessed correctly in the wrong place is a “bull.”
- Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
- Once the user guesses the correct number, the game is over.
- Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
'''

import random

number = [str(random.randint(1,9)), str(random.randint(0,9)), str(random.randint(0,9)), str(random.randint(0,9))]
number_list = ''.join(number)
guess = 0
attempts = 0

while True:
    try:
        cows = 0
        bulls = 0
        idx = 0

        guess = int(input("\n [>] Choose a 4-digit number (1000-9999): "))
        guess_list = [x for x in str(guess)]

        if 1000 > guess or guess > 9999:
            print("\n [!] Invalid number!")
            continue

        for y in number_list:
            if y == guess_list[idx]:
                cows += 1
            elif y in guess_list:
                bulls += 1
            idx += 1

        if str(guess) == number_list:
            attempts +=1
            print("\n [>] Game over!")
            print(f" [>] Secret number: {number_list}")
            print(f" [>] Attempts: {attempts}")
            quit()

        print(f" [>] Cows: {cows}, Bulls: {bulls}")
        attempts +=1

    except KeyboardInterrupt:
        print()
        quit()
    except ValueError:
        print("\n [!] Invalid number!")
        continue