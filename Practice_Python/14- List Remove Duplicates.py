# Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.


import random


def remove_dup():
    for i in a:
        if i not in b:
            b.append(i)

    print("\nList A:", a)
    print("List B:", b)


def remove_dup_set(x):
    return list(set(x))


a = [random.randint(1, 11) for i in range(random.randint(5, 11))]
b = []

remove_dup()

print("\nSet B:", remove_dup_set(a))
