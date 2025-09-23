# hangman

import os  # clear the console for the Windows/Mac
import random 
import art
import words 

# Chose word 

# To choose the Random list of words 
select_word = random.choice(words.word_list)
display = ['']*len(select_word)
# print(display)
lives = 6 # Players can make 6 wrong guesses
guess_letter = [] # stores lettes aready guessed to prevent from repeating 

# print logo and display 
print(art.logo)
print(f"{''.join(display)}") # Joins underscores with spaces for readability

# Main Game Loop 

