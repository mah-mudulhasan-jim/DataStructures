# Task 02: Discard Cards. !!!! AVOID IT...it was a failed attempt !!!!
import fhm_unittest as unittest
import numpy as np
def discardCards(cards, t):
  # TO DO
  count = 0
  # temp = cards
  for i in range(len(cards)):
    if cards[i] == t:
      count += 1
      if count % 2 != 0:
        for j in range(i+1, len(cards)):
          cards[j-1] = cards[j]
        cards[len(cards)-1] = 0
  return cards

print("///  Task 02: Discard Cards  ///")
cards = np.array([1,3,7,2,5,2,2,2,0])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1,3,7,5,2,2,0,0,0]
unittest.output_test(returned_value, np.array([1,3,7,5,2,2,0,0,0]))

cards = np.array([5,5,5,0,0])
returned_value = discardCards(cards, 5)
print(f'Task 2: {returned_value}') # This should print [5,0,0,0,0]
unittest.output_test(returned_value, np.array([5,0,0,0,0]))