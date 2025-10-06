# Lets Check the prime number 

def prime_number(num):
    if num == 1:
        print("It is not a prime number")
    else:
        for digit in range (2, num):
            if num % digit == 0:
                print("Number is not prime number ")
                break
            else:
                print("Number is prime number")


n = int(input ("Add any number"))
# Function call def
prime_number(num =n)

####

