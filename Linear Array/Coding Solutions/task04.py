#Task 04: Get Those Hobbies:
import numpy as np
def analyzeHobbies(* participants): #(* arguments) is used for variable number of parameters
  #TO DO
  #Print inside the function
  count = 0
  for i in range(len(participants)):
    count += len(participants[i])


  allHobby = np.array([None]*count)
  all_indx = 0
  unique_count = 0
  for i in range(len(participants)):
    for j in range(len(participants[i])):
      if participants[i][j] not in allHobby:
        unique_count += 1
      allHobby[all_indx] = participants[i][j]
      all_indx += 1


  uniqueHobby = np.array([None]*unique_count)
  uniqueHobbyCounter = np.zeros(unique_count, dtype = int)


  k = 0
  for i in range(len(allHobby)):
    if allHobby[i] not in uniqueHobby:
      uniqueHobby[k] = allHobby[i]
      k += 1


  i = 0
  while i < len(uniqueHobby):
    count = 0
    for j in range(len(allHobby)):
      if uniqueHobby[i] == allHobby[j]:
        count += 1
    uniqueHobbyCounter[i] = count
    i += 1


  print('Unique Activities in the Town:')
  print(uniqueHobby)
  print()


  print('Statistics:')
  for i in range(len(uniqueHobby)):
    print(f'{uniqueHobbyCounter[i]} participant(s) like(s) {uniqueHobby[i]}.')
  # print(uniqueHobbyCounter)



  # print(allHobby)



print("///  Task 04: Get Those Hobbies  ///")
participant_1 = np.array( ["Hiking", "Reading", "Photography", "Cooking"])
participant_2 = np.array( ["Reading", "Hiking", "Painting"])
participant_3 = np.array( ["Hiking", "Cooking", "Photography"])
print(f'Task 4:')
analyzeHobbies(participant_1, participant_2, participant_3) #This should print

#Unique Activities in the Town:
#['Photography', 'Painting', 'Cooking', 'Reading', 'Hiking']

#Statistics:
#2 participant(s) like(s) Photography.
#1 participant(s) like(s) Painting.
#2 participant(s) like(s) Cooking.
#2 participant(s) like(s) Reading.
#3 participant(s) like(s) Hiking.



participant_1 = np.array( ["Gardening", "Traveling"])
participant_2 = np.array( ["Singing", "Gardening", "Painting"])
print(f'Task 4:')
analyzeHobbies(participant_1, participant_2) #This should print

#Unique Activities in the Town:
#[Gardening, Traveling, Singing, Painting]

#Statistics:
#2 participant(s) like(s) Gardening.
#1 participant(s) like(s) Traveling.
#1 participant(s) like(s) Singing.
#1 participant(s) like(s) Painting.
