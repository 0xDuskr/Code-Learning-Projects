'''
Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
The Fibonacci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 0, 1, 1, 2, 3, 5, 8, 13, …
'''


num = int(input("\nHow many numbers to generate in the Fibonacci sequence: "))
a = []

if num == 0 or num == 1:
    a.append(num)
elif num > 1:
    a = [1, 1]
    for i in a:
        if len(a) < num:
            i = a[-1] + a[-2]
            a.append(i)
print(a)
