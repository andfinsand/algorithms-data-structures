# Check whether two words are an anagram.
# "Heart" == "Earth"?

entry = "heart"

def anagram(checkEntry , given):

    # convert string to lower case and remove empty spaces
    convertEntry = checkEntry.lower().replace(" ", "")
    convertGiven = given.lower().replace(" ", "")

    # check if length is the same
    if len(checkEntry) != len(given):
        return False

    # convert to lists and sort
    sortEntry = sorted(list(convertEntry))
    sortGiven = sorted(list(convertGiven))

    # compare sorted lists
    if sortEntry == sortGiven:
        return True
    else:
        return False

print(anagram(entry, 'earth'))