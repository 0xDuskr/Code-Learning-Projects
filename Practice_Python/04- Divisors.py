'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
'''

def checks_divisors():
    for item in a:
        if num % item == 0:
            b.append(item)


num = int(input("\n Number: "))
a = list(range(1, (num + 1)))
b = []

checks_divisors()
print("\n List of divisors of %s:" % num, b)