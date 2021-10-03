'''
Randomly generate two lists
Write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''


import random


def creates_lists():
    global a
    global b

    len_a = random.randint(1, 16)
    a = [random.randint(1, 51) for i in range(len_a)]

    len_b = random.randint(1, 16)
    b = [random.randint(1, 51) for i in range(len_b)]


def generates_new_list():
    global c

    for i in a:
        if i in b:
            if i not in c:
                c.append(i)


def prints_lists():
    print("\nA:", a)
    print("B:", b)
    print("C:", c)


a = []
b = []
c = []

creates_lists()
generates_new_list()
prints_lists()

# Alternative list comprehension code

print("\n\nList comprehension code")
print(set(x for x in random.sample(range(1, 51),16) if x in random.sample(range(1, 51),16)))
