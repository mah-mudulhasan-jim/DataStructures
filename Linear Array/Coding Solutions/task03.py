# Task 03: DUBER Fare Splitting
import numpy as np
def findGroups(money, fare):
  # TO DO
  # Print outputs inside the method
  i = 0
  j = len(money) - 1
  count = 1
  g_flag = 0
  while j >= i:
    if money[i] + money[j] == fare:
      print(f'Group {count}: {money[i]}, {money[j]}')
      money[i], money[j] = 0, 0
      count += 1
      i += 1
    j -= 1

  for k in range(len(money)):
    if money[k] != 0:
      if money[k] == fare:
        print(f'Group {count}: {money[k]}')
        money[k] = 0
      else:
        if g_flag == 0:
          print('Ungrouped: ', end ='')
          g_flag += 1
        print(money[k], end = " ")
        money[k] = 0

print("///  Task 03: DUBER Fare Splitting  ///")
money = np.array( [120, 100, 150, 50, 30])
fare = 150
print(f'Task 3:')
findGroups(money, fare) # This should print

# Group 1 : 120, 30
# Group 2 : 100, 50
# Group 3 : 150
print()
print()
print()

money = np.array( [60, 150, 60, 30, 120, 30])
fare = 180
print(f'Task 3:')
findGroups(money, fare) # This should print
print()
print()
print()

# Group 1 : 60, 120
# Group 2 : 30, 150
# Ungrouped : 30 60

money = np.array([30, 150, 150])
fare = 180
print(f'Task 3:')
findGroups(money, fare)