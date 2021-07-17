# Generate list of random length with random numbers
# Print all the elements lower than 20
# 57

import random

def generate_list():
  length = random.randint(5,10)
  numbers = random.randrange(1,50)
  list1 = [random.randint(1,50) for num in range(length)]
  return list1

def selected_list(list1):
  list2 = [num for num in list1 if num < 20]
  if len(list2) == 0:
    print("\n Lista vazia")
  else:  
    print("\n",list2)
  
list1 = generate_list()
selected_list(list1)