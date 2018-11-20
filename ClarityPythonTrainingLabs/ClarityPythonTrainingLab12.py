# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:52:25 2018

@author: DK

Create a tuple, dean_metadata_shermer_il, containing three values: the integer 
1986, the string Dean, and the string Rooney.

Create a tuple, dean_metadata_faber_college, containing three values: the 
integer 1978, the string Dean, and the string Wormer.

Using the data from steps (1) and (2), and utilizing the order information 
available from step (3), find and output the years and the names of the dean 
data, omitting the role data.

"""
#create tuples for the dean data
dean_metadata_shermer_il = (1986, "Dean", "Rooney")
dean_metadata_faber_college = (1978, "Dean", "Wormer")

#create a function to accept n-dean tuples
def print_tuples(*args):
    d = {} #intitialize a dictionary
    deans = args
    frmat = ("year", "role", "name") #create format tuple
    for t in deans: #created a nested dictionary with each dean tuple
        d[deans.index(t)] = {k[0]:k[1] for k in zip(frmat, t)}
    for values in d.values(): #for each d.value, print the year and name
        print(values["year"], values["name"], sep = " ")
        
print_tuples(dean_metadata_shermer_il, dean_metadata_faber_college)