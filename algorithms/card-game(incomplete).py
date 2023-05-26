# Two players. Each pull one card from top of deck. Highest card wins, and both cards get added to bottom of winner deck, with highest first. How many turns until either player has zero cards.

# Option 1 - Custom deck

def solution(deck1, deck2):
    turns = 0 # Number of turns
    while True:
        if len(deck1) == 0 or len(deck2) == 0: # Check if either deck is empty
            return turns
        elif deck1[0] > deck2[0]: # Player 1 has a higher card
            turns += 1
            deck1.append(deck1[0])
            deck1.append(deck2[0])
            deck1.remove(deck1[0])
            deck2.remove(deck2[0])
        elif deck1[0] < deck2[0]: # Player 2 has a higher card
            turns += 1
            deck2.append(deck1[0])
            deck2.append(deck2[0])
            deck1.remove(deck1[0])
            deck2.remove(deck2[0])

x = [1, 12]
y = [3, 8]

print(solution(x , y))

# Option 2 - Predefined deck with 52 cards

def solutionTwo():
    deck = list(range(1, 53))  # Create a deck of 52 cards
    player1_deck = []  # Player 1's deck
    player2_deck = []  # Player 2's deck
    turns = 0  # Number of turns

    while len(player1_deck) < 52 and len(player2_deck) < 52:
        turns += 1
        card1 = deck.pop(0)  # Player 1 draws a card
        card2 = deck.pop(0)  # Player 2 draws a card

        if card1 > card2:
            player1_deck.extend([card1, card2])  # Player 1 wins, cards added to their deck
        else:
            player2_deck.extend([card2, card1])  # Player 2 wins, cards added to their deck

    return turns

# Calculate the number of turns until either player has zero cards
turns_to_zero_cards = solutionTwo()
print("Number of turns:", turns_to_zero_cards)
