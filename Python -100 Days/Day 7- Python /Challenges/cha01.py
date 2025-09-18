# Challenge # 1
# Guess a letter game 

import random 

# array with words
word_list = ["dublin" "naples" "milan"]
print(word_list)
select_word = random.choice(word_list)

# letter choose 

select = input("Enter your letter").lower()
print(select)


for letter in select_word:
 if select == letter:
        print("Right")
 else:
        print("Wrong")