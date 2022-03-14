'''
Ask the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
Ask the user for another number and printing out that many copies of the previous message.
Print out that many copies of the previous message on separate lines.
'''

import datetime

name = input("\n Name: ")
age = int(input(" Age: "))
number = int(input(" Choose a number: "))
now = datetime.datetime.now()
year = now.year + (100 - age)

print(number *(f"\n {name}, you will turn 100 years old in {year}!"))