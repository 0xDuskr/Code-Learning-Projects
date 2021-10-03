# Ask the user for a number and determine whether the number is prime or not.


def is_it_prime():
    global num
    global list

    while 1 == 1:
        num = input("\nChoose a number (type 'exit' to quit): ")
        if num == "exit":
            exit()
        else:
            num = int(num)
        list = [i for i in range(2, num) if num % i == 0]
        zero_prime(num)


def zero_prime(n):
    if num > 1:
        if len(list) == 0:
            print("\nPrime number")
        else:
            print("\nNot a Prime number")
            print("Divisors:", list)
    else:
        print("\nNot a Prime number")


is_it_prime()
