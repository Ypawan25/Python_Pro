# Write a function with name ‘dividebyfive’ which generates and prints a random integer
# number from the range 0 to 100 and then returns ‘True’ if the randomly generated
# number is divisible by 5, and ‘False’ otherwise.

import random

def dividebyfive():
  value = random.randint(0,100)
  print(value)
  if(value%5==0):
    return True
  else:
    return False

result =dividebyfive()
print(result)