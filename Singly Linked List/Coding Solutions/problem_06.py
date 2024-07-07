import numpy as np
import fhm_unittest as unittest
from GeneralRun import createList, printLinkedList
# Task 6: Sum of Nodes
def sum_dist(head, arr):
  #TO DO
  sum = 0
  for i in range(len(arr)):
    count = 0
    temp = head
    while temp != None:
      if count == arr[i]:
        sum += temp.elem
        break
      count += 1
      temp = temp.next
  return sum



print('==============Test Case 1=============')
LL1 = createList(np.array([10,16,-5,9,3,4]))
dist = np.array([2,0,5,2,8])
returned_value = sum_dist(LL1, dist)
print(f'Sum of Nodes: {returned_value}') #This should print Sum of Nodes: 4
unittest.output_test(returned_value, 4)
print()