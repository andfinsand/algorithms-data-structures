# Compare each index of Alice's scores and Bob's scores. Eg. a[2] compared to b[2]. Whoever has the highest score, increment the scorecard list by the corresponding index: scorecard[0] == Alice , scorecard[1] == Bob.

a = [1, 2, 3, 2, 5, 2]
b = [3, 2, 1, 2, 1, 1]

def compareTriplets(a, b):
    scorecard = [0,0]
    i = 0
    for i in range(0, len(a)):
        if a[i] < b[i]:
            scorecard[1] += 1
        elif a[i] > b[i]:
            scorecard[0] += 1
        elif a[i] == b[i]:
            continue
        i += 1
    return scorecard

print(compareTriplets(a, b))
