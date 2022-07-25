# Output if odd or even and if divisible by four.

def odd_even(x):
    if x % 2 == 0 and x % 4 == 0:
        return("This is even and divisible by four.")
    elif x % 2 == 0:
        return("This is even")
    else:
        return("This is odd.")

print(odd_even(6))

# BONUS: Check if a number is divisible by another number

num = int(input("Enter a number to check if it divides evenly: "))
divisor = int(input("Enter a divisor: "))

if num % divisor == 0:
    print("Number divides evenly!")
else:
    print("Number does not divide evenly...")