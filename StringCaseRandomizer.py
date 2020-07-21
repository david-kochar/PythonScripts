from random import choice

def case_randomizer(chars):
    new_string = ""
    for char in chars:
        new_string += choice((char.upper(), char.lower()))
    return new_string
    
case_randomizer("The String")