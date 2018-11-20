# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 18:27:47 2018

Read in the contents of the file my_hidden.txt and replace all occurrences of 
the word "hidden" with your favorite subject in school. Write the results to a 
new file called my_favorite_subject.txt.

@author: DK
"""
#read in myhiddentext.txt
txt_file = open("myhiddentext.txt",'r')
file_data = txt_file.read()
txt_file.close()

#replace "hidden" with "math"
new_txt_file = file_data.replace("hidden", "math")
txt_file = open("myhiddentext.txt",'w')
txt_file.write(new_txt_file)
txt_file.close()