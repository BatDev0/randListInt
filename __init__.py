# Importing random so i can get a random index. To index into the list.

import random
from random import randint

def randlistNumber(numberList=[1,2,3,4,5,6,7,8,9,10]
  # Getting the length of the Imported list and subtracting it by the length. And then have the last range just be the length so its ex. 0 - 10 or 0 - 20 etc.
  random = randint(len(numberList)-len(numberList),len(numberList)
  # Indexing into a random area of the list, then printing it to show the random number.
  print(numberList[random])
# Calling the function, so it can run.
randlistNumber()

print(len(numberlist))
