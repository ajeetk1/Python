# Rock Paper Scissors

# Rock paper scissior game with rock beats paper,scissor beats paper,paper beats rock.

import random # Random number generate 0,1,2

print("🏆 Lets play the game of rock,paper,scissior")
print("0-Rock")
print("1-Paper")
print("2-Scissor")
# User will choose the number
user_choice = input("choose the ? ")

if 0<= user_choice <=2:
    machine_index = random.randint(0,2)
    print(f"You choose:rock_paper_scissir{user_choice}")
    print(f"Machine chooses: rock_paper_scissir{machine_index}")








