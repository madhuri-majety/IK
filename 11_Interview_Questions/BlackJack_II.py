"""
Very good blackjack program

https://www.youtube.com/watch?v=qqp11XNMNRg

"""

import random

def shuffle(deck):
    for i in range(len(deck)-1, 0, -1):
        r = random.randint(0,i)

        deck[i], deck[r] = deck[r], deck[i]

# A function for creating a deck
def deck():
    deck = []
    for suit in ['H', 'C', 'S', 'D']:
        for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
            deck.append(suit + rank)

    # Python random module's built in function
    #random.shuffle(deck)
    shuffle(deck)

    return deck

# A function for creating the points
# Takes in the players cards and return his total points
def getCount(myCards):
    myCount = 0
    aceCount = 0

    for card in myCards:
        # Indexing 1 as the cards are stored as suit+rank
        if (card[1] == 'J' or card[1] == 'Q' or card[1]=='K'):
            myCount += 10
        elif card[1] != 'A':
            myCount += int(card[1])
        else:
            aceCount += 1

    # A has two choices either 1 or 11
    # If there is only one A and rest of of count >= 10 then consider A as 11
    # If there are more than one A then count A as 1

    if aceCount == 1 and myCount >= 10:
        myCount += 11
    elif aceCount != 0:
        myCount += 1

    return myCount

# A function for creating the player's and delear's hands
# Randomly gives each two cards from the deck
# Return as list with both hands
def createPlayersHands(myDeck):
    playerHand = []
    dealerHand = []

    dealerHand.append(myDeck.pop())
    dealerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())

    while(getCount(dealerHand) < 16):
        dealerHand.append(myDeck.pop())

    return [dealerHand, playerHand]


# Here we create the game stuff
def playGame():
    game = ""
    myDeck = deck()
    hands = createPlayersHands(myDeck)
    dealer = hands[0]
    player = hands[1]

    while (game != "exit"):
        dealerCount = getCount(dealer)
        playerCount = getCount(player)

        print("Dealer has: {}".format(dealer[0]))

        print("Player you have: {}".format(player))

        if playerCount == 21:
            print("BlackJack!! Player Win")
            break
        elif playerCount > 21:
            print("Player BUSTs! with {} points. Dealer Wins!".format(str(playerCount)))
            break
        elif dealerCount > 21:
            print("Dealer Busts! With {} points. Player Wins!".format(dealerCount))

        game = str(input("What would you like to do? H: Hit me, S: Stand?"))

        if game == 'H':
            player.append(myDeck.pop())
            playerCount = getCount(player)
        elif playerCount > dealerCount:
            print("Player wins with {} points".format(playerCount))
            break
        else:
            print("Dealer Wins!")
            print("Dealer has {} cards and {} points".format(dealer, dealerCount))
            break


if __name__ == '__main__':
    playGame()

