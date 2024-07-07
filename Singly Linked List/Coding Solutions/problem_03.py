import fhm_unittest as unittest
import numpy as np
from GeneralRun import createList, printLinkedList
# Task 3: Assemble Conga Line
def assemble_conga_line(conga_line):
  #TO DO
  temp = conga_line
  while temp.next != None:
    if temp.elem < temp.next.elem:
      pass
    else:
      return False
    temp = temp.next
  return True

print('==============Test Case 1=============')
conga_line = createList(np.array([10,15,34,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print True
unittest.output_test(returned_value, True)
print()
print('==============Test Case 2=============')
conga_line = createList(np.array([10,15,44,41,56,72]))
print('Original Conga Line: ', end = ' ')
printLinkedList(conga_line)
returned_value = assemble_conga_line(conga_line)
print(returned_value) #This should print False
unittest.output_test(returned_value, False)
print()