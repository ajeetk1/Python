# Make a Tip Calculator total amount tip percent and number of people

total_bill = float(input("enter total bill amount ?"))
print(total_bill)

percentage_tip = int(input("How much tip you are giving 5%,10% or 6%"))
print(percentage_tip)

total_number_people = int(input("How many user went for?"))
print(total_number_people)

tip = float((total_bill + ((total_bill*percentage_tip)/100))/total_number_people)
print(f"Each person shoul pay {tip}")
