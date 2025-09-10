print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************

''') # r string that tell the interpreter to trat backlash as literal character.'''''' triple quotes multiple strings
# r is raw literal string

print("Welcome to the Treasure Island")
print("Your mission is to find the treasure.")

# Game starts
print('\nYou are at the crossroad. Where do you want to go?')
choice = input('Type "left" or "right": ').lower()

if choice == 'left':
    print('\nYou arrive at a beautiful lake.')
    print('You see an island in the middle.')
    print('What are you going to do?')
    
    choice = input("Type 'wait' to wait for a boat or type 'swim' to cross: ").lower()
    if choice == 'wait':
        print("\nYou arrive at the house with three doors.")
        print("Each door has a different color: 'red', 'blue' or 'yellow'")
        choice = input("Type 'red', 'blue' or 'yellow': ").lower() # Lower string
         
        if choice == 'red':
            print('\nRoom full of fire!') # /n new line
            print('Game over.')
        elif choice == 'blue':
            print('\nRoom is full of beasts!')
            print('Game over.')
        elif choice == 'yellow':
            print('\nCongratulations! You found the treasure! 🎉')
        else:
            print("\nThat door doesn’t exist.")
            print("Game over.")
    else:
        print("\nYou are attacked by angry piranhas.")
        print('Game over.')
else:
    print('\nYou are run over by a train.')
    print('Game over.')
