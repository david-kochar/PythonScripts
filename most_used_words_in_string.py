# -*- coding: utf-8 -*-
"""
print top n most used words in the following string

The man sprang from his chair and paced up and down the room in uncontrollable 
agitation. Then, with a gesture of desperation, he tore the mask from his face 
and hurled it upon the ground. "You are right," he cried; "I am the King. 
Why should I attempt to conceal it?"
"""

txt = 'The man sprang from his chair and paced up and down the room in \
uncontrollable agitation. Then, with a gesture of desperation, he tore the \
mask from his face and hurled it upon the ground. "You are right," he cried; \
"I am the King. Why should I attempt to conceal it?"'

def wordMatch(text):
  text = text.lower()
  import re
  pattern = re.compile(r'\w+')
  words = list(pattern.findall(text))
  return words

def uniqueWords(text):
  return list(set(text))

def topNWords(text, n):
    word_counts = []
    for i in uniqueWords(wordMatch(text)):
        counter = 0
        for j in wordMatch(text):
            if j == i:
                counter += 1
        word_counts.append((i, counter))
    word_counts_sorted = sorted(word_counts, key = lambda x: x[1], reverse=True)
    return word_counts_sorted[0:n]


print("The Top Words by Count Are...\n")
for word, count in topNWords(txt, 5):
    print(word, count)
    


    
    