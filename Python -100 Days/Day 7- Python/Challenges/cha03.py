# challenge 03
# If letter is there print that 

import random

word_list = ["dublin","denmark","japan"]
print(word_list)

# Select word 
choice_word = random.choice(word_list).lower()
print(choice_word)

# Hangman Game I have to display Dash/hyphen
display = ['_']*len(choice_word)
print(display)

# Testing Phase 
print(f"The feature is {choice_word}") 

# output the letter

while '_' in display:
    print (display)
# Ask the player to input the letter 
    guess_word = input("Enter the letter?").lower()
    print(guess_word)
    for idx,letter in enumerate(choice_word):
     if guess_word == letter:
        display[idx] = letter

print(display)
print("You win")