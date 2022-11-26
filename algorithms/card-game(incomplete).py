# Two players. Each pull one card from top of deck. Highest card wins, and both cards get added to bottom of winner deck, with highest first. How many turns until either player has zero cards.

def solution(deck1, deck2):
    turns = 0
    while True:
        if len(deck1) == 0 or len(deck2) == 0:
            return turns
        elif deck1[0] > deck2[0]:
            turns += 1
            deck1.append(deck1[0])
            deck1.append(deck2[0])
            deck1.remove(deck1[0])
            deck2.remove(deck2[0])
        elif deck1[0] < deck2[0]:
            turns += 1
            deck2.append(deck1[0])
            deck2.append(deck2[0])
            deck1.remove(deck1[0])
            deck2.remove(deck2[0])

x = [1, 12]
y = [3, 8]

print(solution(x , y))