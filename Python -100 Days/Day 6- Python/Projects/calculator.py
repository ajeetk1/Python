# calculator

num_1 = int(input("Enter first number"))
num_2 = int(input("Enter second number"))

sum = num_1 + num_2
print(sum)

mul = num_1*num_2
print(mul)

div = num_1/num_2 
print(div)

sub = num_1 -num_2
print(sub)

# Second Way 
# Press 1,2,3,4 

num_1 = int(input("Enter first number"))
num_2 = int(input("Enter second number"))

print("Select choices/n")
print("1. Addition (+)")
print("2. Substraction (-) ")
print("3. Multiply (*) ")
print("4. Division (/) ")

choice = input("Enter (1/2/3/4)") 

if choice == "1":
    print(num_1 +num_2)
elif choice == "2":
    print(num_1 -num_2)
elif choice =="3":
    print(num_1 *num_2)
elif choice =="4":
    if num_2 != 0:
        print("num_1/num_2")
else:
    print("Invalid")
   





