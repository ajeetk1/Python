# Be Concise I - The Ternary Operator
# You are given a function describeAge / describe_age that takes a parameter age (which will always be a positive integer) and does the following:

# If the age is 12 or lower, it return "You're a(n) kid"
# If the age is anything between 13 and 17 (inclusive), it return "You're a(n) teenager"
# If the age is anything between 18 and 64 (inclusive), it return "You're a(n) adult"
# If the age is 65 or above, it return "You're a(n) elderly"
# Your task is to shorten the code as much as possible. Note that submitting the given code will not work because there is a character limit of 145.

# I'll give you a few hints:

# The title itself is a hint - if you're not sure what to do, always research any terminology in this description that you have not heard of!
# Don't you think the whole "You're a(n) <insert_something_here>" is very repetitive? ;) Perhaps we can shorten it?
# Write everything in one line, \n and other whitespaces counts.
# Whatever you do, do not change what the function does. Good luck :)

# My Solution 
def describe_age(a):
    if a<= 12: 
        return "You're a(n) kid"
    elif(a>= 13 and a<= 17): 
        return "You're a(n) teenager"
    elif (a>= 18 and a<= 64): 
        return "You're a(n) adult"
    else: 
        return "You're a(n) elderly"