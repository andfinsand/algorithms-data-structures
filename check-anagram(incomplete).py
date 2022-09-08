# Check whether two words are an anagram.
# "Heart" == "Earth"?

entry = "heart"

def anagram(checkEntry , given):
    listGiven = list(given)
    if len(checkEntry) != len(given):
        return False
    for x in checkEntry:
        for xgiven in listGiven:
            if x == xgiven:
                listGiven.pop(xgiven)

print(anagram(entry, 'earth'))