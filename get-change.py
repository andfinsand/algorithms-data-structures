import math

# Get change and calculate the most amount of quarters, dimes, nickels and pennies

x = 97

q = 0
d = 0
n= 0
p = 0

q = math.floor(x/25)
x = x - (q * 25)
d =math.floor(x/10)
x = x - (d * 10)
n =math.floor(x/5)
x = x - (n * 5)
p =math.floor(x/1)
x = x - (d * 1)

print(q , d, n, p)