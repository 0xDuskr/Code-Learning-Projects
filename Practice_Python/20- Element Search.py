'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
'''

import random

num_list =[]

while len(num_list) != 5:
    num_list.append(random.randint(1,30))

num_list.sort()
num = random.randint(1,30)

print(num_list)
print(num)

if num in num_list:
    print(True)
else:
    print(False)