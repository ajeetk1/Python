# Split String Method 

import random

names_string = input("Give me everybody names ,seperated by comma")
names = names_string.split(" ,")
print(names)


index = random.randrange(0,len(names)) # Array
print(f'{names[index]} is going to party')