# Bonus Ungraded Task: Look and Say ( Failed attempt)
import numpy as np
def look_and_say(arr):
  #TO DO
  k = 1
  newArr = np.zeros(100, dtype = int)
  # for i in range(len(arr)):
  i = 0
  c = 1
  while i < len(arr):
    print(c, i)
    count = 0
    temp = arr[i]
    # for j in range(i, len(arr)):
    j = i
    while j < len(arr):
      if temp == arr[j]:
        count += 1
        j += 1
      else:
        break
    i = j
    newArr[k-1] = count
    newArr[k] = temp
    k += 1
    c += 1

  return newArr


print("///  Bonus Task: Look and Say  ///")
arr = np.array([1,3,1,1,2,2,2,1])
returned_value = look_and_say(arr)
print(f'Bonus Task: {returned_value}') # This should print [1,1,1,3,2,1,3,2,1,1]
#Hint: The size of the new array will never be more than 100.
#[You need not worry about the extra zeroes at the end of your resulting array]
