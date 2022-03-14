'''
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import random
from string import ascii_letters

def user_input():
    strength = 0
    while strength != 1 and strength != 2 and strength != 3:
        print("\n Choose a password strength ('exit' to quit):")
        print(" (1) Weak   (2) Strong   (3) Very Strong")
        strength = input("\n > ")
        if strength == "exit":
            exit()
        else:
            strength = int(strength)
        if strength == 1:
            weak_pwd()
        elif strength == 2 or strength == 3:
            strong_pwd(strength)
        else:
            print("\n Please choose one of the options.")


def weak_pwd():
    base = ["horse", "shoe", "sun", "computer", "car", "barricade", "sword", "river", "meteor", "shirt", "table", "blanket", "symbol", "cable", "district", "continent", "neptune", "brand", "flag", "thunder", "shield", "emission", "cowl", "cooler", "vitamin", "dust"]
    word1 = random.randint(0, 25)
    word2 = random.randint(0, 25)
    while word1 == word2:
        word2 = random.randint(0, 25)

    password = base[word1] + base[word2]

    print("\n Password:\n\n",password)

    new = ""
    while new != "y" and new != "n":
        new = input("\n Generate a new password (y / n)? ")
        if new == "y":
            user_input()
        elif new == "n":
            exit()
        else:
            print("\n Please choose an option.")


def strong_pwd(strength):
    base = "0123456789()*&%$#@!=+<>.,[]?\/"
    base += ''.join(ascii_letters)

    if strength == 2:
        length = 10
    else:
        length = 15

    password = ''.join(random.sample(base, length))

    print("\n Password:\n\n",password)

    new = ""
    while "y" != new != "n":
        new = input("\n Generate a new password (y / n)? ")
        if new == "y":
            user_input()
        elif new == "n":
            exit()
        else:
            print("\n Please choose an option.")

user_input()