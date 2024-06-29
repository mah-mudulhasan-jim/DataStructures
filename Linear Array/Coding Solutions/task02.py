# Task 02: Discard Cards
import fhm_unittest as unittest
import numpy as np
def discardCards(cards, t):
  # TO DO
  alt = 0
  for i in range(len(cards)):
    if cards[i] == t:
      if alt % 2 == 0:
        cards[i] = 0
      alt += 1
  newArr = np.zeros(len(cards), dtype = int)
  j = 0
  k = 0
  while j < len(cards):
    if cards[j] != 0:
      newArr[k] = cards[j]
      k += 1
    j += 1
  return newArr

print("///  Task 02: Discard Cards  ///")
cards = np.array([1,3,7,2,5,2,2,2,0])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1,3,7,5,2,2,0,0,0]
unittest.output_test(returned_value, np.array([1,3,7,5,2,2,0,0,0]))

cards = np.array([5,5,5,0,0])
returned_value = discardCards(cards, 5)
print(f'Task 2: {returned_value}') # This should print [5,0,0,0,0]
unittest.output_test(returned_value, np.array([5,0,0,0,0]))