number = int(input("\nType a number: "))

if (number % 4 == 0):
  print("\n%s is even and a multiple of 4." % number)
elif (number % 2 == 0):
  print("\n%s is even." % number)
else:
  print("\n%s is odd." % number)
