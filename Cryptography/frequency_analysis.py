import sys
from string import ascii_lowercase as low

def syntax():
    print(f"\n [>] Syntax Error: python {sys.argv[0]} <text file>")
    print(f" [>] Example: python {sys.argv[0]} text.txt")
    print(f" [>] Or send the results to a text file: python {sys.argv[0]} text.txt > result.txt")
    quit()

def intro():
    try:
        english_freq = "etaoinshrdlcumwfgypbvkjxqz"
        letter_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        data = open(sys.argv[1], 'r').read().lower()
        main(english_freq,letter_count,data)
    except IndexError:
        syntax()
    except FileNotFoundError:
        print(f"\n [>] File '{sys.argv[1]}' not found!")
        quit()

def main(english_freq,letter_count,data):
    for letter in data:
        if letter in low:
            letter_count[letter] += 1

    order = []
    for item in sorted(letter_count, key=letter_count.get, reverse=True):
        order.append(item)
    order = ''.join(order)

    print(f"\n[>] English: {english_freq}\n[>] Results: {order}")
    
intro()
