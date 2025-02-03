#Task:
# Write a function that accepts two integers and returns the remainder of dividing the larger value by the smaller value.
# Division by zero should return an empty value.
# Examples:
# n = 17
# m = 5
# result = 2 (remainder of `17 / 5`)
# n = 0
# m = 1
# result - division by zero (refer to the specifications on how to handle this in your language)

# My Solution 
def remainder(a, b):
# First we have to select which is larger and smaller value 
   smaller = min(a,b)
   larger = max(a,b)
   return(larger % smaller)

   if smaller == 0:
    return None

  





