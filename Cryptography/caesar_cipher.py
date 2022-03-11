import sys
from string import ascii_lowercase as low

def syntax():
    print(f"\n [>] Syntax Error: python {sys.argv[0]} <text file> <key number> <encrypt/decrypt>")
    print(f" [>] Example: python {sys.argv[0]} text.txt 3 encrypt")
    print(f" [>] Or send the results to a text file: python {sys.argv[0]} text.txt 3 encrypt > result.txt")
    quit()

def intro():
    try:
        data = open(sys.argv[1], 'r').read().lower()
        key = int(sys.argv[2])
        action = sys.argv[3]
        result = ""
        main(data,key,action,result)
    except IndexError:
        syntax()

def main(data,key,action,result):
    for letter in data:
        if letter in low:
            value = low.find(letter)
            if action == "encrypt":
                value = (value + key) % 26
            elif action == "decrypt":
                value = (value - key) % 26
            else:
                syntax()
            result += low[value]
        else:
            result += letter

    print(f"{result}")

intro()
