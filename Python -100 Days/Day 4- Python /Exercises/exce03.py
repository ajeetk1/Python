# Age 

age = input("What is your current age?")
print(age)

# Age i die is 90 
# Years left 
years_left = 90-int(age)


months_left= 12*years_left
weeks_left= 52*months_left
days_left= 365*weeks_left

print(f"you current age is {age} and you have {years_left} and {months_left} and {days_left} on this planet")