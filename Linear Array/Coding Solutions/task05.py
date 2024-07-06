# Bonus Ungraded Task: Look and Say ( Failed attempt)
import numpy as np
# Bonus Ungraded Task: Look and Say
def look_and_say(arr):
  newArr = np.zeros(100, dtype = int)
  i = 0
  k = 1
  while i < len(arr):
    temp = arr[i]
    count = 1
    j = i+1
    while j < len(arr):
      if arr[j] == temp:
        count += 1
        j += 1
      else:
        break
    newArr[k-1] = count
    newArr[k] = temp
    i = j
    k += 2
  count2 = 0
  zero_count = 0
  for i in range(len(newArr)):
    if newArr[i] != 0:
      count2 += 1
    else:
      break
  newArr2 = np.zeros(count2, dtype = int)
  for i in range(len(newArr2)):
    newArr2[i] = newArr[i]
  return newArr2

print("///  Bonus Task: Look and Say  ///")
arr = np.array([1,3,1,1,2,2,2,1])
# arr = np.array([1,1,1,2,2,3,1,1,1,1,1,2,2,2,90])
returned_value = look_and_say(arr)
print(f'Bonus Task: {returned_value}') # This should print [1,1,1,3,2,1,3,2,1,1]
#Hint: The size of the new array will never be more than 100.
#[You need not worry about the extra zeroes at the end of your resulting array]
