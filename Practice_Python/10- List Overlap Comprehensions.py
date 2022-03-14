'''
Randomly generate two lists
Write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
'''
import random

def creates_lists():
    len_a = random.randint(1, 16)
    a = [random.randint(1, 51) for i in range(len_a)]
    len_b = random.randint(1, 16)
    b = [random.randint(1, 51) for i in range(len_b)]
    c = []

    for i in a:
        if i in b:
            if i not in c:
                c.append(i)
    prints_lists(a,b,c)

def prints_lists(a,b,c):
    print("\n A:", a)
    print(" B:", b)
    print(" C:", c)

creates_lists()

# Alternative list comprehension code

print("\n\n Alternative list comprehension code")
print(" ",set(x for x in random.sample(range(1, 51),16) if x in random.sample(range(1, 51),16)))