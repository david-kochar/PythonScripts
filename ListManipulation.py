# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 12:23:20 2018

@author: DK
"""

# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

#Change "Hanna" to "Hannah"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[5] = "Aparna"

#for person in people:
#    print(person)
    
i = 0
while i < len(people):
    print(f"{i}: {people[i]}")
    i += 1
    
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]

result = str()

for i in sounds:
    result = result + str(i)
    result = result.upper()
    
print(result)

# Create a list called instructors
instructors = []

# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
instructors.extend(["Colt","Blue", "Lisa"])

# Remove the last value in the list

instructors.pop(-1)

# Remove the first value in the list

instructors.pop(0)

# Add the string "Done" to the beginning of the list

instructors.insert(0,"Done")

print(instructors)

# Run the tests to make sure you've done this correctly!

chars = ["a", "b", "c", "a", "d", "a"]
result = []

i = 0
while i < len(chars):
    if chars[i] == "a":
        result += str(i)
    i += 1

print(result)

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

#Infinite loop with list mutation
f = open('Output.txt','w')
L1 = [1,2]
for x in L1:
    L1.append(3)
    print(x, file=f)
    
names = ["Ellie", "Tim", "Matt"] 
answer = []
for i in names:
    answer += i[0][:1]
print(answer)

names = ["Ellie", "Tim", "Matt"] 
answer = [name[0] for name in names]
print(answer)

answer2 = [ num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0 ]
print(answer2)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

answer = [ num for num in [1, 2, 3, 4] if num in [3, 4, 5, 6] ]

print(answer)

names = ["Ellie", "Tim", "Matt"] 
answer = [name[::-1].lower() for name in names]
print(answer)

numbers = list(range(0, 101))

answer  = [ num for num in (range(1, 101)) if num % 12 == 0] 
print (answer)

answer = [ letter for letter in "amazing" if letter not in ["a", "e", "i", "o", "u"] ]
print(answer)

answer = [[num for num in range(0, 3)] for val in range(1, 4)]
print(answer)

# 2-D list comprehension array
answer = [[i for i in range(0,10)] for j in range(0,10)]
print(answer)