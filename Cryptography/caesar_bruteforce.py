import sys
from string import ascii_lowercase as low

try:
    data = open(sys.argv[1], "r").read().lower()
except IndexError:
    print(f"\n [>] Syntax Error: python {sys.argv[0]} <text file>")
    print(f" [>] Example: python {sys.argv[0]} encrypted.txt")
    print(f" [>] Or send the results to a text file: python {sys.argv[0]} encrypted.txt > decrypted.txt")
    quit()
except FileNotFoundError:
    print(f"\n [>] File '{sys.argv[1]}' not found!")
    quit()

for key in range(1,26):
    result = ""
    print(f"\n[>] Key: {key}")

    for letter in data:
        if letter in low:
            value = low.find(letter)
            value = (value - key) % 26
            result += low[value]
        else:
            result += letter

    print(result)
