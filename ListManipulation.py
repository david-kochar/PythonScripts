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
