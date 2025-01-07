 # Tip Calculator
print ("Tip Calculator")
# Total Bill Amount 
total = float(input("How much is total Bill amount"))
# Percentage of Tip
tip = int(input("How much tip you want to give, 10 ,12 or 15"))
# Number of Member
member = int(input("How many number members you have"))
# Bill per Person
bill_per_person =(((total + total*(tip/100))/member))
# To Round to the 2 decimal 
bill_to_round = round(bill_per_person,2)
print(bill_to_round)

