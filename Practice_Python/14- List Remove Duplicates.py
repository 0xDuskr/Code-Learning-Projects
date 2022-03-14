'''
Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
'''

import random

a = [random.randint(1, 11) for i in range(random.randint(5, 11))]
a.sort()
b = []

for i in a:
    if i not in b:
        b.append(i)

print("\n List A:", a)
print(" List B:", b)
print(" Set:", list(set(a)))