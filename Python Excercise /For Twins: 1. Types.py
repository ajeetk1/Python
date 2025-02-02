# For Twins: 1. Types
# DESCRIPTION:
# This kata series was created for friends of mine who just started to learn programming. Wish you all the best and keep your mind open and sharp!
# Task:
# Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types match or false if not.
# Examples:
# 42, "int"    --> True
# "42", "int"  --> False

# My Solution 
def type_validation(variable, _type):

    return type(variable).__name__ == _type # Here we are comparing the 1) type(variable) = type and 
                                            # _type can be string so type(variable),._name_

# The .__name__ attribute is a special attribute in Python that is used to get the name of a class, 
# function, type, or module as a string. It is particularly useful when you want to work 
# with the name of an object rather than the object itself.