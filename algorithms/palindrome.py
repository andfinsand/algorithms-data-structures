# determine if a given value is a palindrome

x = "level"

def solution(inputString):
    counter = -1
    for letter in range(0, len(inputString)):
        if inputString[letter] == inputString[counter]:
            counter -= 1
        else:
            return False
    return True

print(solution(x))
