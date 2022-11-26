# Output all divisible numbers in a selected number

user_input = int(input("Choose a number: "))
divisible_list = []

def all_divisors(x):
    for num in range(x+1):
        if num > 0 and x % num == 0:
            divisible_list.append(num)
    return(divisible_list)

print(all_divisors(user_input))
