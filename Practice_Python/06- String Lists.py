'''
Ask the user for a string and print out whether this string is a palindrome or not.
A palindrome is a string that reads the same forwards and backwards.
'''

word = input("\nWord: ")
rev = word[::-1]

if word == rev:
    print("\nPalindrome!")
else:
    print("\nNOT a Palindrome!")
