# Challenge # 1
# Guess a letter game 

import random 

# array with words
word_list = ["akkasin","night","yourstory"]
#print(word_list)
select_word = random.choice(word_list)
print(select_word)
# letter choose 

select = input("Enter your letter").lower()
print(select)

if select in select_word:
        print("Right")
else:
        print("Wrong")