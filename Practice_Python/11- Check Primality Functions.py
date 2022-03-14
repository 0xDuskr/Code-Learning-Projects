'''
Ask the user for a number and determine whether the number is prime or not.
'''

def is_it_prime():
    num = input("\n Choose a number (type 'exit' to quit): ")
    if num == "exit":
        quit()
    else:
        num = int(num)
    list = [i for i in range(2, num) if num % i == 0]
    zero_prime(num,list)

def zero_prime(num,list):
    if num > 1:
        if len(list) == 0:
            print("\n Prime number!")
        else:
            print("\n Not a Prime number!")
            print(" Divisors:", list)
    else:
        print("\n Not a Prime number!")

is_it_prime()