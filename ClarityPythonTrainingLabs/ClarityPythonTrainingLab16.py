# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 08:36:23 2018

@author: DK

What is the regex pattern to match the following:
• Email (such as name@email.com)
• Email with .com, .edu or .gov address
• Email with no numbers allowed in
  mailbox name

"""
import re

#What is the regex pattern to match the following:

#Email (such as name@email.com)
def valid_email(email):
    if not re.match("[^@]+@[^@]+\.[^@]+", email):
        return f"'{email}' is not a valid email"
    else:
        return f"'{email}' is a valid email"
    
valid_email("me@me.com")
valid_email("foo")
    
#Email with .com, .edu or .gov address
def email_domain_whitelist(email):
    if not re.match("[^@]+@[^@]+\.(^@|com|gov|edu)+", email):
        return f"'{email}' does not have a whitelisted domain"
    else:
        return f"'{email}' has a whitelisted domain"

email_domain_whitelist("me@me.com")    
email_domain_whitelist("me@me.net")

#Email with no numbers allowed in mailbox name
def email_mailbox_nonumeric(email):
    if not re.match("[^@0-9]+@[^@]+\.[^@]+", email):
        return f"'{email}' is not a vaild email. Numbers in the mailbox are not allowed"
    else:
        return f"'{email}' is a valid email"

email_mailbox_nonumeric("me@me.com")
email_mailbox_nonumeric("me2@me.com")

"""
Write a function which tests if a password is >= 8 characters and meets at 
least 3 of the following requirements:
• Has 1+ English uppercase alphabet character (A–Z)
• Has 1+ English lowercase alphabet character (a–z)
• Has 1+ Base-10 digits (0–9)
• Has 1+ Non-alphanumeric characters (for example,
  !$#,%)
This function should accept one parameter.
"""

def password_requirements(password):
    password = str(password)
    if len(password) < 8:
        return f"Your password must be at least 8 characters"
    elif not re.search(r'[A-Z]', password):
        return f"Your password needs to contain 1+ English uppercase alphabet character (A–Z)"
    elif not re.search(r'[a-z]', password):
        return f"Your password needs to contain 1+ English lowercase alphabet character (a–z)"
    elif not re.search(r'[0-9]', password):
        return f"Your password needs to contain 1+ Base-10 digits (0–9)"
    elif not re.search(r'[\W]', password):
        return f"Your password needs to contain 1+ Non-alphanumeric characters"
    else:
        return f"Your password meets the requirements"

password_requirements("Abcdefg$")
        