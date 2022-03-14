'''
Write a program that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
'''

words = input("\n Type a phrase: ")
rev = ' '.join(words.split()[::-1])

print(f"\n {rev}")