import fhm_unittest as unittest
import numpy as np
from GeneralRun import createList, printLinkedList, Node
# Task 4: Word Decoder
def word_Decoder(head):
  count  = 0
  temp = head
  while temp != None:
    count += 1
    temp = temp.next
  x = 13 % count
  new = Node(None)
  temp2 = new
  for i in range(count, x-1, -1):
    count2 = 0
    temp = head
    if i % x == 0:
      while temp2 != None:
        count2 += 1
        if count2 == i:
          temp2.next = Node(temp.next.elem)
          temp2 = temp2.next
          break
        temp = temp.next
      temp = head

  return new

#Driver Code
print('==============Test Case 1=============')
head = createList(np.array(['B', 'M', 'D', 'T', 'N', 'O', 'A', 'P', 'S', 'C']))
print("Encoded Word:")
printLinkedList(head) #This should print B→M→D→T→N→O→A→P→S→C

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→C→A→T

print('==============Test Case 2=============')

head = createList(np.array(['Z', 'O', 'T', 'N', 'X']))
print("Encoded Word:")
printLinkedList(head) #This should print Z→O→T→N→X

result = word_Decoder(head)
print("Decoded Word:")
printLinkedList(result)    #This should print None→N

