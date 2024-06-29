#Assignment Part-1
#Write 3 methods and driver codes for this part.
import numpy as np
import math
def findMean(arr):
  sum = 0
  for i in range(len(arr)):
    sum += arr[i]
  mean = sum/(len(arr))
  return mean

def standardDev(arr):
  sum = 0
  for i in range(len(arr)):
    sum += (arr[i]-(findMean(arr)))**2
  sd = math.sqrt(sum/(len(arr)-1))
  return sd

def newArr(arr, ran):
  low = findMean(arr) - ((standardDev(arr)) * ran)
  high = findMean(arr) + ((standardDev(arr)) * ran)
  count = 0
  for i in range(len(arr)):
    if arr[i] > high or arr[i] < low:
      count += 1
  newArr = np.zeros(count, dtype = int)
  k = 0
  for i in range(len(arr)):
    if arr[i] > high:
      newArr[k] = arr[i]
      k += 1
  for j in range(len(arr)):
    if arr[j] < low:
      newArr[k] = arr[j]
      k += 1
  return newArr

arr = [10, 8, 13, 9, 14, 25, -5, 20, 7, 7, 4]
print(f'The mean of the numbers is: {findMean(arr)}')
print(f'The standard deviation is: {standardDev(arr):.2f}')
# print(type(standardDev(arr)))

print(f'New array: {newArr(arr, 1.5)}')