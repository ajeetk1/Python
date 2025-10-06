# Color Change

RED = "\033[31m"
RESET = "\033[0m"

print("My name is " + RED + "Ajeet" + RESET)
# How can we use in fstring color

# Define ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"


# Adventure Simulator 

print("=== Adenture Simulator")
print ("You will be asked a bunch of questions the you will make up an amazings story")
print()


name = input("Enter your name")
enemy = input("Your worst enemy name")
superPower = input("Your super power:")
print ()


print("Our story begins as our hero name approaches a forboding castle...")
print(f"Suddenly a bolt of lightening striked the ground at the fee of {name}")
print(f'"Our final battle begins!" shouts the evil {GREEN}{enemy}{RESET}. "Clearly missing the fact that" {BLUE}{name}{RESET}, "has the power of" {RED} {superPower}{RESET}, "which means they will win quite easily".')



# Color print("\033 [32] m")
# Super Basic Project Random Number

import random 

number = random.randint(1,10)
guess = int(input("Enter your guessed number?"))

if number == guess:
    print("You won")
else:
    print("You lost")







