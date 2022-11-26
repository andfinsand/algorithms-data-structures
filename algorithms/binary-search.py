# Implement a binary search

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:
                break
            lower = x
        elif target < val:
            upper = x

print(binary_search(l,5))