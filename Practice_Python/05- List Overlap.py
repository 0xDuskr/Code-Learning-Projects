'''
Take two lists, say for example these two:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Randomly generate two lists to test this
'''

import random

def creates_lists():
    len_a = random.randint(5, 11)
    a = [random.randint(1, 51) for i in range(len_a)]
    len_b = random.randint(5, 11)
    b = [random.randint(1, 51) for i in range(len_b)]
    c = []
    
    for i in a:
        if i in b:
            if i not in c:
                c.append(i)
    prints_results(a,b,c)


def prints_results(a,b,c):
    a.sort()
    b.sort()
    c.sort()
    print("\nList A:", a)
    print("\nList B:", b)
    print("\nList C:", c)

creates_lists()