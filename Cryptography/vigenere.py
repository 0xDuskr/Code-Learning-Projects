import sys
from string import ascii_lowercase as low

def syntax():
    print(f"\n [>] Syntax Error: python {sys.argv[0]} <text file> <key string> <encrypt/decrypt>")
    print(f" [>] Example: python {sys.argv[0]} text.txt thisismykey encrypt")
    print(f" [>] Or send the results to a text file: python {sys.argv[0]} text.txt thisismykey encrypt > result.txt")
    quit()

def intro():
    try:
        data = open(sys.argv[1], 'r').read().lower()
        key = sys.argv[2].lower()
        action = sys.argv[3]
        result = ""
        key_value = 0
        main(data,key,action,result,key_value)
    except IndexError:
        syntax()
    except FileNotFoundError:
        print(f"\n [>] File '{sys.argv[1]}' not found!")
        quit() 

def main(data,key,action,result,key_value):
    for letter in data:
        if letter in low:
            value = low.find(letter)
            if action == "encrypt":
                value += low.find(key[key_value % len(key)])
            elif action == "decrypt":
                value -= low.find(key[key_value % len(key)])
            else:
                syntax()
            result += low[value % 26]
            key_value += 1
        else:
            result += letter

    print(result)

intro()
