'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''

def even_odd():
    if num % 4 == 0:
        print("\n %s is an even number, and a multiple of 4!" % num)
    elif num % 2 == 0:
        print("\n %s is an even number!" % num)
    else:
        print("\n %s is an odd number!" % num)


def checks_division():
    if num % check == 0:
        print(" {} evenly divides by {}.".format(num, check))
    else:
        print(" {} doesn't evenly divides by {}.".format(num, check))


num = int(input("\n Number to check: "))
check = int(input(" Number to divide by: "))

even_odd()
checks_division()
