import datetime

name = input("\nName: ")
age = int(input("Age: "))
bday = input("Did you celebrate your birthday this year already? (y/n) ")
number = int(input("Type a random number: "))
if (bday == "n"):
  age_corrected = (age + 1)
else:
  age_corrected = age  
now = datetime.datetime.now()
year = now.year + (100 - age_corrected)

print(number *("\n{} will turn 100 years old in {}".format(name, year)))
