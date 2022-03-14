'''
Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
'''

import random

a = [random.randint(1, 51) for i in range(random.randint(1, 16))]
a.sort()
b = [i for i in (a[0],a[-1])]

print("\n A:", a)
print(" B:", b)