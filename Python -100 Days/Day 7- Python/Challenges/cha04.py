# Challenge 4

import random 

stages = [r '''''']

word_list = ["adverse","john","Judo"]
#print(word_list)
choice_of_word = random.choice(word_list)
print(choice_of_word)
# Find length of word
display =["-"]*len(choice_of_word)
print(display)
lives = 6  # lives ??

print(f"What is the word {choice_of_word}")


while '-' in display and lives>0:
    print(f"{'.'.join(display)}")

    guess_letter = input("Enter the chosen letter").lower()
    if guess_letter in choice_of_word:
        for idx,letter in enumerate(choice_of_word):
            if guess_letter == letter:
                display[idx] = letter

            else:
                lives -= 1
                print(stages[lives])
                print(f"{"".join(display)}")

                if lives == 0:
                    print("you loose")
                else:
                    print("You win")
