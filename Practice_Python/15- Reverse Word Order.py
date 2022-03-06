# Write a program that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.


def get_word():
    return(input("\nPhrase: "))


def reverse_word(w):
    return ' '.join(w.split()[::-1])


word = get_word()
rev = reverse_word(word)
print(rev)
