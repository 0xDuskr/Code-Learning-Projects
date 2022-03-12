import sys
from string import ascii_lowercase as low

def syntax():
    print(f"\n [>] Syntax Error: python {sys.argv[0]} <message> <key> <encrypt/decrypt>")
    print(f" [>] Example: python {sys.argv[0]} hello mykey encrypt")
    print(f" [>] Or send the results to a text file: python {sys.argv[0]} tciss mykey decrypt > result.txt")
    print("\n [>] Only letters are accepted in this method (and no spaces), the size of the key must be the same of the message.")
    quit()

def intro():
    try:
        data = sys.argv[1].lower()
        key = sys.argv[2].lower()
        action = sys.argv[3].lower()
        letter_position = []
        key_position = []
        result = []

        if len(data) != len(key):
            print("\n [>] The size of the key must be the same of the message!")
            quit()
        
        words = data + key
        for character in words:
            if character not in low:
                print("\n[>] Only letters are accepted in this method!")
                quit()

        main(data,key,action,letter_position,key_position,result)

    except IndexError:
        syntax()

def main(data,key,action,letter_position,key_position,result):
    if action == "encrypt":
        for letter in data:
            letter_position.append(low.find(letter))
        for key_letter in key:
            key_position.append(low.find(key_letter))

        char_list = [(x+y)%26 for (x,y) in zip(letter_position, key_position)]

        for char in char_list:
            result.append(low[char])
        print(''.join(result))        
    
    elif action == "decrypt":
        for letter in data:
            letter_position.append(low.find(letter))
        for key_letter in key:
            key_position.append(low.find(key_letter))

        char_list = [(x-y)%26 for (x,y) in zip(letter_position,key_position)]

        for char in char_list:
            result.append(low[char])
        print(''.join(result))
    
    else:
        syntax()
    
intro()
