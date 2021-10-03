'''
Take a list, say for example this one:  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
Write a program that prints out all the elements of the list that are less than 5.
Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''


def smaller_than_five():
    for num in a:
        if num < 5:
            b.append(num)


def user_number():
    for num in a:
        if num < number:
            d.append(num)


def prints_results():
    print("\nList: ", a)
    print("\nNumbers < 5: ", b)
    print("\nList comprehension: ", c)
    print("\nNumbers < %s:" % number, d)


number = int(input("\nNumber: "))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
c = [num for num in a if num < 5]
d = []

smaller_than_five()
user_number()
prints_results()
