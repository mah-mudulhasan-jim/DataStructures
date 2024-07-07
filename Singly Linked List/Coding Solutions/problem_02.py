import fhm_unittest as unittest
import numpy as np
from GeneralRun import createList, printLinkedList
# Task 2: Remove Compartment
def remove_compartment(head,n):
  #TO DO
  temp = head
  count = 0
  while temp != None:
    count += 1
    temp = temp.next
  temp = head
  n = count - n
  count = 0
  if n == 0:
    head = head.next
    return head
  while temp.next != None:
    count += 1
    if count == n:
      temp1 = temp.next
      temp.next = temp.next.next
      temp1.next = None
    temp = temp.next

  return head
print('==============Test Case 1=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,2)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->72
print()
print('==============Test Case 2=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,7)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 10-->15-->34-->41-->56-->72
print()
print('==============Test Case 3=============')
head = createList(np.array([10,15,34,41,56,72]))
print('Original Compartment Sequence: ', end = ' ')
printLinkedList(head)
head = remove_compartment(head,6)
print('Changed Compartment Sequence: ', end = ' ')
printLinkedList(head) #This should print 15-->34-->41-->56-->72
print()