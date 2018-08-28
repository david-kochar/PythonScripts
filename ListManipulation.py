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

